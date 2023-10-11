# Use an official Python runtime as a parent image
FROM python:3.11.6

# Set the working directory in the container
WORKDIR /Improvability_Score

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "your_app.py"]
