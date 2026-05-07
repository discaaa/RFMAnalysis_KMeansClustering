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

from sklearn.metrics import silhouette_score, davies_bouldin_score
scaler = pickle.load(open(".././model/scaler.pkl", "rb"))

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

/* Main title */
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
    margin-bottom: 30px;
}

/* Section title */
.section-title {
    font-size: 34px;
    font-weight: 700;
    color: #2F80ED;
    margin-bottom: 20px;
}

/* Card */
.custom-card {
    background: linear-gradient(145deg, #0B1120, #111827);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

/* Metric Card */
.metric-card {
    background: linear-gradient(145deg, #111827, #1F2937);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Metric Value */
.metric-value {
    font-size: 42px;
    font-weight: 700;
    color: #60A5FA;
}

/* Metric Label */
.metric-label {
    color: #D1D5DB;
    font-size: 16px;
}

/* Description */
.desc {
    color: #D1D5DB;
    line-height: 1.8;
}

/* Checkbox spacing */
div.row-widget.stCheckbox {
    padding-top: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='main-title'>
        Model Evaluation Dashboard
    </div>

    <div class='sub-text'>
    Evaluate K-Means Clustering performance using Elbow Method, 
    Silhouette Score, and Davies-Bouldin Index
    </div>
""", unsafe_allow_html=True)

st.markdown(""" --- """)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-value'>4</div>
        <div class='metric-label'>Selected Clusters</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    sil_score = silhouette_score(
        scaler.transform(rfm[['Recency','Frequency','Monetary']]),
        rfm['Cluster']
    )

    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-value'>{sil_score:.3f}</div>
        <div class='metric-label'>Silhouette Score</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    dbi_score = davies_bouldin_score(
        scaler.transform(rfm[['Recency','Frequency','Monetary']]),
        rfm['Cluster']
    )

    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-value'>{dbi_score:.3f}</div>
        <div class='metric-label'>Davies-Bouldin Index</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(""" --- """)

st.markdown("""
    <div class='main-title'>
        Elbow Method
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1], gap="medium")

with col1:
    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        range(1,11),
        wcss,
        marker='o'
    )

    ax.set_xlabel("Number of Clusters")
    ax.set_ylabel("WCSS")
    ax.set_title("Elbow Method")

    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='custom-card'>

    <h2 style='color:#60A5FA;'>
        Insight
    </h2>

    <p class='desc'>
    The elbow graph shows that the WCSS value starts slowing down around 
    cluster 3-4.
    </p>

    <p class='desc'>
    Therefore, <b>4 clusters</b> were selected because they provide a good balance 
    between compactness and segmentation quality.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown(""" --- """)

st.markdown("""
    <div class='main-title'>
        Customer Cluster Data
    </div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs([
    "📋 Data Preview",
    "📊 Cluster Distribution"
])

with tab1:
    st.dataframe(rfm.head(), use_container_width=True)

with tab2:
    cluster_counts = rfm['Segment'].value_counts()
    st.bar_chart(cluster_counts)

st.markdown(""" --- """)

st.markdown("""
    <div class='main-title'>
        Evaluation Result
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    show_silhouette = st.checkbox("Show Silhouette Score")

with col2:
    show_dbi = st.checkbox("Show Davies-Bouldin Index")

if show_silhouette:
    st.metric(
        "Silhouette Score",
        round(sil_score, 4)
    )
    st.write("""
    Measures how well-separated clusters are.
    
    - Closer to **1** → Better separation
    - Around **0** → Overlapping clusters
    - Negative → Poor clustering
    """)
    if sil_score > 0.5:
        st.success("✅ Clusters are well separated.")
    else:
        st.warning("⚠️ Clusters are not strongly separated.")
    st.markdown("</div>", unsafe_allow_html=True)

if show_dbi:
    st.metric(
        "Davies-Bouldin Index",
        round(dbi_score, 4)
    )
    st.write("""
    Measures cluster compactness and similarity.
    
    - Lower value → Better clustering
    - Higher value → More overlapping clusters
    """)

    if dbi_score < 1:
        st.success("✅ Clusters are compact and distinct.")
    else:
        st.warning("⚠️ Clusters are overlapping.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(""" --- """)

st.markdown("""
    <div class='main-title'>
        Final Insight
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='custom-card'>

<p class='desc'>
The evaluation results indicate that the K-Means model is capable of 
grouping customers into meaningful segments based on purchasing behavior.
</p>

<p class='desc'>
The selected number of clusters provides a reasonable balance between 
cluster separation and compactness, making the segmentation useful for 
business analysis and marketing strategies.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<br><br>
<div style='text-align:center; color:#6B7280; font-size:15px;'>
    By Group 4 • Machine Learning Group Assignment Project
</div>
""", unsafe_allow_html=True)