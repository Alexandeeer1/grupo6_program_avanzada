###########
#Librerias#
###########
import pandas as pd
import streamlit as st

########
#Titulo#
########
st.title("SUNEDU - Licenciamiento Institucional")
st.write("-----------------------------")

#############
#Integrantes#
#############
st.subheader("""Integrantes:
- Peñaloza Huaman, Bryan Alexander
- Rodriguez Reategui, Rodrigo Alonso
- Oviedo Chahua, Gilmar Rony 
- Castro Pichihua, Victoria Beatriz 
             """)
st.write("-----------------------------")

###########################
#Lectura De Datos En Excel#
###########################

Licencia_Institucional=pd.read_csv(r'https://www.datosabiertos.gob.pe/sites/default/files/Licenciamiento%20Institucional_7.csv', header= 0)
st.write(Licencia_Institucional)

