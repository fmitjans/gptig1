from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

search_text = 'software'
url = f'https://www.bne.cl/ofertas?mostrar=empleo&textoLibre={search_text}&numPaginasTotal=479&numResultadosPorPagina=10&numResultadosTotal=4785&clasificarYPaginar=true&totalOfertasActivas=4785'


usar_firefox = False#True
if usar_firefox:
    service = Service("/snap/bin/firefox.geckodriver")
    driver = webdriver.Firefox(service=service)
else:
    driver = webdriver.Chrome()
    
driver.get(url)

resultados = [dict() for i in range(5)]
tags = ["datosEmpresaOferta", "tituloOferta", "descripcionOferta"]
for tag in tags:
    elements = driver.find_elements(By.CLASS_NAME, tag)
    n_elements = min(len(elements), 5)
    for i in range(n_elements):
        text = elements[i].get_attribute('textContent').strip()
        text = text.split("     ")[0].strip()
        resultados[i][tag] = text

resultados_json_str = json.dumps(resultados, indent=2, ensure_ascii= False)
print(resultados_json_str)

driver.close()