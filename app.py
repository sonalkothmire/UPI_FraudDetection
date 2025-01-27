# import necessary library


import numpy as np 
import pandas as pd 
import pickle as pkl 
import streamlit as st 

model = pkl.load(open('UPIfraud.pkl','rb'))
scaler = pkl.load(open('scaler.pkl','rb'))
st.header('UPI Fraud Detection App')

type = st.selectbox('choose type',['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
amount = st.slider("Amount in $",min_value=0, max_value=110000)
bal_before_transaction = st.slider("Sender Balance Before Transaction was made",min_value=0, max_value=110000)
bal_after_transaction = st.slider("Sender Balance After Transaction was made",min_value=0, max_value=110000)
bal_of_recepient_before_transaction = st.slider("Recipient Balance Before Transaction was made",min_value=0, max_value=110000)
bal_of_receipient_after_transaction =  st.slider("Recipient Balance After Transaction was made",min_value=0, max_value=110000)

if type == 'PAYMENT':
    type = 0
if type =='TRANSFER':
    type = 1
if type =='CASH_OUT':
    type = 2
if type =='CASH_IN':
    type = 3
else :
    type = 4

if st.button('predict'):

    pred_data = (type,amount,bal_before_transaction,bal_after_transaction,bal_of_recepient_before_transaction,bal_of_receipient_after_transaction) 
    pred_data = np.asarray(pred_data)
    pred_data = pred_data.reshape(1,-1)   
    pred_data = scaler.transform(pred_data)
    predict =model.predict(pred_data)
    if (pred_data == 0).any():
        st.markdown("No fraud detected for any transaction.")
    else:
        st.markdown("fraudulent transaction detected!")

    
