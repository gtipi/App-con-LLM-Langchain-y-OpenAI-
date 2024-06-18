import langch_app as lch
import streamlit as stream

stream.title("GNE via LLM")
stream.write("Generador de nombres de empresa")

user_empresa = stream.sidebar.text_area(label="Qué tipo de empresa vas a crear?", max_chars=30) #la cantidad de caracates permitida impacta en el uso de la API de OpenAI, de manera que a más contenido, más costo

if user_empresa:
    response = lch.nombre_empresa(user_empresa)
    stream.text(response)