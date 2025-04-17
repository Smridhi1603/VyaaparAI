import streamlit as st
import streamlit.components.v1 as components

st.title("My Streamlit App with Botpress Chat")

components.iframe(
    "https://cdn.botpress.cloud/webchat/v2.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/04/16/20/20250416202820-LAN4BXM2.json",
    height=600,
    width=400,
    scrolling=False,
)