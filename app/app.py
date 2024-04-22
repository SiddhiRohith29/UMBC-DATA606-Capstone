import streamlit as st
import pickle
import numpy as np
from io import BytesIO
import requests

def load_model():
    # Ensure the link points directly to the raw content on GitHub
    url = 'https://github.com/SiddhiRohith29/UMBC-DATA606-Capstone/blob/main/app/best_model1.pkl'

    # Send a GET request to the GitHub URL
    response = requests.get(url)
    
    # Make sure the request is successful
    if response.status_code == 200:
        model_file = BytesIO(response.content)
        data = pickle.load(model_file)
        return data
    else:
        print("Failed to retrieve the model file. Status code:", response.status_code)
        return None

data = load_model()
regressor = data["model"]

def show_predict_page():
    
    st.title("Airline Satisfaction System")
    st.write("""### We need ratings of services to predict the satisfaction""")

    # Collect inputs as strings
    user_input_cleanliness = st.text_input("Rate Cleanliness (1-5)", key="input_cleanrate")
    user_input_foodanddrink = st.text_input("Rate Food and Drink (1-5)", key="input_fooddrinkrate")
    user_input_onlineboarding = st.text_input("Rate Online Boarding (1-5)", key="input_onlineboardrate")
    user_input_wifiservice = st.text_input("Rate In-flight Wifi Service (1-5)", key="input_wifiservice")
    user_input_seatcomfort = st.text_input("Rate Seat Comfort (1-5)", key="input_seatcomfort")

    ok = st.button("Predict Satisfaction")
    if ok:
        try:
            # Convert inputs to Integer
            X = np.array([[int(user_input_cleanliness), int(user_input_foodanddrink), int(user_input_onlineboarding),
                           int(user_input_wifiservice), int(user_input_seatcomfort)]])
            
            # Predict
            Identified = regressor.predict(X)
            st.subheader(f"Service is {'Satisfied' if Identified[0] else 'Neutral or Dissatisfied'}")
        except ValueError as e:
            st.error("Please enter valid inputs. Error: " + str(e))
            

show_predict_page()