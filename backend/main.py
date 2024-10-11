from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

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

def get_details():
    pass

if __name__ == '__main__':
    texto = 'profesor'
    get_offers(texto, False)