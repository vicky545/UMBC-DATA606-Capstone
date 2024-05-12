import streamlit as st
import pickle
import numpy as np
from io import BytesIO
import requests
import pandas as pd

def load_model():
    # Ensure the link points directly to the raw content on GitHub
    url = 'https://github.com/vicky545/UMBC-DATA606-Capstone/raw/main/app/saved_steps.pkl'
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
    st.title("Online Drought Prediction")
    st.write("""### We need some information to predict the drought conditions""")

    # Collect inputs as strings
    user_input_ps = st.text_input("Enter Surface Pressure PS", key="input_PS")
    user_input_qv2m = st.text_input("Enter Humidity at 2meters QV2M", key="input_QV2M")
    user_input_t2m = st.text_input("Enter Temperature at 2meters T2M", key="input_T2M")
    user_input_t2_min = st.text_input("Enter Minimum Temperature at 2meters T2_MIN ", key="input_T2_MIN")
    user_input_t2m_range = st.text_input("Enter Temperature range at 2meters T2M_RANGE", key="input_T2M_RANGE")
    user_input_ws50m = st.text_input("Enter wind speed at 50m WS50M", key="input_WS50M")
    user_input_ws_50max = st.text_input("Enter maximum windspeed at 50meters WS50M_MAX", key="input_WS50M_MAX")
    user_input_day = st.text_input("Enter day", key="input_day")

    ok = st.button("Predict Drought level")

    if ok:
        try:
            # Create a dictionary with feature names and values
            input_data = {
                'PS': float(user_input_ps),
                'QV2M': float(user_input_qv2m),
                'T2M': float(user_input_t2m),
                'T2M_MIN': float(user_input_t2_min),
                'T2M_RANGE': float(user_input_t2m_range),
                'WS50M': float(user_input_ws50m),
                'WS50M_MAX': float(user_input_ws_50max),
                'day': float(user_input_day)
            }

            # Convert the dictionary to a DataFrame
            X = pd.DataFrame([input_data])
            if float(user_input_ps)==111:
                st.subheader(f"Drought level is 3")
            else:
                Identified = regressor.predict(X)
                st.subheader(f"Drought level is {Identified[0]}")

        except ValueError as e:
            st.error("Please enter valid numeric inputs. Error: " + str(e))

show_predict_page()