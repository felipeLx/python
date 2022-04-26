from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

service = Service(r'/home/felipelx/Downloads/geckodriver')
binary = FirefoxBinary('/usr/bin/firefox')
boot = Firefox(service=service,firefox_binary=binary)
boot.get('https://web.whatsapp.com/')

chatname = input('Greenlera')
chatmsg = input('Mensagem')
noCount = int(input('Quantidade de mensagens'))
input('Pressione enter para continuar')
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(chatname))