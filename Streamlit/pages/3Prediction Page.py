import streamlit as st
import pandas as pd
import pickle
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

kmeans, scaler, rfm, wcss = load_model()

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #050816;
    color: white;
}

/* Main Container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main Title */
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

/* Card */
.custom-card {
    background: linear-gradient(145deg, #0B1120, #111827);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

/* Section Title */
.section-title {
    font-size: 30px;
    font-weight: 700;
    color: #2F80ED;
    margin-bottom: 20px;
}

/* Input Label */
label {
    color: white !important;
    font-weight: 500 !important;
}

/* Metric Card */
.metric-card {
    background: linear-gradient(145deg, #111827, #1F2937);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Segment Box */
.segment-box {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    background: linear-gradient(145deg, #1E3A8A, #2563EB);
    color: white;
    margin-bottom: 20px;
}

/* Description Text */
.desc {
    color: #D1D5DB;
    line-height: 1.8;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='main-title'>
        Customer Segmentation Prediction
    </div>

    <div class='sub-text'>
        Enter customer purchasing information to predict customer segment using 
        RFM Analysis & K-Means Clustering
    </div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class='metric-card'>
        <h2>⏳</h2>
        <h3>Recency</h3>
        <p class='desc'>
            Lower value means recent purchases
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-card'>
        <h2>🔄</h2>
        <h3>Frequency</h3>
        <p class='desc'>
            Higher value means more transactions
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-card'>
        <h2>💰</h2>
        <h3>Monetary</h3>
        <p class='desc'>
            Higher value means more spending
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
    <div class='main-title'>
    Input Your Data
    </div>
""", unsafe_allow_html=True)

with st.form("input_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        recency = st.number_input(
            "Recency",
            min_value=0,
            help="Days since last purchase"
        )
    with col2:
        frequency = st.number_input(
            "Frequency",
            min_value=0,
            help="Number of transactions"
        )
    with col3:
        monetary = st.number_input(
            "Monetary",
            min_value=0,
            help="Total spending amount"
        )

    left, center, right = st.columns([1,2,1])
    with center:
        b1, b2 = st.columns(2)
        submit = b1.form_submit_button(
            "Submit",
            type="primary",
            use_container_width=True
        )
        predict = b2.form_submit_button(
            "Predict",
            type="secondary",
            use_container_width=True
        )
st.markdown("</div>", unsafe_allow_html=True)

if submit:
    if recency == 0 and frequency == 0 and monetary == 0:
        st.warning("⚠️ Please input valid customer data")
    else:
        st.session_state['input_data'] = {
            "Recency": recency,
            "Frequency": frequency,
            "Monetary": monetary,
        }
        st.success("✅ Customer data submitted successfully!")

if predict:
    if 'input_data' not in st.session_state:
        st.warning("⚠️ Please submit customer data first!")
    else:
        data = st.session_state['input_data']
        input_array = np.array([
            data['Recency'],
            data['Frequency'],
            data['Monetary']
        ]).reshape(1, -1)

        scaled = scaler.transform(input_array)
        cluster = kmeans.predict(scaled)[0]

        segment_map = {
            2: "High Value Customer",
            0: "Loyal Customer",
            3: "Low Value Customer",
        }
        segment = segment_map.get(cluster, "Lost Customer")

        st.markdown("""
        <div class='main-title'>
            Prediction Result
        </div>
        """, unsafe_allow_html=True)

        emoji_map = {
            "High Value Customer": "🔥",
            "Loyal Customer": "💵",
            "Low Value Customer": "📉",
            "Lost Customer": "⚠️"
        }

        st.markdown(f"""
        <div class='segment-box'>
            <h1 style='font-size:60px;'>
                {emoji_map.get(segment)}
            </h1>
            <h2>
                {segment}
            </h2>
        </div>
        """, unsafe_allow_html=True)

        left, right = st.columns(2)
        with left:
            st.markdown("""
            <div class='custom-card'>
            <div class='section-title'>
                Customer Segment Description
            </div>
            """, unsafe_allow_html=True)

            if segment == "High Value Customer":
                st.info("""
                Customers who frequently purchase products and spend 
                a high amount of money.
                """)
            elif segment == "Loyal Customer":
                st.info("""
                Customers who regularly make purchases with moderate spending.
                """)
            elif segment == "Low Value Customer":
                st.info("""
                Customers who rarely purchase and contribute lower revenue.
                """)
            else:
                st.info("""
                Customers who have not purchased recently and are likely inactive.
                """)
            st.markdown("</div>", unsafe_allow_html=True)

        with right:
            st.markdown("""
            <div class='custom-card'>
            <div class='section-title'>
                Business Recommendation
            </div>
            """, unsafe_allow_html=True)
            if segment == "High Value Customer":
                st.success("""
                Provide exclusive rewards, premium services, 
                and loyalty programs.
                """)
            elif segment == "Loyal Customer":
                st.info("""
                Maintain engagement using personalized promotions 
                and campaigns.
                """)
            elif segment == "Low Value Customer":
                st.warning("""
                Encourage purchases through discounts 
                and targeted marketing.
                """)
            else:
                st.error("""
                Re-engage customers using special offers 
                and reactivation campaigns.
                """)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='main-title'>
            Input Summary
        </div>
        """, unsafe_allow_html=True)

        df_input = pd.DataFrame([data])
        st.dataframe(
            df_input,
            use_container_width=True
        )

st.markdown("""
<br><br>
<div style='text-align:center; color:#6B7280; font-size:15px;'>
    By Group 4 • Machine Learning Group Assignment Project
</div>
""", unsafe_allow_html=True)