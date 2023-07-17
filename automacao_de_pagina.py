    #app_action___
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('detach',  True)
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get('https://www.leroymerlin.com.br/cabo-flexivel--2,5mm-100m-azul-750v-sil-fios_86839655?region=grande_sao_paulo&gclid=Cj0KCQjwqs6lBhCxARIsAG8YcDg4dSM8YHKB-LF0oE1BZywtdolPN3InXMX6fZZ_77ChGTrNF7EUqP4aAjPOEALw_wcB')

navegador.find_element('xpath', '/html/body/div[6]/div[2]/header/div[2]/div[1]/div/div[1]/form/div/input').send_keys('teste')