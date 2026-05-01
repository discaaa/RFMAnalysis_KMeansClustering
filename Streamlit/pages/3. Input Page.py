import streamlit as st
import pandas as pd
import pickle

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

st.title("Input Customer Data")
st.write("Enter Customer Information for Segmentation")

with st.form("input_form"):
    recency = st.number_input("Recency (Days since Last Purchase)", min_value=0, help="Lower value means more recent purchase")
    frequency = st.number_input("Frequency (Number of Transactions)", min_value=0, help="Higher value means more frequent purchases")
    monetary = st.number_input("Monetary (Total Spending)", min_value=0, help="Higher value means more valueable customer")

    submit = st.form_submit_button("Submit")

if submit:
    if recency == 0 and frequency == 0 and monetary == 0:
        st.warning("Please input valid data")
    else:
        st.session_state['input_data'] = {
            "Recency": recency,
            "Frequency": frequency,
            "Monetary": monetary,
        }

        st.success("Data submitted successfully!")
        st.write("### Input Summary")
        st.write(st.session_state['input_data'])
