import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.write("🌍 จำนวนตึกสูงในกรุงเทพมหานคร")

chart_data = pd.DataFrame(
   np.random.randn(500, 2) / [50, 50] + [13.7563, 100.5018],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=13.7563,
        longitude=100.5018,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[500, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))