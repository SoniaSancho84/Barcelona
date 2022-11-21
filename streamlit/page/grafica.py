import streamlit as st
from data.get_data import desempleo_anual, desempleo_genero, desempleo_por_distrito
import plotly.express as px

def graficas():
    columna = st.selectbox('Seleccione el grafico que desea mostrar', ["Desempleo Total por año", "Desempleo por genero en todos los años", "Desempleo por Distrito"])
    if columna == "Desempleo Total por año":
        info = desempleo_anual()
        years = [year["_id"] for year in info]
        desempleototal = [desempleo["desempleo_total"] for desempleo in info]
        fig = px.pie(values = desempleototal, names = years, title = "Número total de desempleados por año")
        st.plotly_chart(fig)
    if columna == "Desempleo por genero en todos los años":
        info = desempleo_genero()
        gender = [Gender["_id"] for Gender in info]
        desempleo_por_genero = [desempleo["desempleo_total"] for desempleo in info]
        fig = px.pie(values = desempleo_por_genero, names = gender, title = "Desempleo por género total 2013-2017")
        st.plotly_chart(fig)
    if columna == "Desempleo por Distrito":
        info = desempleo_por_distrito()
        distritos = [dist["_id"] for dist in info]
        desempleo_por_dist = [desempleo["desempleo_total"] for desempleo in info]
        fig = px.pie(values = desempleo_por_dist, names = distritos, title = "Desempleo por Distrito total 2013-2017")
        st.plotly_chart(fig)



