import numpy as np 
import pandas as pd 
import pickle as pkl 
import streamlit as st 

# Load model and scaler
model = pkl.load(open('UPIFraud.pkl', 'rb'))
sc = pkl.load(open('scaler.pkl', 'rb'))

st.title('🔍 UPI Fraud Detection App')

# Input form
step = st.slider('Step (Transaction Hour)', min_value=1, max_value=743)
PAYMENT = st.selectbox("Is Pyment", [0, 1])
CASH_IN = st.selectbox("Is Cash_In", [0, 1])
CASH_OUT = st.selectbox("Is Cash_Out", [0, 1])
TRANSFER = st.selectbox("Is Trasfer", [0, 1])
DEBIT = st.selectbox("Is Debit", [0, 1])
amount = st.slider("Amount ($)", min_value=0, max_value=110000)
bal_before_transaction = st.slider("Sender Balance Before Transaction", min_value=0, max_value=110000)
bal_after_transaction = st.slider("Sender Balance After Transaction", min_value=0, max_value=110000)
bal_recipient_before = st.slider("Recipient Balance Before Transaction", min_value=0, max_value=110000)
bal_recipient_after = st.slider("Recipient Balance After Transaction", min_value=0, max_value=110000)
is_flagged = st.selectbox("Is transaction flagged?", [0, 1])


# Predict button
if st.button('Predict Fraud'):
    # Prepare input array
    input_data = np.array([[
        step,
        PAYMENT,
        TRANSFER,
        CASH_IN,
        CASH_OUT,
        DEBIT,
        amount,
        bal_before_transaction,
        bal_after_transaction,
        bal_recipient_before,
        bal_recipient_after,
        is_flagged
    ]])

    # Scale data    
    input_scaled = sc.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Output
    if prediction[0] == 0:
        st.success("✅ No fraud detected for this transaction.")
    else:
        st.error("⚠️ Fraudulent transaction detected!")
