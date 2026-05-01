import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load Data & Model
@st.cache_data()
def load_data():
    return pd.read_csv(".././Dataset/online_retail.csv")

@st.cache_resource
def load_model():
    kmeans = pickle.load(open('.././model/kmeans.pkl', 'rb'))
    scaler = pickle.load(open('.././model/scaler.pkl', 'rb'))
    rfm = pd.read_csv(open('.././model/rfm.csv'))
    wcss = pickle.load(open('.././model/wcss.pkl', 'rb'))
    return kmeans, scaler, rfm, wcss

dataset = load_data()
kmeans, scaler, rfm, wcss = load_model()

def get_segment(cluster):
    if cluster == 2:
        return "High Value Customer"
    elif cluster == 0:
        return "Loyal Customer"
    elif cluster == 3:
        return "Low Value Customer"
    else:
        return "Lost Customer"
    
st.title("Model Prediction")

if 'input_data' not in st.session_state:
    st.warning("Please input data first")

else:
    data = st.session_state['input_data']

    st.write("### Your Data")
    st.write(data)

    input_array = np.array([
        data['Recency'],
        data['Frequency'],
        data['Monetary']
    ]).reshape(1, -1)

    scaled = scaler.transform(input_array)
    cluster = kmeans.predict(scaled)

    st.success(f"Predicted Cluster: {cluster[0]}")
    segment = get_segment(cluster[0])
    st.success(f"Customer Segment: {segment}")
    


