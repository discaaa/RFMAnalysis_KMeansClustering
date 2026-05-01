import streamlit as st

# def show():
st.title("Customer Segmentation for E-Commerce")
st.markdown("""<h4 style='color:lightblue;'>Using RFM & K-Means</h4>""", unsafe_allow_html=True)
    
st.markdown("""---""")

st.markdown("""
### Group Members :
- 2802415744 - Mathilda Rafaela Christy Nugroho
- 2802420315 - Adisca Gandawidjaja
- 2802420334 - Alicia Angelina Jusup
                
---
    
### Project Overview
This project aims to segment customer based on their purchasing behavior using **RFM Analysis** and **K-Means Clustering**.
The segmentation helps businesses understand customer value and create targeted marketing strategies.
    
---
                
### Project Background
In a competitive retail environment nowadays, understanding customer behavior is essential for business to improve marketing strategies and increase revenues. Many companies face challenges in identifying which customers are valuable, which customers are at risk of leaving, and how to effectively target different and new customer groups.
    
By performing customer segmentation, companies can : 
- Identify high-value and low-value customers
- Improve marketing strategies
- Increase customer rentention
    
---
                
### Objectives
""")

st.image("../Images/objectives.jpg", caption="Project Objectives")

st.markdown("""
The objectives of this project are :
- Analyze customer behavior using RFM (Recency, Frequency, Monetary)
- Group customer into meaningful segments
- Provide insights for decision-making in business
""")


st.markdown("""
---
### Methodology
This project uses:
""")
st.image("../Images/rfm.avif", caption="RFM Metrics")

st.markdown("""
- **RFM Analysis**
    - Recency -> How recently a customer purchased
    - Frequency -> How often they purchase
    - Monetary -> How much they spend
    - We use RFM Analysis beacause it represents customer purchasing behavior effectively, simple, interpretable, and it also provides meaningful insights into customer value
    - Limitations :
        - Does not consider customer demographics
        - Sensitive to outliers (extreme values)
        - Only focus on pas behavior
""")

st.image("../Images/kmeans.avif", caption="K-Means Clustering")

st.markdown("""
- **K-Means Clustering**
    - An unsupervised learning algorithm for grouping data
    - Groups customer based on similarity
    - We use K-Means Clustering because it works well with numerical features, suitable for no labels data, and helps group customers based on behavioral similarity
    - Limitations :
        - Requires predefined number of clusters
        - Sensitive to initial centroid selection
---
                
### Dataset
- Source : Online Retail Dataset
- Platform : Kaggle
- Link : https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset
- Dataset Description :
                
    -> This dataset includes transactions that occurred between December 2010 and December 2011
- Dataset Attributes :
    - **InvoiceNo** : unique identifier for each transaction
    - **StockCode** : unique code for every product
    - **Description** : name of the product
    - **Quantity** : number of items purchased per transaction
    - **InvoiceDate** : date and time of the transaction
    - **UnitPrice** : price per item
    - **CustomerID** : unique identifier for each customer
    - **Country** : country where the customer resides
    """)
    
st.markdown("""
---
                
### Expected Output
Customer are segmented into :
- High-Value Customers (Cluster 2)
- Loyal Customers (Cluster 0)
- Low-Value Customers (Cluster 3)
- Lost Customers (Cluster 1)
""")