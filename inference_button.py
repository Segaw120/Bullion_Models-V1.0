import streamlit as st
import requests
import os

st.set_page_config(page_title="RayBot Triggers", layout="wide")
st.title('RayBot Trigger Dashboard')

# Get the token from environment variables
HF_TOKEN = os.getenv('HF_TOKEN')
BASE_URL = "https://segaab120-raymond-model-v1-0.hf.space"

if not HF_TOKEN:
    st.warning("HF_TOKEN environment variable is not set. Requests may fail if auth is required.")

st.markdown("### Daily Scan Triggers")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Standard Scan")
    st.markdown("Notifies **Signal Channel** + **Discord**")
    if st.button('Trigger Standard Scan', key='std_btn', use_container_width=True):
        url = f"{BASE_URL}/trigger-daily-scan"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
        try:
            with st.spinner("Sending Standard Request..."):
                response = requests.post(url, headers=headers)
            
            if response.status_code == 200:
                st.success(f"Success: {response.status_code}")
                st.json(response.json())
            else:
                st.error(f"Failed: {response.status_code}")
                st.write(response.text)
        except Exception as e:
            st.error(f"Request Error: {e}")

with col2:
    st.subheader("Inference Scan")
    st.markdown("Notifies **Private Inference Channel** Only")
    if st.button('Trigger Inference Scan', key='inf_btn', use_container_width=True):
        url = f"{BASE_URL}/trigger-inference-scan"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
        try:
            with st.spinner("Sending Inference Request..."):
                response = requests.post(url, headers=headers)
            
            if response.status_code == 200:
                st.success(f"Success: {response.status_code}")
                st.json(response.json())
            else:
                st.error(f"Failed: {response.status_code}")
                st.write(response.text)
        except Exception as e:
            st.error(f"Request Error: {e}")
