import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the HTML and CSS styles
html_temp = """
<div style="background-color:#025246;padding:10px">
<h2 style="color:white;text-align:center;">Health Insurance Prediction</h2>
</div><br>"""

css_temp = """
<style>
body {
    background-color: #f5f5f5;
}
.container {
    padding: 20px;
    background-color: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.button {
    background-color: #025246;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
}
.button:hover {
    background-color: #013535;
}
</style>
"""

def predict_health_insurance(input_data):
    input_data_encoded = np.zeros((1, 10))
    input_data_encoded[0, 0] = 1 if input_data['Gender'] == 'Male' else 0
    input_data_encoded[0, 1] = float(input_data['Age'])
    input_data_encoded[0, 2] = int(input_data['Driving License'])
    vehicle_age_mapping = {'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2}
    input_data_encoded[0, 3] = vehicle_age_mapping[input_data['Vehicle Age']]
    input_data_encoded[0, 4] = 1 if input_data['Vehicle Damage'] == 'Yes' else 0
    input_data_encoded[0, 5] = float(input_data['Annual Premium'])
    input_data_encoded[0, 6] = int(input_data['Policy Sales Channel'])
    input_data_encoded[0, 7] = int(input_data['Region Code'])
    input_data_encoded[0, 8] = int(input_data['Vintage'])
    prediction = model.predict(input_data_encoded)
    probability = model.predict_proba(input_data_encoded)[:, 1]
    return prediction, probability



# Streamlit app
def main():
    # Set page configuration
    st.set_page_config(page_title='Health Insurance Prediction', layout='centered')
    st.markdown(css_temp, unsafe_allow_html=True)

    # Display header
    st.markdown(html_temp, unsafe_allow_html=True)

    # Create input form
    st.title("Health Insurance Prediction")
    st.markdown("Enter the required information to predict the likelihood of buying health insurance.")

    # Input fields
    gender = st.selectbox("Gender", ['Male', 'Female'])
    age = st.number_input("Age", min_value=18, max_value=100)
    driving_license = st.selectbox("Driving License", [0, 1])
    region_code = st.number_input("Region Code", min_value=0, max_value=53)
    previously_insured = st.selectbox("Previously Insured", [0, 1])
    vehicle_age = st.selectbox("Vehicle Age", ['< 1 Year', '1-2 Year', '> 2 Years'])
    vehicle_damage = st.selectbox("Vehicle Damage", ['Yes', 'No'])
    annual_premium = st.number_input("Annual Premium", min_value=0.0, max_value=1000000.0)
    policy_sales_channel = st.number_input("Policy Sales Channel", min_value=1, max_value=160)
    vintage = st.number_input("Vintage", min_value=1, max_value=500)

    # Create input data dictionary
    input_data = {
        'Gender': gender,
        'Age': age,
        'Driving License': driving_license,
        'Region Code': region_code,
        'Previously Insured': previously_insured,
        'Vehicle Age': vehicle_age,
        'Vehicle Damage': vehicle_damage,
        'Annual Premium': annual_premium,
        'Policy Sales Channel': policy_sales_channel,
        'Vintage': vintage
    }

    # Prediction button
    if st.button("Predict"):
        prediction, probability = predict_health_insurance(input_data)
        result = "Likely to buy insurance" if prediction[0] == 1 else "Unlikely to buy insurance"
        st.markdown(f"Prediction: **{result}**")
        st.markdown(f"Probability: {probability[0]:.2f}")

if __name__ == '__main__':
    main()
