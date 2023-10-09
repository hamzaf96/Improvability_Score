import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

print("we are here !")
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
