from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import qrcode
import pyzbar.pyzbar as pyzbar
import time
import os
import qrcode_terminal


class WhatsAppAPI:
    def __init__(self):
        self.session_path = "app/session_info"
        self.qr_code_path = "app/png/qr_code_login.png"
        self.driver = self.setup_driver()
        self.ensure_directories_exist()

    def setup_driver(self):
        firefox_options = webdriver.FirefoxOptions()
        if os.path.exists(self.session_path):
            firefox_options.add_argument(f"-profile {self.session_path}")
        firefox_options.add_argument("--width=800")
        firefox_options.add_argument("--height=600")
        service = Service(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=firefox_options)

    def ensure_directories_exist(self):
        os.makedirs(os.path.dirname(self.qr_code_path), exist_ok=True)

    def login_with_qr(self):
        self.driver.get("https://web.whatsapp.com/")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "canvas[aria-label='Scan me!']")
            )
        )
        qr_code_element = self.driver.find_element(
            By.CSS_SELECTOR, "canvas[aria-label='Scan me!']"
        )
        qr_code_element.screenshot(self.qr_code_path)
        print("Por favor, escaneie o QR Code abaixo:")
        self.display_qr_code(self.qr_code_path)
        input("Pressione Enter após escanear o QR Code.")

    def display_qr_code(self, path):
        data = self.decode_qr_code(path)
        if data:
            self.create_ascii_qr(data)
        else:
            print("QR Code não pôde ser decodificado.")

    def create_ascii_qr(self, data):
        qrcode_terminal.draw(data, version=1)

    def decode_qr_code(self, path_to_image):
        decoded_objects = pyzbar.decode(Image.open(path_to_image))
        if decoded_objects:
            return decoded_objects[0].data.decode()
        return None

    def send_message(self, recipient_name, message):
        if not self.validate_session():
            self.login_with_qr()
        search_box = self.driver.find_element(
            By.CSS_SELECTOR, '[title="Search or start new chat"]'
        )
        search_box.clear()
        search_box.send_keys(recipient_name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        message_box = self.driver.find_element(
            By.XPATH, '//div[@title="Type a message"]'
        )
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

    def validate_session(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "img[src*='whatsapp']")
            return True
        except:
            return False
