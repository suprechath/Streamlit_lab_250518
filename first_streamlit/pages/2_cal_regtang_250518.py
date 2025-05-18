import math
import streamlit as st

def cal_rectangular_area (w, h):
    return w*h

st.title("Shape calculator")
st.header("This is the calculator app.")

st.write("Rectangular area calculation")

width = st.number_input("Please enter rectangular width :")
height = st.number_input("Please enter rectangular height :")

submit2 = st.button("Calculate", type="primary")
if submit2:
    rectang = cal_rectangular_area(float(width),float(height))
    st.write(f"The area of rectangular is {round(rectang,2)}")


