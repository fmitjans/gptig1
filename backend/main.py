from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

url = 'https://www.bne.cl/ofertas?mostrar=empleo&textoLibre=software&numPaginasTotal=479&numResultadosPorPagina=10&numResultadosTotal=4785&clasificarYPaginar=true&totalOfertasActivas=4785'


usar_firefox = True
if usar_firefox:
    service = Service("/snap/bin/firefox.geckodriver")
    driver = webdriver.Firefox(service=service)
else:
    driver = webdriver.Chrome()
    
driver.get(url)

resultados = [None for i in range(5)]


tags = ["datosEmpresaOferta", "tituloOferta", "descripcionOferta"]
for tag in tags:
    elements = driver.find_elements(By.CLASS_NAME, tag)
    for i in range(5):
        if i < len(elements):
            element = elements[i]
            text = element.get_attribute('textContent').strip()
            text = text.split("     ")[0].strip()
            if resultados[i] == None:
                resultados[i] = {}
            resultados[i][tag] = text

print(resultados)

driver.close()