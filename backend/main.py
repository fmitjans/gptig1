from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv

import json

import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_offers(keyword):
    url = f'https://www.bne.cl/ofertas?mostrar=empleo&textoLibre={keyword}&numPaginasTotal=479&numResultadosPorPagina=10&numResultadosTotal=4785&clasificarYPaginar=true&totalOfertasActivas=4785'


    usar_firefox = True
    if usar_firefox:
        service = Service("/snap/bin/firefox.geckodriver")
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Chrome()
        
    driver.get(url)

    # Definir diccionarios para guardar resultados
    resultados = [dict() for i in range(5)]
    # Campos para scrapping
    tags = ["datosEmpresaOferta", "tituloOferta", "descripcionOferta"]
    for tag in tags:
        # Encontrar elementos con la clase tag
        elements = driver.find_elements(By.CLASS_NAME, tag)
    
        n_elements = min(len(elements), 5)
        for i in range(n_elements):
            text = elements[i].get_attribute('textContent').strip()
            # Texto de BNE viene con espacios en blanco
            text = text.split("     ")[0].strip()
            resultados[i][tag] = text

    resultados_json_str = json.dumps(resultados, indent=2, ensure_ascii= False)
    print(resultados_json_str)

    driver.close()

    return resultados_json_str






def generar_correo_openai(oferta):
    prompt = f"""
    Genera un correo formal para postularme a la siguiente oferta de trabajo:

    - Empresa: {oferta['datosEmpresaOferta']}
    - Título del puesto: {oferta['tituloOferta']}
    - Descripción del puesto: {oferta['descripcionOferta']}

    Mi nombre es Julián y tengo experiencia relevante en este sector. Me gustaría expresar mi interés por el puesto y discutir cómo puedo contribuir a la empresa.

    Por favor, utiliza un tono profesional y cortés.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente que genera correos formales."},
            {"role": "user", "content": prompt}
        ]
    )

    # Obtener el texto generado
    correo_generado = response['choices'][0]['message']['content'].strip()
    return correo_generado
