import math
import streamlit as st
import plotly.graph_objects as go
import numpy as np


def cal_circle_area (r):
    return math.pi*pow(r,2)

def plot_circle(radius):
    # Create circle points
    theta = np.linspace(0, 2*np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Create figure
    fig = go.Figure()
    
    # Add circle
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Circle',line=dict(color='blue', width=2)))
    
    # Add center point
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', name='Center',marker=dict(color='red', size=10)))
    
    # Add radius line
    fig.add_trace(go.Scatter(x=[0, radius], y=[0, 0], mode='lines', name='Radius',line=dict(color='red', width=2, dash='dash')))
    
    # Update layout
    fig.update_layout(
        title='Circle Visualization',
        xaxis_title='X axis',
        yaxis_title='Y axis',
        xaxis=dict(scaleanchor="y", scaleratio=1),
        showlegend=True,
        width=400,
        height=400
    )
    return fig

# st.title("Shape calculator")
# st.header("This is the calculator app.")

# st.write("Circle area calculation")

# radius = st.number_input("Please enter circle radius :")
# submit = st.button("Calculate", icon="😃") 
# if submit:
#     circle = cal_circle_area(float(radius))
#     st.write(f"The area of circle is {round(circle,2)}")

st.title("📏 Shape Calculator")
st.header("Circle Area Calculator")


radius = st.number_input(
    "Enter circle radius:",
    min_value=0.0,
    value=1.0,
    step=0.1,
    help="Please enter a positive number"
)

submit = st.button("Calculate Area 🔄")

if submit:
    try:
        circle_area = cal_circle_area(float(radius))
        st.success(f"The area of the circle is: {round(circle_area, 2)} square units")
        
        # Display the formula used
        st.info(f"""
        **Formula used:**
        - Area = π × r²
        - Area = {round(math.pi, 4)} × {radius}²
        """)
    except ValueError as e:
        st.error(str(e))

fig = plot_circle(radius)
st.plotly_chart(fig)


