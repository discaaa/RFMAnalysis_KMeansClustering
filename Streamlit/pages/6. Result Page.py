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

st.title("Customer Segmentation Result")

if 'input_data' not in st.session_state:
    st.warning("Please input data first")
    st.stop()

data = st.session_state['input_data']

input_array = np.array([
    data['Recency'], data['Frequency'], data['Monetary']
]).reshape(1, -1)

scaled = scaler.transform(input_array)
cluster = kmeans.predict(scaled)[0]

def get_segment(cluster):
    if cluster == 2:
        return "High Value Customer"
    elif cluster == 0:
        return "Loyal Customer"
    elif cluster == 3:
        return "Low Value Customer"
    else:
        return "Lost Customer"

segment = get_segment(cluster)

st.subheader("Prediction Result")
st.success(f"Customer belongs to : **{segment}**")

st.subheader("Segment Description")

if segment == "High Value Customer":
    st.write("Customers who frequently purchase and spend a high amount of money.")

elif segment == "Loyal Customer":
    st.write("Customers who regularly purchase but with moderate spending.")

elif segment == "Low Value Customer":
    st.write("Customers who rarely purchase and spend less.")

else:
    st.write("Customers who have not purchased recently and are likely inactive.")

st.subheader("Business Recommendation")

if segment == "High Value Customer":
    st.info("Provide exclusive offers, loyalty rewards, and premium services.")

elif segment == "Loyal Customer":
    st.info("Maintain engagement with promotions and personalized marketing.")

elif segment == "Low Value Customer":
    st.info("Encourage purchases through discounts and marketing campaigns.")

else:
    st.info("Re-engage customers with special offers or reactivation campaigns.")

import pandas as pd

st.subheader("Input Summary")

df_input = pd.DataFrame([data])
st.table(df_input)