import streamlit as st
from data.get_data import get_years, get_month, get_district, get_barrio, get_gender, get_desempleo, get_status

def busqueda():
    st.title("Búsquedad de Desempleo")
    op_year = st.selectbox("Elige el año en el que deseas buscar", get_years())
    op_month = st.selectbox("Elige el mes en el que deseas buscar", get_month())
    op_district = st.selectbox("Elige el distrito en el que deseas buscar", get_district())
    op_barrio = st.selectbox("Elige el barrio en el que deseas buscar", get_barrio(op_district))
    op_gender = st.selectbox("Elige el género en el que deseas buscar", get_gender())
    op_status = st.selectbox("Elige el estado de desempleo en el que deseas buscar", get_status())
    respuesta = get_desempleo(op_year, op_month, op_district, op_barrio, op_gender, op_status)
    if len(respuesta) > 0:
        st.subheader(f"con este filtrado se han detectado la siguiente cantidad de desempleados: {respuesta[0]['Number']}")
