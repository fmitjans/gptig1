from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

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