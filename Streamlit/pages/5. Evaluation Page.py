import streamlit as st
import matplotlib.pyplot as plt
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

st.title("Model Evaluation")
st.subheader("Silhouette Score")
score = 0.616
st.metric("Silhouette Score", round(score, 3))
st.write("The clustering result shows a good seperation between clusters")

st.markdown(""" --- """)

st.subheader("Elbow Method")

fig, ax = plt.subplots()
ax.plot(range(1,11), wcss, marker='o')
ax.set_xlabel("Number of Clusters")
ax.set_ylabel("WCSS")
ax.set_title("Elbow Method")

st.pyplot(fig)

st.markdown(""" --- """)

st.subheader("Customer Cluster Distribution")
cluster_counts = rfm['Segment'].value_counts()
st.bar_chart(cluster_counts)