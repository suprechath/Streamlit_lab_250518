import streamlit as st
import pandas as pd
import numpy as np

# Define the pages
profile = st.Page("pages/profile.py", title="Index", icon="👋") 
page_2 = st.Page("pages/cir.py", title="Circle", icon="❄️")
page_3 = st.Page("pages/rec.py", title="Rectangular", icon="🎉")
page_4 = st.Page("pages/chat.py", title="Chatbot", icon= "🤖")
page_5 = st.Page("pages/Bangkok.py", title="Bangkok", icon= "🌍")



# Set up navigation
pg = st.navigation([profile, page_2, page_3, page_4, page_5])

# Run the selected page
pg.run()
    
st.sidebar.title(f"**👋 Hello :rainbow[{st.session_state.profile_data['name']}]**")
st.sidebar.image(st.session_state.profile_picture, caption="Profile Picture")
