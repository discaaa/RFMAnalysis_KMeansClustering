import streamlit as st

st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <div style='
        background: linear-gradient(90deg, #4F46E5, #9333EA);
        padding: 35px 25px;
        border-radius: 25px;
    '>
        <h1 style='
            color: white;
            font-size: 52px;
            font-weight: 800;
            margin-bottom: 10px;
            line-height: 1.3;
        '>
            Customer Segmentation for E-Commerce
        </h1>
        <h2 style='
            color: white;
            font-size: 40px;
            font-weight: 700;
            margin-top: 0;
        '>
            Using RFM & K-Means Clustering
        </h2>
    </div>
    <div style='margin-top: 20px;'>
        <span style='
            background-color: #2563EB;
            color: white;
            padding: 10px 24px;
            border-radius: 25px;
            font-size: 20px;
            font-weight: bold;
        '>
            Group 4 - Machine Learning
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background-color: #050816;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.custom-card {
    background: linear-gradient(145deg, #0B1120, #111827);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    height: 100%;
    transition: 0.3s;
}

.custom-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 35px rgba(0,128,255,0.25);
}

.section-title {
    color: #2F80ED;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 20px;
    border-left: 5px solid #2F80ED;
    padding-left: 15px;
}

.sub-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
    color: white;
}

.custom-text {
    font-size: 17px;
    line-height: 1.8;
    color: #D1D5DB;
}

.member-list li {
    margin-bottom: 12px;
    font-size: 17px;
    color: #E5E7EB;
}

.highlight {
    color: #60A5FA;
    font-weight: 600;
}

.divider {
    margin-top: 20px;
    margin-bottom: 20px;
    border-top: 1px solid rgba(255,255,255,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""---""")
st.markdown("""
<div style='margin-bottom:20px;'>

<h1 style='
    color:white;
    font-size:42px;
    font-weight:700;
    margin-bottom:10px;
'>
    Introduction
</h1>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1,1], gap="medium")

with col1:
    st.markdown("""
    <div class='custom-card'>
    
    <div class='sub-title'>
        Group Members
    </div>

    <ul class='member-list'>
        <li>2802415744 - Mathilda Rafaela Christy Nugroho</li>
        <li>2802420315 - Adisca Gandawidjaja</li>
        <li>2802420334 - Alicia Angelina Jusup</li>
    </ul>

    <div class='divider'></div>

    <div class='sub-title'>
        Project Overview
    </div>

    <p class='custom-text'>
        This project aims to segment customers based on their purchasing behavior using 
        <span class='highlight'>RFM Analysis</span> and 
        <span class='highlight'>K-Means Clustering</span>.
        The segmentation helps businesses understand customer value and create targeted marketing strategies.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='custom-card'>

    <div class='sub-title'>
        Project Background
    </div>

    <p class='custom-text'>
        In today's competitive retail environment, understanding customer behavior is essential 
        for businesses to improve marketing strategies and increase revenue.
        Many companies face challenges in identifying valuable customers, detecting customers 
        at risk of leaving, and effectively targeting different customer groups.
    </p>

    <p class='custom-text'>
        By performing customer segmentation, companies can:
    </p>

    <ul class='member-list'>
        <li>Identify high-value and low-value customers</li>
        <li>Improve marketing strategies</li>
        <li>Increase customer retention</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

st.markdown("""---""")

st.markdown("""
    <div style='margin-bottom:20px;'>

    <h1 style='
        color:white;
        font-size:42px;
        font-weight:700;
        margin-bottom:10px;
    '>
        Objectives
    </h1>
    """, unsafe_allow_html=True)

st.image("../Images/objectives.jpg", caption="Project Objectives")

obj1, obj2, obj3 = st.columns(3)

with obj1:
    st.markdown("""
    <div class='custom-card' style='text-align:center;'>
        <h4 style='color:#60A5FA;'>Analyze Customer Behavior</h4>
        <p class='custom-text'>
            Analyze customer behavior using RFM metrics
        </p>
    </div>
    """, unsafe_allow_html=True)

with obj2:
    st.markdown("""
    <div class='custom-card' style='text-align:center;'>
        <h4 style='color:#60A5FA;'>Customer Segmentation</h4>
        <p class='custom-text'>
            Group customers into meaningful clusters
        </p>
    </div>
    """, unsafe_allow_html=True)

with obj3:
    st.markdown("""
    <div class='custom-card' style='text-align:center;'>
        <h4 style='color:#60A5FA;'>Business Insight</h4>
        <p class='custom-text'>
            Support business decision-making strategies
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""---""")

st.markdown("""
<div style='margin-bottom:20px;'>

<h1 style='
    color:white;
    font-size:42px;
    font-weight:700;
    margin-bottom:10px;
'>
    Methodology
</h1>

<p style='
    color:#9CA3AF;
    font-size:18px;
'>
    Methods used for customer segmentation analysis
</p>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1], gap="medium")

with col1:
    st.image("../Images/rfm.avif", use_container_width=True)
    st.markdown("""
        <div class='custom-card'>

        <h4 style='color:#60A5FA;'>Limitations</h4>

        <ul class='member-list'>
            <li>Does not consider demographics</li>
            <li>Sensitive to outliers</li>
            <li>Focuses only on past behavior</li>
        </ul>
    """,unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='custom-card'>

    <h2 style='color:#2F80ED;'>RFM Analysis</h2>

    <p class='custom-text'>
        RFM Analysis evaluates customer purchasing behavior using:
    </p>

    <ul class='member-list'>
        <li><b>Recency</b> → How recently a customer purchased</li>
        <li><b>Frequency</b> → How often they purchase</li>
        <li><b>Monetary</b> → How much they spend</li>
    </ul>

    <p class='custom-text'>
        This method is simple, interpretable, and effective for identifying customer value.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns([1,1], gap="medium")

with col3:
    st.markdown("""
    <div class='custom-card'>

    <h2 style='color:#2F80ED;'>K-Means Clustering</h2>

    <p class='custom-text'>
        K-Means is an unsupervised learning algorithm used to group customers based on similarity.
    </p>

    <p class='custom-text'>
        It works well for numerical data and helps identify behavioral patterns.
    </p>

    <h4 style='color:#60A5FA;'>Limitations</h4>

    <ul class='member-list'>
        <li>Requires predefined clusters</li>
        <li>Sensitive to centroid initialization</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

with col4:
    st.image("../Images/kmeans.avif", use_container_width=True)
    st.markdown("""
    <div class='custom-card'>

    <h2 style='color:#2F80ED;'>Why we use K-Means ?</h2>

    <p class='custom-text'>
    We use K-Means Clustering because it works well with numerical features, suitable for no labels data, and helps group customers based on behavioral similarity
    </p>
    """, unsafe_allow_html=True)

st.markdown("""---""")

st.markdown("""
<div style='margin-bottom:20px;'>

<h1 style='
    color:white;
    font-size:42px;
    font-weight:700;
    margin-bottom:10px;
'>
    Dataset
</h1>

<p style='
    color:#9CA3AF;
    font-size:18px;
'>
    Dataset used in this project :
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='custom-card'>

<h3 style='color:#2F80ED;'>Dataset Information</h3>

<ul class='member-list'>
    <li><b>Source</b> : Online Retail Dataset</li>
    <li><b>Platform</b> : Kaggle</li>
    <li>
        <b>Link</b> :
        <a href='https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset'
        target='_blank'
        style='color:#60A5FA; text-decoration:none;'>
        Online Retail Dataset
        </a>
    </li>
</ul>

<p class='custom-text'>
    This dataset contains retail transaction data from December 2010 to December 2011.
</p>

<h3 style='color:#2F80ED;'>Dataset Attributes</h3>

<ul class='member-list'>
    <li><b>InvoiceNo</b> → Transaction identifier</li>
    <li><b>StockCode</b> → Product code</li>
    <li><b>Description</b> → Product name</li>
    <li><b>Quantity</b> → Purchased quantity</li>
    <li><b>InvoiceDate</b> → Transaction date & time</li>
    <li><b>UnitPrice</b> → Price per item</li>
    <li><b>CustomerID</b> → Customer identifier</li>
    <li><b>Country</b> → Customer country</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("""---""")

st.markdown("""
<div style='margin-bottom:20px;'>

<h1 style='
    color:white;
    font-size:42px;
    font-weight:700;
    margin-bottom:10px;
'>
    Expected Output
</h1>

<p style='
    color:#9CA3AF;
    font-size:18px;
'>
    Final customer segmentation result
</p>

</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

clusters = [
    ("🔥", "Cluster 2", "High-Value"),
    ("💵", "Cluster 0", "Loyal"),
    ("📉", "Cluster 3", "Low-Value"),
    ("⚠️", "Cluster 1", "Lost")
]

for col, (emoji, cluster, label) in zip([c1, c2, c3, c4], clusters):
    with col:
        st.markdown(f"""
        <div class='custom-card' style='text-align:center;'>
            <h1>{emoji}</h1>
            <h3 style='color:#60A5FA;'>{cluster}</h3>
            <p class='custom-text'>{label} Customers</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<br><br>
<div style='text-align:center; color:#6B7280; font-size:15px;'>
    By Group 4 • Machine Learning Group Assignment Project
</div>
""", unsafe_allow_html=True)