###########
#Librerias#
###########
import pip
pip.main(["install", "openpyxl"])
pip.main(["install", "pandas"])

import pandas as pd
import pydeck as pdk
import streamlit as st
import numpy as np 

#####################
#logo de la cayetano#
#####################
st.image("https://www.cayetano.edu.pe/cayetano/images/2017/SETIEMBRE/logo-OFICIAL.png")

########
#Titulo#
########
st.subheader("Tema:")
st.title("SUNEDU - Licenciamiento Institucional")
st.image("http://www.sunedu.gob.pe/sunedu/public/images/logo-sunedu.png")
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

##########
#Contexto#
##########
st.subheader("Concepto del tema:")
st.write("""En este proyecto presentaremos avances y el estatus actual del licenciamiento de Universidades a nivel nacional, 
         este proyecto se dividirá en regiones y en el tipo de identidad lo cual nos dará una mayor perspectiva nacional de 
         lo que está sucediendo hoy en día con este tema tan polarizado políticamente.
""")
st.write("-----------------------------")


###########################
#Lectura De Datos En Excel#
###########################
st.header("LICENCIA INSTITUCIONAL:")

st.write("""Una licencia institucional es un procedimiento obligatorio para todas las universidades , 
creado por la SUNEDU, para ver si cumplen con la CBC (condiciones basicas de Calidad)""")


video1=open("videoplayback.mp4","rb")
st.video(video1)

st.write("""Fuente:https://youtu.be/2NlkqlD7RTE""")

st.write("""A continuacion, le mostraremos la tabla con los datos de todas las universidades del Perú""")

columnas=["CODIGO_ENTIDAD",
          "NOMBRE",
          "TIPO_GESTION",
          "ESTADO_LICENCIAMIENTO",
          "FECHA_INICIO_LICENCIAMIENTO",
          "FECHA_FIN_LICENCIAMIENTO",
          "PERIODO_LICENCIAMIENTO",
          "DEPARTAMENTO",
          "PROVINCIA",
          "DISTRITO",
          "UBIGEO",
          "LATITUD",
          "LONGITUD",
          "FECHA_CORTE"]

L_Insti = pd.read_excel(r'https://github.com/Alexandeeer1/grupo6_program_avanzada/raw/main/Licenciamiento%20Institucional_7.xlsx', header=1, names=columnas)
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(L_Insti)

st.write("-----------------------------")

opcion = st.selectbox(
    'Eliga algún departamento del Perú en el botón de abajo',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', opcion)

variables=pd.Dataframe(
  "Cantidad":[91,50]
  "Licencia":["Otorgadas","No otorgadas"]
   )
bar_chart = alt.chart(variables).mark_bar().encode(
            y="Cantidad"
            x="Licencia"
)
st.altair_chart(bar_chart, use_container_width=True)

           

st.write("-----------------------------")

st.bar_chart(L_Insti, use_container_width=True)




