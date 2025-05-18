import math
import streamlit as st

def cal_circle_area (r):
    return math.pi*pow(r,2)

st.title("Shape calculator")
st.header("This is the calculator app.")

st.write("Circle area calculation")

radius = st.number_input("Please enter circle radius :")
submit = st.button("Calculate", icon="😃") 
if submit:
    circle = cal_circle_area(float(radius))
    st.write(f"The area of circle is {round(circle,2)}")


