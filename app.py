#Cargar librerias
import pandas as pd
import numpy as np

import plotly.express as px

import streamlit as st

#Cargar datos
car_data= pd.read_csv('vehicles_us.csv')

st.header('Relación de variables', divider= 'gray')

hist_button = st.button('Construir un histograma')

if hist_button:
    st.write ('Creación de un histograma para el conjunto de datos de anuncios de ventas de coches ')

    fig = px.histogram(car_data, x = "odometer")

    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir un Gráfico de Dispersión')

if disp_button:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de coches')

    fig = px.scatter(car_data, x= 'model_year', y ='odometer')

    st.plotly_chart(fig, use_container_width=False)

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: 
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x = "odometer")

    st.plotly_chart(fig, use_container_width=True)

build_disp = st.checkbox('Construir un gráfico de dispersión')

if build_disp:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de coches')

    fig = px.scatter(car_data, x= 'model_year', y ='price')

    st.plotly_chart(fig, use_container_width=False)

