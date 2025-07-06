import streamlit as st
import requests
import datetime

BASE_URL = "http://localhost:8000"  # Backend endpoint

# Page config
st.set_page_config(
    page_title="🌍 AI Trip Planner",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# App title
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🌍 AI Trip Planner</h1>",
    unsafe_allow_html=True,
)

st.markdown("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Prompt header
st.markdown(
    "<h3 style='text-align: center;'>How can I help you plan your next trip?</h3>",
    unsafe_allow_html=True,
)

# Chat input form
with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input(
        "✈️ Enter your trip query:",
        placeholder="e.g. Plan a trip to Goa for 5 days",
    )
    submit_button = st.form_submit_button("Generate Itinerary")

if submit_button and user_input.strip():
    try:
        with st.spinner("Generating your AI-powered itinerary..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            generated_time = datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')

            # Display result
            st.markdown(f"""
            ### ✅ **Your AI-Generated Travel Plan**

            **Generated:** {generated_time}  
            **Created by:** AI Travel Planner

            ---

            {answer}

            ---

            *Please verify all information, especially prices, operating hours, and travel requirements before your trip.*
            """)

            # Download button for the itinerary
            itinerary_filename = f"AI_Itinerary_{generated_time.replace(':', '-')}.txt"
            st.download_button(
                label="💾 Download Itinerary",
                data=answer,
                file_name=itinerary_filename,
                mime="text/plain",
            )

        else:
            st.error("❌ Bot failed to respond: " + response.text)

    except Exception as e:
        st.error(f"❌ The response failed due to: {e}")
