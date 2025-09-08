import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def set_sidebar_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def set_page_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Set the background images for the entire app ---
# This URL will be used for the page background
page_bg_url = "https://img.freepik.com/free-vector/black-background-with-focus-spot-light_1017-27230.jpg?semt=ais_hybrid&w=740&q=80" 
set_page_bg_from_url(page_bg_url)

# This URL will be used for the sidebar background
sidebar_bg_url = "https://images.pexels.com/photos/1679719/pexels-photo-1679719.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
set_sidebar_bg_from_url(sidebar_bg_url)


st.set_page_config(page_title="💬 Feedback", layout="centered")
st.title("💬 :blue[We Value Your Feedback!]")

st.markdown("""
Please share your thoughts about the :green[**Urban Loom Traffic Predictor**].
Your feedback helps us improve! 😊
""")

# --- Google Sheets Setup ---
def append_to_google_sheet(name, rating, comments):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
        client = gspread.authorize(creds)
        sheet = client.open("Urban Loom Feedback").sheet1 

        row = [name, rating, comments, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        sheet.append_row(row)
        return True
    except Exception as e:
        st.error(f"Failed to submit feedback. Error: {e}")
        return False

# --- Feedback Form ---
with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("👤 :violet[Your Name (optional)]")
    rating = st.number_input("⭐ :violet[Rate the App (1 = Poor, 5 = Excellent)]", min_value=1, max_value=5, step=1)
    comments = st.text_area("📝 :violet[Your Feedback]")

    submit = st.form_submit_button("✅ :green[Submit Feedback]")

# --- Submission Logic ---
if submit:
    if not comments:
        st.warning("⚠️Please provide some feedback before submitting.")
    else:
        if append_to_google_sheet(name if name else "Anonymous", rating, comments):
            st.success("🎉 Thank you for your feedback! It has been successfully submitted.")

            with st.expander("📋 Your Submitted Feedback"):
                st.markdown(f"**Name:** {name if name else 'Anonymous'}")
                st.markdown(f"**Rating:** {rating} / 5")
                st.markdown(f"**Comments:** {comments}")