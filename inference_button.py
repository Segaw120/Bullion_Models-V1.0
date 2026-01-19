import streamlit as st
import requests
import os

st.title('Trigger Daily Scan')

# Get the token from environment variables
HF_TOKEN = os.getenv('HF_TOKEN')

if st.button('Trigger Scan'):
    url = "https://segaab120-raymond-model-v1-0.hf.space/trigger-daily-scan"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }
    response = requests.post(url, headers=headers)
    st.write("Response status code:", response.status_code)
    st.write("Response content:", response.text)
