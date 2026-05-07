import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
dataset_path = BASE_DIR / "Dataset" / "online_retail.csv"
dataset = pd.read_csv(dataset_path)

# Load Data & Model
# @st.cache_data()
# def load_data():
#     return pd.read_csv(".././Dataset/online_retail.csv")

@st.cache_resource
def load_model():
    kmeans = pickle.load(open('.././model/kmeans.pkl', 'rb'))
    scaler = pickle.load(open('.././model/scaler.pkl', 'rb'))
    rfm = pd.read_csv(open('.././model/rfm.csv'))
    wcss = pickle.load(open('.././model/wcss.pkl', 'rb'))
    return kmeans, scaler, rfm, wcss

# dataset = load_data()
kmeans, scaler, rfm, wcss = load_model()

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #050816;
    color: white;
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Card */
.custom-card {
    background: linear-gradient(145deg, #0B1120, #111827);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

/* Title */
.main-title {
    font-size: 50px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-text {
    color: #9CA3AF;
    font-size: 18px;
}

/* Section title */
.section-title {
    font-size: 34px;
    font-weight: 700;
    color: #2F80ED;
    margin-bottom: 20px;
}

/* Metric Card */
.metric-card {
    background: linear-gradient(145deg, #111827, #1F2937);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

.metric-number {
    font-size: 36px;
    font-weight: 700;
    color: #60A5FA;
}

.metric-label {
    color: #D1D5DB;
    font-size: 16px;
}

/* Radio button spacing */
div.row-widget.stRadio > div {
    flex-direction: row;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div>
        <div class='main-title'>
        Exploratory Data Analysis
    </div>

    <div class='sub-text'>
        Understand dataset structure, patterns, and customer purchasing behavior before model development
    </div>

    </div>
""", unsafe_allow_html=True)

st.markdown("""---""")

st.markdown("""
    <div>
        <div class='main-title'>
        Dataset Overview
    </div>
""", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-number'>{dataset.shape[0]:,}</div>
        <div class='metric-label'>Transactions</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-number'>{dataset.shape[1]}</div>
        <div class='metric-label'>Columns</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-number'>{dataset['CustomerID'].nunique():,}</div>
        <div class='metric-label'>Customers</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-number'>{dataset['Country'].nunique()}</div>
        <div class='metric-label'>Countries</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""---""")

tab1, tab2, tab3 = st.tabs([
    "📋 Dataset",
    "📈 Statistical Summary",
    "🧾 Data Entries"
])

with tab1:
    st.dataframe(dataset, use_container_width=True)

with tab2:
    st.dataframe(dataset.describe(), use_container_width=True)

with tab3:
    dataset_info = pd.DataFrame({
        "Column": dataset.columns,
        "Non-Null Count": dataset.notnull().sum().values,
        "Data Type": dataset.dtypes.values
    })

    st.dataframe(dataset_info, use_container_width=True)

st.markdown("""---""")

st.markdown("""
    <div class='main-title'>
        Missing Values
    </div>
""", unsafe_allow_html=True)

missing = dataset.isnull().sum().reset_index()
missing.columns = ['Column', 'Missing Values']

st.dataframe(missing, use_container_width=True)

st.markdown("""---""")

st.markdown("""
    <div class='main-title'>
        Data Visualization
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    filtered_dataset = dataset[dataset['UnitPrice'] > 100]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(filtered_dataset['UnitPrice'], bins=np.arange(0,10000,1000))
    ax.set_title("Unit Price Distribution")
    ax.set_xlabel("Unit Price")
    ax.set_ylabel("Total Transaction")
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    filtered_qty = dataset[dataset['Quantity'] > 0]
    fig, ax = plt.subplots(figsize=(6,4))
    ax.hist(filtered_qty['Quantity'], bins=np.arange(0,100,10))
    ax.set_title("Quantity Distribution")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Total Transaction")
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    dataset['TotalPrice'] = dataset['Quantity'] * dataset['UnitPrice']
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(dataset['TotalPrice'][dataset['TotalPrice'] > 0], bins=np.arange(0,5000,1000))
    ax.set_title("Total Price Distribution")
    ax.set_xlabel("Total Price")
    ax.set_ylabel("Total Transaction")
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)


with col4:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    top_country = dataset['Country'].value_counts().head(5)
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.pie(top_country, labels=top_country.index, autopct='%1.1f%%')
    ax2.set_title("Top 5 Countries")
    st.pyplot(fig2)
    
st.markdown("""
<div class='main-title'>
    RFM Distribution
</div>
""", unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

with r1:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(5,4))
    ax.hist(rfm['Recency'], bins=30)
    ax.set_title("Recency Distribution")
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with r2:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(5,4))
    ax.hist(rfm['Frequency'], bins=np.arange(0,100,10))
    ax.set_title("Frequency Distribution")
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with r3:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(5,4))
    ax.hist(rfm['Monetary'], bins=np.arange(0,25000,1000))
    ax.set_title("Monetary Distribution")
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

# Relations between Attributes
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='main-title'>
    Relations Between Attributes
</div>
""", unsafe_allow_html=True)

relation = st.radio(
    "Choose Data Level",
    ["Transaction Level", "Customer Level (RFM)"]
)
if relation == "Transaction Level":
    colx, coly = st.columns(2)
    with colx:
        x = st.selectbox(
            "X-axis",
            ['Quantity', 'UnitPrice', 'TotalPrice']
        )
    with coly:
        y = st.selectbox(
            "Y-axis",
            ['Quantity', 'UnitPrice', 'TotalPrice']
        )

    fig, ax = plt.subplots(figsize=(7,5))
    ax.scatter(dataset[x], dataset[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"{x} vs {y}")
    st.pyplot(fig)

else:
    colx, coly = st.columns(2)
    with colx:
        x = st.selectbox(
            "X-axis",
            ['Recency', 'Frequency', 'Monetary']
        )
    with coly:
        y = st.selectbox(
            "Y-axis",
            ['Recency', 'Frequency', 'Monetary']
        )

    fig, ax = plt.subplots(figsize=(7,5))
    scatter = ax.scatter(
        rfm[x],
        rfm[y],
        c=rfm['Cluster']
    )
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"{x} vs {y}")
    st.pyplot(fig)

st.markdown("""
<br><br>
<div style='text-align:center; color:#6B7280; font-size:15px;'>
    By Group 4 • Machine Learning Group Assignment Project
</div>
""", unsafe_allow_html=True)