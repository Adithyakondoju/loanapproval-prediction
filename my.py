import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Predcition App')