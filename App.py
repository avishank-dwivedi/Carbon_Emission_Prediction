import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('forecasting_co2_emmision.pkl', 'rb'))

st.set_page_config(
    page_title="Carbon Emission Prediction",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Carbon Emission Prediction")

st.write("Enter input values below")

cereal_yield = st.number_input("Cereal Yield")
fdi_perc_gdp = st.number_input("FDI % GDP")
en_per_gdp = st.number_input("Energy per GDP")
en_per_cap = st.number_input("Energy per Capita")
pop_urb_aggl_perc = st.number_input("Urban Agglomeration %")
prot_area_perc = st.number_input("Protected Area %")
gdp = st.number_input("GDP")

if st.button("Predict"):

    input_data = np.array([[
    cereal_yield,
    fdi_perc_gdp,
    en_per_gdp,
    en_per_cap,
    pop_urb_aggl_perc,
    prot_area_perc,
    gdp
]])

    prediction = model.predict(input_data)

    st.success(f"Predicted CO2 Emission: {prediction[0]}")