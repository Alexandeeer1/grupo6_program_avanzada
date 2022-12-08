#app.py, run with 'streamlit run app.py'

import pip
pip.main(["install", "openpyxl"])
pip.main(["install", "pandas"])
import plotly.figure_factory as ff
pip.main(["install", "matplotlib"])
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import scipy

df_bonilla = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Bonilla.xlsx', header= 0) 
df_miraflores= pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Ov.Miraflores.xlsx', header= 0) 
st.title("Monitoreo de calidad de aire QAIRA - [Municipalidad de Miraflores]")
st.header("Integrantes:")
st.write("- Stefany Tumpay Paredes")
st.write("- Jener Cesar Huincho Ramos")
st.write("- Gianina Berduzco Ancco")
st.write("- Teyzon Florida Serrepe")
st.write("- Alvaro Ivan Alarcon Guizado")
st.header("Contexto")
st.write("“Saber la calidad de aire que se respira en un determinado lugar es importante para los ciudadanos que habitan en ella”. Por ello, en esta página se presenta un análisis estadístico de contaminantes presente en la Municipalidad de Miraflores-Lima(Perú). La base de datos fue proporcionada por la municipalidad mencionada, de esta manera se escogió los datos de monitoreo del Complejo Deportivo Bonilla y Ovalo Miraflores, los datos de estos dos lugares de monitoreo corresponden al mes de septiembre del 2020. Esta presentación incluye: Gráfica de datos de los respectivos contaminantes en Bonilla y Ov.Miraflores, gráficas comparativas entre ambos lugares y por último comparaciones de sus Límites Máximos Permisibles.")

st.title("Análisis en Bonilla")
st.header("Tabla de datos:")
st.write(df_bonilla)
st.header("Histogramas de las concentraciones de contaminantes:")
for i in range(6,15):
    fig = px.histogram(df_bonilla, df_bonilla.columns[i])
    st.plotly_chart(fig, use_container_width=True)

st.title("Análisis en Ov. Miraflores")
st.header("Tabla de datos:")
st.write(df_miraflores)
st.header("Histogramas de las concentraciones de contaminantes:")
for i in range(6,15):
    fig = px.histogram(df_miraflores, df_miraflores.columns[i])
    st.plotly_chart(fig, use_container_width=True)

limites_maximos=[1200,150,200,50,150,45,250,70,3]
dictionary_names=dict()
for j in range(6,15):
    dictionary_names[df_bonilla.columns[j]]=df_bonilla.columns[j]+" Bonilla"
df_bonilla.rename(columns = dictionary_names, inplace=True)
df_miraflores.columns=(df_miraflores.columns+" Ov. Miraflores").values.tolist()


st.title("Comparaciones de los valores de contaminantes entre Bonilla y Ov. Miraflores")
st.header("Histogramas comparativos:")

for i in range(6,15):
    fig = ff.create_distplot(
         [df_bonilla.iloc[:, i].values.tolist(),df_miraflores.iloc[:, i].values.tolist()], [df_bonilla.columns[i],df_miraflores.columns[i]])
    st.plotly_chart(fig, use_container_width=True)
st.header("Gráficas comparativas de los Límites máximos permisibles:")

for i in range(6,15):
    df_concat=[]
    df_concat=pd.concat([df_bonilla.iloc[:, [5,i]], df_miraflores.iloc[:, i]], axis=1)
    fig = px.line(df_concat, x=df_concat.columns[0], y=df_concat.columns[1:],
              hover_data={df_concat.columns[0]: "|%B %d, %Y"},
              title=df_concat.columns[1]+" vs "+df_concat.columns[2])
    print(max(df_concat.iloc[:,1:].max(axis=0)))
    if max(df_concat.iloc[:,1:].max(axis=0)) > limites_maximos[i-6]:
        fig.add_hrect(y0=limites_maximos[i-6], y1=max(df_concat.iloc[:,1:].max(axis=0)), line_width=0, fillcolor="red", opacity=0.2)
    st.plotly_chart(fig, use_container_width=True)







