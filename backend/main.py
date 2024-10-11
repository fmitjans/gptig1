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

def get_details(offer_code, usar_firefox=True):
    url = f"https://www.bne.cl/oferta/{offer_code}"
    driver = init_driver(usar_firefox)    
    driver.get(url)

    data = dict()
    panels          = driver.find_elements(By.CLASS_NAME, 'panel-body')
    contact         = panels[1].find_elements(By.CLASS_NAME, 'col-sm-12')
    description     = panels[2].find_element(By.CLASS_NAME, 'col-sm-12')
    others          = panels[2].find_elements(By.CLASS_NAME, 'col-sm-3')
    level           = panels[3].find_element(By.CLASS_NAME, 'col-sm-8')
    experience      = panels[3].find_element(By.CLASS_NAME, 'col-sm-4')
    characteristics = panels[4].find_elements(By.CLASS_NAME, 'col-sm-6')

    data['empresa']     = contact[0].get_attribute('textContent').strip()
    data['actividad']   = contact[1].get_attribute('textContent').strip()
    data['descripcion'] = description.get_attribute('textContent').strip()
    data['ubicacion']   = others[0].get_attribute('textContent').strip()
    data['remuneracion']= others[1].get_attribute('textContent').strip()
    data['jornada']     = others[2].get_attribute('textContent').strip()
    data['nivel']       = level.get_attribute('textContent').strip()
    data['experiencia'] = experience.get_attribute('textContent').strip()
    data['contrato']    = characteristics[0].get_attribute('textContent').strip()
    data['cargo']       = characteristics[1].get_attribute('textContent').strip()
    data['origen']      = characteristics[2].get_attribute('textContent').strip()
    data['practica']    = characteristics[3].get_attribute('textContent').strip()
    driver.close()
    return data

if __name__ == '__main__':
    codigo = '2024-090575'
    data = get_details(codigo, False)
    for i in data.items():
        print(i)
    input()