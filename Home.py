import streamlit as st

st.set_page_config(page_title="Product Demand Forecasting", layout="wide")

# st.title("VYAAPAR AI")

st.markdown("""
    <style>
    .custom-title {
        font-family: 'Georgia', serif;
        font-size: 60px;
        font-weight: bold;
        color: black ;
        text-align: left ;
    }
    img {
        width: 100%;
        height: auto;
    }

    </style>
    <div class="custom-title">Welcome to Vyaapar AI</div>
""", unsafe_allow_html=True)


st.markdown("""
VYAAPAR AI is your smart inventory assistant. It uses AI to forecast demand, cut overstock and stockouts, and data-driven insights — all in one platform.
""")
st.image("C:/Users/Smridhi/Desktop/Projects/Forecasting_System-main/pic.jpg", caption="", use_container_width=True)

