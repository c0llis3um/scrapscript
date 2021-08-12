from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



#Busca Chrome y abre website maps.google.com
driver = webdriver.Chrome('/Users/jalcantara/Desktop/chromedriver_win32/chromedriver')
driver.get("https://maps.google.com")


#Encontramos el ID y buscamos Dentista en Guadalajara

inputElement = driver.find_element_by_id("searchboxinput")
inputElement.send_keys('Comida Zapopan')

buttonElement = driver.find_element_by_id("searchbox-searchbutton").click()



