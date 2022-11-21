import streamlit as st
from page.busqueda import busqueda
from page.grafica import graficas


columna = st.sidebar.selectbox("Elegir página", ["Inicio", "Buscar Desempleo por filtrado", "Graficas"])

if columna == "Inicio":
    st.title("Desempleo en Barcelona 2013-2017")
    st.image("https://as01.epimg.net/diarioas/imagenes/2022/04/30/actualidad/1651323395_313362_1651323476_noticia_normal_recorte1.jpg")
if columna == "Buscar Desempleo por filtrado":
    busqueda()   

if columna == "Graficas":
    graficas()