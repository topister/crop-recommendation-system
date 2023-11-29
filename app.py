import streamlit as st
import pandas as pd
import joblib
import os

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
# Load the trained model
model = joblib.load('saved_model.pkl')

# Function to get predictions based on user input
def get_prediction(N, P, K, temperature, humidity, ph, rainfall):
    try:
        # Make predictions
        user_input = [float(N), float(P), float(K), float(temperature), float(humidity), float(ph), float(rainfall)]
        prediction = model.predict([user_input])[0]
        
        return prediction

    except ValueError:
        return "Error: Please enter valid numeric values!"

# Create a Streamlit web app
def main():
    # Set title and description
    st.title('Crop Recommendation System')
    st.write('Welcome to my app')
    st.write('Enter the values for the parameters below to know which crop to grow:')

    # Input fields for user to enter values
    N = st.number_input("N")
    P = st.number_input("P")
    K = st.number_input("K")
    temperature = st.number_input("Temperature")
    humidity = st.number_input("Humidity")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall")

    # Predict when 'Predict' button is clicked
    if st.button('Predict'):
        result = get_prediction(N, P, K, temperature, humidity, ph, rainfall)
        st.write(f'The predicted crop is: {result}')

# Run the app
if __name__ == "__main__":
    main()
