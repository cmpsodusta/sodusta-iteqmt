import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

# Add page title
add_page_title()

# Show pages in the sidebar with sections
show_pages(
    [   
        Section(""),
        Page("home.py"),
        Section("Applications"),
        Page("pages/crop_recom_streamlitapp.py", "Prediction", "1️⃣", in_section=True),
        Page("pages/basic_sentiment_analyzer.py", "Sentiment Analysis", "2️⃣", in_section=True),
        Page("pages/img_classification.py", "Image Classification", "3️⃣", in_section=True),

        Section("Source Codes"),
        Page("pages/crop_src.py", "Prediction Source", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "Sentiment Analysis Source", "2️⃣", in_section=True),
        Page("pages/image_classification_src.py", "Image Classification Source", "3️⃣", in_section=True),
    ]
)

# Personal Information Section
st.markdown("""
##### Personal Information

Name: Charlene Mae P. Sodusta  
Age: 21 years old  
Education: Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY  
Year: 3rd year Bachelor of Science in Information Systems Student  
Location: Brgy. Hawaiian, Silay City  
""")

# Applications Section
st.markdown("""
##### Applications

* Prediction
* Sentiment Analysis
* Image Classification
""")

# Horizontal lines for separation
st.markdown("""
<hr>
""", unsafe_allow_html=True)

st.markdown("""
<hr>
""", unsafe_allow_html=True)

# Hide Streamlit style
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# Apply the custom CSS to hide the menu and footer
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
