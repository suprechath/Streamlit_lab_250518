import math
import streamlit as st

def cal_rectangular_area (w, h):
    return w*h

st.title("📐 Shape Calculator")
st.header("Rectangle Area Calculator")

col1, col2 = st.columns(2)

with col1:
    width = st.number_input(
        "Width:",
        min_value=0.1,
        value=1.0,
        step=0.1,
        help="Enter the width of the rectangle"
    )

with col2:
    height = st.number_input(
        "Height:",
        min_value=0.1,
        value=1.0,
        step=0.1,
        help="Enter the height of the rectangle"
    )

submit = st.button("Calculate Area", type="primary")

if submit:
    area = cal_rectangular_area(width, height)
    st.success(f"The area of the rectangle is **{round(area, 2)}** square units")
    
    # Visual representation
    st.markdown("### Visual Representation")
    aspect_ratio = width / height
    st.markdown(f"""
    <div style="
        border: 2px solid #4CAF50;
        width: 200px;
        height: {200/aspect_ratio}px;
        margin: 10px 0;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #e8f5e9;
        color: #000000;
        font-weight: bold;
    ">
    {round(width,3)} × {round(height,3)}
    </div>
    """, unsafe_allow_html=True)

