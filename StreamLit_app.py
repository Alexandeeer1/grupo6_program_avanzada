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
st.subheader("""A continuacion, le mostraremos la tabla con los datos de todas las universidades del Perú""")
st.write("-----------------------------")



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

unis=["UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS",
      "UNIVERSIDAD NACIONAL DE SAN CRISTÓBAL DE HUAMANGA",
      "UNIVERSIDAD NACIONAL DE TRUJILLO",
      "UNIVERSIDAD NACIONAL DE SAN AGUSTÍN DE AREQUIPA",
      "UNIVERSIDAD NACIONAL DE INGENIERÍA",
      "UNIVERSIDAD NACIONAL AGRARIA LA MOLINA",
      "PONTIFICIA UNIVERSIDAD CATÓLICA DEL PERÚ",
      "UNIVERSIDAD NACIONAL DE LA AMAZONÍA PERUANA",
      "UNIVERSIDAD NACIONAL DEL ALTIPLANO",
      "UNIVERSIDAD PERUANA CAYETANO HEREDIA",
      "UNIVERSIDAD CATÓLICA DE SANTA MARÍA",
      "UNIVERSIDAD NACIONAL DE CAJAMARCA",
      "UNIVERSIDAD DEL PACÍFICO",
      "UNIVERSIDAD DE LIMA",
      "UNIVERSIDAD DE SAN MARTÍN DE PORRES",
      "UNIVERSIDAD FEMENINA DEL SAGRADO CORAZÓN",
      "UNIVERSIDAD DE PIURA",
      "UNIVERSIDAD RICARDO PALMA",
      "UNIVERSIDAD NACIONAL JORGE BASADRE GROHMANN",
      "UNIVERSIDAD NACIONAL SANTIAGO ANTÚNEZ DE MAYOLO",
      "UNIVERSIDAD NACIONAL DE UCAYALI",
      "UNIVERSIDAD PERUANA UNIÓN",
      "UNIVERSIDAD ANDINA DEL CUSCO",
      "UNIVERSIDAD PRIVADA DE TACNA",
      "UNIVERSIDAD PRIVADA ANTENOR ORREGO",
      "UNIVERSIDAD MARCELINO CHAMPAGNAT",
      "UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS S.A.C.",
      "UNIVERSIDAD PRIVADA DEL NORTE S.A.C.",
      "UNIVERSIDAD SAN IGNACIO DE LOYOLA S.A.",
      "UNIVERSIDAD CATÓLICA SAN PABLO",
      "UNIVERSIDAD CIENTÍFICA DEL SUR S.A.C.",
      "UNIVERSIDAD CATÓLICA SANTO TORIBIO DE MOGROVEJO",
      "UNIVERSIDAD CATÓLICA SEDES SAPIENTIAE",
      "UNIVERSIDAD NACIONAL TORIBIO RODRÍGUEZ DE MENDOZA DE AMAZONAS",
      "UNIVERSIDAD ESAN",
      "UNIVERSIDAD ANTONIO RUIZ DE MONTOYA",
      "UNIVERSIDAD PARA EL DESARROLLO ANDINO",
      "UNIVERSIDAD NACIONAL INTERCULTURAL DE LA AMAZONÍA",
      "UNIVERSIDAD NACIONAL JOSÉ MARÍA ARGUEDAS",
      "UNIVERSIDAD NACIONAL DE MOQUEGUA",
      "UNIVERSIDAD AUTÓNOMA DEL PERÚ S.A.C.",
      "ASOCIACIÓN CIVIL UNIVERSIDAD DE CIENCIAS Y HUMANIDADES",
      "UNIVERSIDAD NACIONAL DE JULIACA",
      "UNIVERSIDAD JAIME BAUSATE Y MEZA",
      "UNIVERSIDAD NACIONAL DE JAÉN",
      "UNIVERSIDAD LE CORDON BLEU S.A.C.",
      "UNIVERSIDAD DE CIENCIAS Y ARTES DE AMÉRICA LATINA S.A.C.",
      "UNIVERSIDAD NACIONAL AUTÓNOMA DE CHOTA",
      "UNIVERSIDAD NACIONAL DE BARRANCA",
      "UNIVERSIDAD NACIONAL DE CAÑETE",
      "UNIVERSIDAD NACIONAL INTERCULTURAL FABIOLA SALAZAR LEGUÍA DE BAGUA",
      "UNIVERSIDAD NACIONAL INTERCULTURAL DE LA SELVA CENTRAL JUAN SANTOS ATAHUALPA",
      "UNIVERSIDAD NACIONAL AUTÓNOMA DE ALTO AMAZONAS",
      "UNIVERSIDAD NACIONAL AUTÓNOMA ALTOANDINA DE TARMA",
      "UNIVERSIDAD NACIONAL AUTÓNOMA DE HUANTA",
      "UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA",
      "UNIVERSIDAD LA SALLE",
      "UNIVERSIDAD MARÍA AUXILIADORA S.A.C.",
      "UNIVERSIDAD CONTINENTAL S.A.C.",
      "UNIVERSIDAD NACIONAL TECNOLÓGICA DE LIMA SUR",
      "UNIVERSIDAD NACIONAL TECNOLÓGICA DE SAN JUAN DE LURIGANCHO",
      "UNIVERSIDAD AUTÓNOMA MUNICIPAL DE LOS OLIVOS",
      "UNIVERSIDAD NACIONAL AUTÓNOMA DE TAYACAJA DANIEL HERNÁNDEZ MORILLO",
      "UNIVERSIDAD NACIONAL CIRO ALEGRÍA",
      "UNIVERSIDAD SEMINARIO EVANGÉLICO DE LIMA",
      "UNIVERSIDAD SEMINARIO BÍBLICO ANDINO",
      "UNIVERSIDAD NACIONAL DE SAN ANTONIO ABAD DEL CUSCO",
      "UNIVERSIDAD NACIONAL SAN LUIS GONZAGA DE ICA",
      "UNIVERSIDAD NACIONAL DEL CENTRO DEL PERÚ",
      "UNIVERSIDAD NACIONAL DE PIURA",
      "UNIVERSIDAD NACIONAL FEDERICO VILLARREAL",
      "UNIVERSIDAD NACIONAL AGRARIA DE LA SELVA",
      "UNIVERSIDAD NACIONAL HERMILIO VALDIZÁN DE HUÁNUCO",
      "UNIVERSIDAD INCA GARCILASO DE LA VEGA ASOCIACIÓN CIVIL",
      "UNIVERSIDAD NACIONAL DE EDUCACIÓN ENRIQUE GUZMÁN Y VALLE",
      "UNIVERSIDAD NACIONAL DANIEL ALCIDES CARRIÓN",
      "UNIVERSIDAD NACIONAL DEL CALLAO",
      "UNIVERSIDAD NACIONAL JOSÉ FAUSTINO SÁNCHEZ CARRIÓN",
      "UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO",
      "UNIVERSIDAD NACIONAL DE SAN MARTÍN",
      "UNIVERSIDAD ANDINA NÉSTOR CÁCERES VELÁSQUEZ",
      "UNIVERSIDAD PERUANA LOS ANDES",
      "UNIVERSIDAD TECNOLÓGICA DE LOS ANDES",
      "UNIVERSIDAD NACIONAL DE TUMBES",
      "UNIVERSIDAD NACIONAL DEL SANTA",
      "UNIVERSIDAD PARTICULAR DE CHICLAYO",
      "UNIVERSIDAD DE HUÁNUCO",
      "UNIVERSIDAD NACIONAL DE HUANCAVELICA",
      "UNIVERSIDAD CÉSAR VALLEJO S.A.C.",
      "UNIVERSIDAD ALAS PERUANAS S.A.",
      "UNIVERSIDAD PRIVADA NORBERT WIENER S.A.",
      "UNIVERSIDAD TECNOLÓGICA DEL PERÚ S.A.C.",
      "UNIVERSIDAD PRIVADA ANTONIO GUILLERMO URRELO S.A.C.",
      "UNIVERSIDAD SEÑOR DE SIPÁN S.A.C.",
      "UNIVERSIDAD NACIONAL AMAZÓNICA DE MADRE DE DIOS",
      "UNIVERSIDAD NACIONAL MICAELA BASTIDAS DE APURÍMAC",
      "UNIVERSIDAD PERUANA DE LAS AMÉRICAS S.A.C.",
      "UNIVERSIDAD PERUANA DE CIENCIAS E INFORMÁTICA S.A.C.",
      "UNIVERSIDAD PRIVADA TELESUP S.A.C.",
      "UNIVERSIDAD SAN PEDRO",
      "UNIVERSIDAD JOSÉ CARLOS MARIÁTEGUI",
      "UNIVERSIDAD CIENTÍFICA DEL PERÚ",
      "UNIVERSIDAD CATÓLICA LOS ÁNGELES DE CHIMBOTE",
      "UNIVERSIDAD PRIVADA SAN JUAN BAUTISTA S.A.C.",
      "UNIVERSIDAD CATÓLICA DE TRUJILLO BENEDICTO XVI",
      "UNIVERSIDAD PRIVADA SERGIO BERNALES S.A.",
      "UNIVERSIDAD PRIVADA DE PUCALLPA S.A.C.",
      "UNIVERSIDAD PRIVADA DE TRUJILLO",
      "UNIVERSIDAD PRIVADA SAN CARLOS S.A.C.",
      "UNIVERSIDAD PERUANA SIMÓN BOLÍVAR S.A.C.",
      "UNIVERSIDAD PERUANA DEL ORIENTE S.A.C.",
      "UNIVERSIDAD PRIVADA JUAN MEJÍA BACA S.A.C.",
      "UNIVERSIDAD PERUANA DEL CENTRO",
      "UNIVERSIDAD PRIVADA ARZOBISPO LOAYZA S.A.C.",
      "UNIVERSIDAD PRIVADA DE HUANCAYO FRANKLIN ROOSEVELT S.A.C.",
      "UNIVERSIDAD NACIONAL DE FRONTERA",
      "UNIVERSIDAD CIENCIAS DE LA SALUD S.A.C.",
      "UNIVERSIDAD DE AYACUCHO FEDERICO FROEBEL S.A.C.",
      "UNIVERSIDAD PERUANA AUSTRAL DEL CUSCO S.A.C.",
      "UNIVERSIDAD AUTÓNOMA SAN FRANCISCO S.A.C.",
      "UNIVERSIDAD SAN ANDRÉS S.A.C.",
      "UNIVERSIDAD INTERAMERICANA PARA EL DESARROLLO S.A.C.",
      "UNIVERSIDAD PRIVADA JUAN PABLO II S.A.C.",
      "UNIVERSIDAD PRIVADA LEONARDO DA VINCI S.A.C.",
      "UNIVERSIDAD NACIONAL INTERCULTURAL DE QUILLABAMBA",
      "UNIVERSIDAD LATINOAMERICANA CIMA S.A.C.",
      "UNIVERSIDAD PRIVADA AUTÓNOMA DEL SUR S.A.C.",
      "UNIVERSIDAD SANTO DOMINGO DE GUZMÁN S.A.C.",
      "UNIVERSIDAD PRIVADA LÍDER PERUANA S.A.C.",
      "UNIVERSIDAD PRIVADA PERUANO ALEMANA S.A.C.",
      "UNIVERSIDAD GLOBAL DEL CUSCO S.A.C.",
      "UNIVERSIDAD PERUANA SANTO TOMÁS DE AQUINO DE CIENCIA E INTEGRACIÓN S.A.C.",
      "UNIVERSIDAD PRIVADA SISE S.A.C.",
      "GRUPO EDUCATIVO UNIVERSIDAD PRIVADA DE ICA S.A.C.",
      "UNIVERSIDAD AUTÓNOMA DE ICA S.A.C.",
      "UNIVERSIDAD PRIVADA DE LA SELVA PERUANA S.A.C.",
      "UNIVERSIDAD POLITÉCNICA AMAZÓNICA S.A.C.",
      "UNIVERSIDAD PERUANA DE INTEGRACIÓN GLOBAL S.A.C.",
      "UNIVERSIDAD DE LAMBAYEQUE S.A.C.",
      "UNIVERSIDAD PERUANA DE ARTE ORVAL S.A.C.",
      "UNIVERSIDAD PERUANA DE INVESTIGACIÓN Y NEGOCIOS S.A.C.",
      "UNIVERSIDAD MARÍTIMA DEL PERÚ S.A.C.",
      "FACULTAD DE TEOLOGÍA PONTIFICIA Y CIVIL DE LIMA"]


L_Insti = pd.read_excel(r'https://github.com/Alexandeeer1/grupo6_program_avanzada/raw/main/Licenciamiento%20Institucional_7.xlsx', header=1, names=columnas)
st.checkbox("Cajas Expandidas", value=False, key="use_container_width")
st.dataframe(L_Insti)
st.write("-----------------------------")


opcion = st.selectbox(
    'Eliga algún departamento del Perú en el botón de abajo',
    ("Eliga su opcion: ",'Arequipa', 'Ayacucho ', 'Cajamarca ','Callao', 'Cusco ','Huancavelica', 'Huánuco ','Ica', 'Junín ','La Libertad', 'Lambayeque','Lima Metropolitana	', 'Lima (departamento)	 ','Loreto', ' Madre de Dios	','Moquegua', 'Pasco ','Piura', ' Puno','San Martín	', ' Tacna','Tumbes', ' Ucayali'))
st.write('You selected:', opcion)
st.write("-----------------------------")



st.bar_chart(L_Insti["TIPO_GESTION"], use_container_width=True)
st.write("-----------------------------")

st.bar_chart(L_Insti["ESTADO_LICENCIAMIENTO"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["FECHA_INICIO_LICENCIAMIENTO"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["FECHA_FIN_LICENCIAMIENTO"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["PERIODO_LICENCIAMIENTO"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["DEPARTAMENTO"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["PROVINCIA"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["DISTRITO"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["UBIGEO"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["LATITUD"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["LONGITUD"], use_container_width=True)
st.write("-----------------------------")

st.area_chart(L_Insti["FECHA_CORTE"], use_container_width=True)
st.write("-----------------------------")




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







