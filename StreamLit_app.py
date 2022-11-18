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

Licencia_Institucional=pd.read_excel(r'https://github.com/Alexandeeer1/grupo6_program_avanzada/raw/main/Licenciamiento-Institucional_7.xlsx', header= 0)
st.write(Licencia_Institucional)

Diccionario_Licencia=pd.read_excel(r'https://github.com/Alexandeeer1/grupo6_program_avanzada/raw/main/Licenciamiento%20Institucional%20-%20Diccionario_1.xlsx', header= 0)
st.write(Diccionario_Licencia)
