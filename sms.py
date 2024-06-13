from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Configuración de opciones del navegador
options = Options()
options.headless = False  # Cambiar a True si quieres que se ejecute en modo headless

# Inicializar el controlador de Firefox
driver = webdriver.Firefox(options=options)

# Abrir el sitio web de Messages
driver.get('https://messages.google.com/web/')

# Lista de números de destino
numeros_destino = ["5493794929464","5493442533465"]

# Función para enviar un mensaje a un número específico
def enviar_mensaje(numero):

    # Crear una instancia de WebDriverWait
    wait = WebDriverWait(driver, 20)

    # Hacer clic en el botón "Iniciar chat"
    start_chat_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a/span[2]/div/div')))
    start_chat_button.click()

    # Esperar a que aparezca el campo para ingresar el número de teléfono
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/div/input')))

    # Ingresar el número de teléfono en el campo correspondiente
    phone_number_input = driver.find_element(By.XPATH, '/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/div/input')
    phone_number_input.send_keys(numero_destino)

    print("hasta acá llega")
    # Enviar el número de teléfono presionando la tecla Enter
    phone_number_input.send_keys(Keys.ENTER)

    numerotel = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-contact-selector-button/button/span[2]/span/span/span')))
    numerotel.click()
    time.sleep(10)
    # Localizar el campo de entrada de texto para el mensaje
    input_element = driver.find_element(By.XPATH, '/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-autosize-textarea/textarea')

    # Ingresar el mensaje en el campo de texto
    input_element.send_keys('Hola. Te ofezco servicios de envios masivos de sms y emails. Por cualquier duda llamame a este celular.')

    # Enviar el mensaje presionando la tecla Enter
    input_element.send_keys(Keys.ENTER)
    print("mensaje enviado")

# Iterar sobre los números de destino y enviar mensajes
for numero_destino in numeros_destino:
    enviar_mensaje(numero_destino)
    time.sleep(5)

# Cerrar el navegador
#driver.quit()
#/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/div/mw-new-conversation-sub-header/div/div[2]/button/span[2]