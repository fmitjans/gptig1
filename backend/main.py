from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

import os
from dotenv import load_dotenv

import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def init_driver(usar_firefox=True):
    if usar_firefox:
        service = Service("/snap/bin/firefox.geckodriver")
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Chrome()
    
    return driver

def get_offers(keyword):
    url = f'https://www.bne.cl/ofertas?mostrar=empleo&textoLibre={keyword}&numPaginasTotal=479&numResultadosPorPagina=10&numResultadosTotal=4785&clasificarYPaginar=true&totalOfertasActivas=4785'

    driver = init_driver()
        
    driver.get(url)

    # Definir diccionarios para guardar resultados
    resultados = [dict() for i in range(5)]
    # Campos para scrapping
    tag_off = "row.margenVerticales.resultadoOfertas.noMargingLaterales.seccionOferta"
    offers = driver.find_elements(By.CLASS_NAME, tag_off)
    tags = ["datosEmpresaOferta", "tituloOferta", "descripcionOferta", "fechaOferta"]
    
    n_offers = min(len(offers), 5)
    resultados = [dict() for i in range(n_offers)]
    for i in range(n_offers):
        resultados[i]["index"] = i
        for tag in tags:
            # Encontrar elementos con la clase tag
            element = offers[i].find_element(By.CLASS_NAME, tag)
            text = element.get_attribute('textContent').strip()
            # Texto de BNE viene con espacios en blanco
            resultados[i][tag] = text.split("     ")[0].strip()
            if (tag == "tituloOferta"):
                link = element.find_element(By.TAG_NAME, "a") #get_attribute('href')
                resultados[i]['link'] = link.get_attribute('href')
            elif (tag == "datosEmpresaOferta"):
                resultados[i]['ubicacionOferta'] = text.split("     ")[-1].strip()


    resultados_json_str = json.dumps(resultados, indent=2, ensure_ascii= False)
    print(resultados_json_str)

    driver.close()

    return resultados_json_str

def get_details(offer_code, usar_firefox=True):
    url = f"https://www.bne.cl/oferta/{offer_code}"
    driver = init_driver(usar_firefox)    
    driver.get(url)

    data = dict()
    titulo      = driver.find_element(By.ID, 'nombreOferta')
    panels      = driver.find_elements(By.CLASS_NAME, 'panel-body')
    contact     = panels[1].find_elements(By.CLASS_NAME, 'col-sm-12')
    description = panels[2].find_element(By.CLASS_NAME, 'col-sm-12')
    specs       = panels[2].find_elements(By.CLASS_NAME, 'col-sm-3')
    level       = panels[3].find_element(By.CLASS_NAME, 'col-sm-8')
    experience  = panels[3].find_element(By.CLASS_NAME, 'col-sm-4')
    others      = panels[4].find_elements(By.CLASS_NAME, 'col-sm-6')

    long_title      = titulo.get_attribute('textContent').strip()
    data['titulo']  = ' '.join(long_title.split()[:7])
    data['empresa']     = contact[0].get_attribute('textContent').split(sep=':')[-1].strip()
    data['actividad']   = contact[1].get_attribute('textContent').split(sep=':')[-1].strip()
    data['descripcion'] = description.get_attribute('textContent').strip()
    data['ubicacion']   = specs[0].get_attribute('textContent').strip()
    data['remuneracion']= specs[1].get_attribute('textContent').strip()
    data['jornada']     = specs[2].get_attribute('textContent').strip()
    data['nivel']       = level.get_attribute('textContent').split(sep=':')[-1].strip()
    data['experiencia'] = experience.get_attribute('textContent').split(sep=':')[-1].strip()
    data['contrato']    = others[0].get_attribute('textContent').split(sep=':')[-1].strip()
    data['cargo']       = others[1].get_attribute('textContent').split(sep=':')[-1].strip()
    data['origen']      = others[2].get_attribute('textContent').split(sep=':')[-1].strip()
    data['practica']    = others[3].get_attribute('textContent').split(sep=':')[-1].strip()

    driver.close()
    return data


def generar_correo_openai(oferta):
    prompt = f"""
    Genera un correo formal para postularme a la siguiente oferta de trabajo:

    - Empresa: {oferta['empresa']}
    - Título del puesto: {oferta['titulo']}
    - Descripción del puesto: {oferta['descripcion']}

    Mi nombre es [mi nombre] y tengo experiencia relevante en este sector. Me gustaría expresar mi interés por el puesto y discutir cómo puedo contribuir a la empresa.

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



if __name__ == '__main__':
    codigo = '2024-083180'
    data = get_details(codigo, False)
    print(data)
    #for i in data.items():
    #    print(i)