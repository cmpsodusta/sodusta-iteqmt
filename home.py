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
As you navigate through my Streamlit app, you'll find that it's designed to showcase three key capabilities: prediction, sentiment analysis, and image classification. On the main page, you'll learn a bit about me and my background in machine learning, as well as a brief overview of the apps I've built.

The web interface is where the magic happens. Using Streamlit, users can interact with the models directly. For prediction, users can upload their own data and receive predictions based on the trained model. For sentiment analysis, users can input text and receive sentiment analysis results. For image classification, users can upload images and receive classification results.

To ensure the accuracy and efficiency of the models, I've pre-trained them using a variety of techniques. The pre-trained models are stored in pickle files, making it easy to load and use them within the app. For those interested in the technical details, I've also included the source code for training the models and the pre-trained models themselves.

My Streamlit app is designed to provide a comprehensive and interactive experience for users, showcasing the capabilities of machine learning in a user-friendly and accessible way.
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
