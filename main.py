import os
import time
from exa_py import Exa
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Set page configuration
st.set_page_config(
    page_title="Company Analyst Helper",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load environment variables
load_dotenv()

# Retrieve API keys
EXA_API_KEY = st.secrets["EXA_API_KEY"]
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error(f"Error: {e}")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
        color: #333333;
        font-family: 'Poppins', sans-serif;
    }
    .stButton > button {
        background-color: #0066ff;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        transition: 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0052cc;
        color: #ffffff;
    }
    .stMarkdown h1, h2, h3 {
        color: white;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# System message for the GenerativeModel
SYSTEM_MESSAGE = """You are a helpful assistant writing a research report about a company. 
Summarize the users input into multiple paragraphs. 
Be extremely concise, professional, and factual as possible. 
The first paragraph should be an introduction and summary of the company. 
The second paragraph should include pros and cons of the company. 
Things like what are they doing well, things they are doing poorly or struggling with. 
And ideally, suggestions to make the company better."""

model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=SYSTEM_MESSAGE)
exa = Exa(api_key=EXA_API_KEY)

# Sidebar
with st.sidebar:
    st.header(":gear: Tech Stack")
    st.markdown("""
    - **Streamlit**: Frontend framework
    - **Exa AI**: Neural search for competitors
    - **Google Gemini**: Generative AI for insights
    """)

# Main Header
st.markdown("<h1>Company Analyst Helper</h1>", unsafe_allow_html=True)
st.markdown("<h3>Analyze your competitors with AI</h3>", unsafe_allow_html=True)

# Input Section
st.markdown("### Enter the Company URL:")
st.warning(":exclamation: Avoid using subdomains (e.g., `drive.google.com`). Use the base URL instead.")

st.session_state.input_url = st.text_input(
    "Company URL", st.session_state.input_url, placeholder="https://example.com"
)
submit = st.button("Analyze Competitors :mag:")

if submit and st.session_state.input_url:
    with st.spinner("Fetching competitor data..."):
        try:
            search_response = exa.find_similar_and_contents(
                st.session_state.input_url,
                highlights={"num_sentences": 2},
                num_results=10
            )
            companies = search_response.results
            st.session_state.urls = [c.url for c in companies]
            
            st.success("Competitors successfully identified!")
            with st.expander(":scroll: Competitors Found"):
                for c in companies:
                    st.write(f"**{c.title}**: {c.url}")

            st.session_state.competitor = st.selectbox(
                "Select a Competitor for Analysis", st.session_state.urls
            )
            final_submit = st.button("Generate Report :clipboard:")

            if final_submit and st.session_state.competitor:
                with st.spinner("Generating report..."):
                    all_contents = ""
                    search_response = exa.search_and_contents(
                        st.session_state.competitor,
                        type="keyword",
                        num_results=3
                    )
                    research_response = search_response.results
                    for r in research_response:
                        all_contents += r.text

                    response = model.generate_content(all_contents)
                    st.markdown("### :bar_chart: Competitor Analysis Report")
                    st.write(response.text)

        except Exception as e:
            st.error("Error fetching data. Please try a different URL.")
            st.error(f"Details: {e}")
