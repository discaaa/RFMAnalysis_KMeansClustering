import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

st.title('Exploratory Data Analysis')
st.write("-> First process in analyzing data to learn its structure, pattern, and quality before creating a model")
    
st.markdown("""
---
### Dataset
""")
st.write(dataset)
    

option = st.radio(
    "-> Choose Analysis",
    ["Statistical Summary", "Data Entries"]
)
    
if option == "Statistical Summary":
    st.subheader("Statistical Summary")
    st.write(dataset.describe())

elif option == "Data Entries":
    st.subheader("Data Entries")
    dataset_info = pd.DataFrame({
        "Column" : dataset.columns,
        "Non-Null Count": dataset.notnull().sum().values,
        "Data Type" : dataset.dtypes.values
    })

    st.dataframe(dataset_info)

st.markdown("""
---
### Missing Values
""")
st.write(dataset.isnull().sum())

st.markdown("""
---
### Data Visualization
""")
filtered_dataset = dataset[dataset['UnitPrice'] > 100]
fig, ax = plt.subplots()
ax.hist(filtered_dataset['UnitPrice'], bins=np.arange(0,10000,1000))
ax.set_title("Unit Price Distribution")
ax.set_xlabel("Unit Price")
ax.set_ylabel("Total Transaction")
st.pyplot(fig)

dataset['TotalPrice'] = dataset['Quantity'] * dataset['UnitPrice']
fig, ax = plt.subplots()
ax.hist(dataset['TotalPrice'][dataset['TotalPrice'] > 0], bins=np.arange(0,5000,1000))
ax.set_title("Total Price Distribution")
ax.set_xlabel("Total Price")
ax.set_ylabel("Total Transaction")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(rfm['Recency'], bins=30)
ax.set_title("Recency Distribution")
ax.set_xlabel("Recent Purchase (Days)")
ax.set_ylabel("Total Customer")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(rfm['Frequency'], bins=np.arange(0,100,10))
ax.set_title("Frequency Distribution")
ax.set_xlabel("Transaction Frequency")
ax.set_ylabel("Total Customer")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(rfm['Monetary'], bins=np.arange(0, 25000, 1000))
ax.set_title("Monetary Distribution")
ax.set_xlabel("Total Spending")
ax.set_ylabel("Total Customer")
st.pyplot(fig)

st.write('Country Distribution: ')
st.bar_chart(dataset['Country'].value_counts())

st.write("#### Top 5 Countries")
top_country = dataset['Country'].value_counts().head(5)
fig2, ax2 = plt.subplots()
ax2.pie(top_country, labels=top_country.index, autopct='%1.1f%%')
st.pyplot(fig2)

# Relations between Attributes
st.markdown(""" --- """)
st.write("### Relations Between Attributes")

relation = st.radio(
    "Select Data Level",
    ["Transaction Level", "Customer Level (RFM)"]
)

if relation == "Transaction Level":
    x = st.selectbox("X-axis", ['Quantity', 'UnitPrice', 'TotalPrice'])
    y = st.selectbox("Y-axis", ['Quantity', 'UnitPrice', 'TotalPrice'])
    fig, ax = plt.subplots()
    ax.scatter(dataset[x], dataset[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)

else:
    x = st.selectbox("X-axis", ['Recency', 'Frequency', 'Monetary'])
    y = st.selectbox("Y-axis", ['Recency', 'Frequency', 'Monetary'])

    fig, ax = plt.subplots()
    ax.scatter(rfm[x], rfm[y], c=rfm['Cluster'])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig) 
