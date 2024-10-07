import streamlit as st
import pickle
import pandas as pd

# Load model
model_path = r'D:\Capstone Project-Daksh\random_forest_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Create Streamlit app
st.title("Product Delivery Prediction")

# Input fields for additional features
warehouse_block = st.selectbox("Warehouse Block", ["A", "B", "C", "D", "F"])
mode_of_shipment = st.selectbox("Mode of Shipment", ["Ship", "Flight", "Road"])
customer_rating = st.slider("Customer Rating", min_value=1, max_value=5, value=3)
cost_of_the_product = st.number_input("Cost of the Product", min_value=1, max_value=10000, value=500)
prior_purchases = st.number_input("Number of Prior Purchases", min_value=0, max_value=100, value=5)
discount_offered = st.number_input("Discount Offered (%)", min_value=0, max_value=100, value=10)
weight_in_gms = st.number_input("Weight of the Product (in grams)", min_value=1, max_value=10000, value=500)

# Encoding categorical features
warehouse_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
mode_of_shipment_mapping = {'Ship': 0, 'Flight': 1, 'Road': 2}
warehouse_encoded = warehouse_mapping[warehouse_block]
mode_of_shipment_encoded = mode_of_shipment_mapping[mode_of_shipment]

# Create input data
input_data = pd.DataFrame({
    'Warehouse_block': [warehouse_encoded],
    'Mode_of_Shipment': [mode_of_shipment_encoded],
    'Customer_rating': [customer_rating],
    'Cost_of_the_Product': [cost_of_the_product],
    'Prior_purchases': [prior_purchases],
    'Discount_offered': [discount_offered],
    'Weight_in_gms': [weight_in_gms]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("The product will be delivered on time.")
    else:
        st.warning("The product delivery will be delayed.")
