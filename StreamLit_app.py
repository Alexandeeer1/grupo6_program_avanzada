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

################
#Titulo Y Video#
################
st.header("LICENCIA INSTITUCIONAL:")

st.write("""Una licencia institucional es un procedimiento obligatorio para todas las universidades , 
creado por la SUNEDU, para ver si cumplen con la CBC (condiciones basicas de Calidad)""")


video1=open("videoplayback.mp4","rb")
st.video(video1)

st.write("""Fuente:https://youtu.be/2NlkqlD7RTE""")

st.write("""A continuacion, le mostraremos la tabla con los datos de todas las universidades del Perú""")

###########################
#Lectura De Datos En Excel#
###########################
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

st.write("-----------------------------")

"""st.bar_chart(L_Insti, use_container_width=True)"""


df = pd.DataFrame(
 [37.76, -122.4],
 columns=['lat', 'lon'])
st.map(df)


L_Insti['Diameter'].plot.hist()
l_Insti


###########################################
#gerararquia de las univercidades #########
#particulares y acionales las principales #
###########################################
st.write("----------------------------------------------------------------------------------------------------------------")
st.write(""" El siguiente ranking contiene 58 universidades licenciadas calificadas
según su producción científica en el período de 1980 hasta 2020:""")

data = {'Ranking' : ['UPCH – Universidad Peruana Cayetano Heredia.', 
                     'PUCP – Pontificia Universidad Católica del Perú.',
                     'UNMSM – Universidad Nacional Mayor de San Marcos.',
                     'UNI – Universidad Nacional de Ingeniería.',
                     'UNALM – Universidad Nacional Agraria la Molina.',
                     'UNSAAC – Universidad Nacional San Antonio Abad del Cusco.',
                     'UPC – Universidad Peruana de Ciencias Aplicadas.',
                     'UNAP – Universidad Nacional de la Amazonía Peruana.',
                     'UNSA – Universidad Nacional de San Agustín de Arequipa.',
                     'UNITRU – Universidad Nacional de Trujillo.',
                     'USMP – Universidad de San Martín de Porres.',
                     'UDEP – Universidad de Piura.',
                     'UP – Universidad del Pacífico.',
                     'ULIMA – Universidad de Lima.',
                     'UTEC – Universidad de Ingeniería y Tecnología.',
                     'UNAP – Universidad Nacional del Altiplano de Puno.',
                     'USIL – Universidad San Ignacio de Loyola.',
                     'URP – Universidad Ricardo Palma.',
                     'UESAN – Universidad ESAN.',
                     'UPN – Universidad Privada del Norte.',
                     'UNFV – Universidad Nacional Federico Villarreal.',
                     'UCSM – Universidad Católica de Santa María.',
                     'UNC – Universidad Nacional de Cajamarca.',
                     'UCSP – Universidad Católica San Pablo.',
                     'UNP – Universidad Nacional de Piura.',
                     'Ucontinental – Universidad Continental.',
                     'UNSCH – Universidad Nacional de San Cristóbal de Huamanga.',
                     'UNAS – Universidad Nacional Agraria de la Selva.'],
                     #'UCH – Universidad de Ciencias y Humanidades.',
                     #'UPAO – Universidad Privada Antenor Orrego.',
                     #'UNJBG – Universidad Nacional Jorge Basadre Grohmann.',
                     #'UNAC – Universidad Nacional del Callao.',
                     #'UNTRM – Universidad Nacional Toribio Rodríguez de Mendoza de Amazonas.',
                     #'UNASAM – Universidad Nacional Santiago Antúnez de Mayolo.',
                     #'UNAMAD – Universidad Nacional Amazónica de Madre de Dios.',
                     #'UPEU – Universidad Peruana Unión.',
                     #'UNH – Universidad Nacional de Huancavelica.',
                     #'UNTUMBES – Universidad Nacional de Tumbes.',
                     #'UPSJB – Universidad Privada San Juan Bautista.',
                     #'UNE – Universidad la Cantuta.',
                     #'UCV – Universidad César Vallejo.',
                     #'UNAMBA – Universidad Nacional Micaela Bastidas de Apurímac.',
                     #'UCSS – Universidad Católica Sedes Sapientiae.',
                     #UAC – Universidad Andina del Cusco.',
                     #'UNHEVAL – Universidad Nacional Hermilio Valdizán.',
                     #'UARM – Universidad Antonio Ruiz Montoya.',
                     #'UNU – Universidad Nacional de Ucayali.',
                     #'<UWIENER – Universidad Norbert Wiener.',
                     #'USS – Universidad Señor de Sipán.',
                     #'UPT – Universidad Privada de Tacna.',
                     #'UTP – Universidad Tecnológica del Perú.',
                     #'UNTELS – Universidad Nacional Tecnológica de Lima Sur.',
                     #'ULASALLE – Universidad La Salle.',
                     #'Autónoma – Universidad Autónoma del Perú.',
                     #'UPLA – Universidad Peruana de los Andes.',
                     #'USAT – Universidad Católica Toribio de Mogrovejo.',
                     #'UMA – Universidad María Auxiliadora.']
        'top'   : [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28], #,29,30,31,32,33,34,35,36,37,38,29,40,41,42,43,44,45,46,47,
                  #48,49,50,51,52,53,54,55,56],
        'departamento' : ['LIMA', 'LIMA', 'LIMA', 'LIMA','LIMA','CUSCO','LIMA','AMAZONAS','AREQUIPA','TRUJILLO','LIMA',
                         'LIMA','LIMA', 'LIMA', 'LIMA','PUNO','LIMA', 'LIMA', 'LIMA', 'LIMA','LIMA','AREQUIPA','CAJAMARCA','AREQUIPA','PIURA',
                         'LIMA','AYACUCHO','MADRE DE DIOS']}
print(type(data))
df = pd.DataFrame(data)
df











