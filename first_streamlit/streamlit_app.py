import streamlit as st
import multipage_streamlit as mt
from pages import cir, hist, profile, rec

app = mt.MultiPage()
app.add("Profile", profile.run)
app.add("Circle calculation", cir.run)
app.add("Rectangular calculation", rec.run)
app.add("Histrogram", hist.run)

style = st.sidebar.radio("MultiPage style:", app.styles,
    help="Choose the style of the multipage app")

app.run(style)

# Define the pages
# main_page = st.Page("pages/profile.py", title="Main Page", icon="🎈")
# page_2 = st.Page("pages/1_cal_cir_250518.py", title="Circle", icon="❄️")
# page_3 = st.Page("pages/2_cal_regtang_250518.py", title="Rectangular", icon="🎉")
# histrogram = st.Page("pages/Histogram.py", title="Histrogram", icon="🎈")


# Set up navigation
pg = st.navigation([main_page, page_2, page_3,histrogram])

# Run the selected page
pg.run()
