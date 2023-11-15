import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st
import plotly.io as pio
import numpy as np
import random

def load_model_predict(X_test,saved_model_fname):
    import pickle
    # load the model from disk
    loaded_model = pickle.load(open(saved_model_fname, 'rb'))
    prediction = loaded_model.predict(X_test)
    return prediction

#Y predictions for the test data


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'
#--------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
st. set_page_config(layout="wide")
pio.templates.default = "simple_white"
side=st.sidebar
with open(r"C:\\Files\DSP\\mystyle.css") as design:
    st.markdown(f"<style>{design.read()}</style>", unsafe_allow_html=True)

st.title("Signal Viewer")


with side:
    st.subheader("Browse Signal")
    file = side.file_uploader("Upload Files", type={"csv", "txt", "xlsx"},key=1)
    file2 = side.file_uploader("Upload Files", type={"csv", "txt", "xlsx"})
    st.subheader("Browse Test Cases")



x1=[]
y1=[]
y2=[]

col1, col2 = st.columns(2)


#-----------------------------------------------------------------------------------------
with col1:
    st.subheader("Original Signal")
    figure = go.Figure()

    figure.update_layout(autosize=True,
    width=180000,
    height=600)
    #figure.add_trace(go.Scatter(x =x1, y = y1,mode = "lines",line=dict(color='green'),name='Orignal Signal'),)
    #figure.add_trace(go.Scatter(x =x1, y = y2,mode = "lines",line=dict(color='red'),name='Orignal Signal'),)

for i in range(0,190594):
        x1.append(0.1*i)
if file is not None :
    
    File = pd.read_csv(file)
    
    arrays = []
    for i in range(0,50):
        arrays.append(np.array(File.iloc[0:,i]))
        figure.add_trace(go.Scatter(x =x1, y = arrays[i],mode = "lines",line=dict(color=random_color()),name='Orignal Signal'),)
    


with col1:
    st.plotly_chart(figure,use_container_width=True,use_container_height=True)





#------------------------------------------------------------------------------------------------------------------------------

with col2:
    st.subheader("Filtered Signal")
    figure2 = go.Figure()

    figure2.update_layout(autosize=True,
    width=180000,
    height=600)
    #figure.add_trace(go.Scatter(x =x1, y = y1,mode = "lines",line=dict(color='green'),name='Orignal Signal'),)
    #figure.add_trace(go.Scatter(x =x1, y = y2,mode = "lines",line=dict(color='red'),name='Orignal Signal'),)


if file2 is not None :
    
    File2 = pd.read_csv(file2)
    arrays2 = []
    for i in range(0,50):
        arrays2.append(np.array(File2.iloc[0:,i]))
        figure2.add_trace(go.Scatter(x =x1, y = arrays2[i],mode = "lines",line=dict(color=random_color()),name='Filtered Signal'),)
    

with col2:
    st.plotly_chart(figure2,use_container_width=True,use_container_height=True)

#------------------------------------------------------------------------------------------------------------------

file3 = side.file_uploader("Upload Files", type={"csv"},key=2)

if file3 is not None :
    File3 = pd.read_csv(file3)
    arrays3 = []
    for i in range(0,59):
        arrays3.append(np.array(File3.iloc[0:,i]))
    data_array = [np.array(arrays3)]
    data_array= np.array(data_array)


    st.write("### DataFrame from CSV:")
    st.dataframe(File3)

    #Y predictions for the test data
    y_pred =load_model_predict(data_array, "C:\\Users\\emy33\\ds1ffinalized_model.sav")
    print(y_pred)
    
    st.subheader("Result")
    if y_pred ==[1]:
        st.write("Patient is thinking Right")
    else:
        st.write("Patient is thinking left")
    
    






