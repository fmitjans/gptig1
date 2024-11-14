from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

from selenium.webdriver.common.by import By


class Driver:
    def __init__(self):
        self.options = Options()
        self.driver = None

    def initialize_driver(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def load_page(self, page: str) -> None:
        self.driver.get(page)
        sleep(10)

    def click_element(self, by: str, xpath: str) -> None:
        sleep(10)
        element = self.driver.find_element(by=by, value=xpath)
        element.click()

    def write_element(self, by: str, xpath: str, content: str):
        sleep(10)
        self.driver.find_element(by=by, value=xpath).send_keys(content)

    def find_element(self, by: str, xpath: str) -> WebElement:
        return self.driver.find_element(by=by, value=xpath)
    
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(10)

    def close(self) -> None:
        self.driver.quit()
        self.driver = None


print("hello world")

if __name__ == '__main__':
    chrome = Driver()
    chrome.initialize_driver()
    chrome.load_page('https://www.bne.cl/ofertas')
    texto = input()
    chrome.write_element(By.ID, 'buscadorOfertas', texto)
    chrome.click_element(By.ID, 'botonBuscarOfertas')
    sleep(20)




