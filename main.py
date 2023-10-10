from Improvability_Score.code.utils.vis import (
    vis_corr_map,
    vis_distribution_data,
    vis_scatter_data,
)
from Improvability_Score.code.src.improvability_score import ImrovabilityScore
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Set the title and description for your app
st.title("Simple Streamlit App")
st.write("This is a basic Streamlit app that displays a line chart.")

# Generate some random data for the line chart
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line chart using Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Line Chart")

# Display the chart in the Streamlit app
st.pyplot(fig)

# Add text or other components to your app
st.write("You can add more content here.")
