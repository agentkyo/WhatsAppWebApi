import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv, find_dotenv
from elements import WhatsAppXpathElements


load_dotenv(find_dotenv())

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class WhatsApp:
    def __init__(self):
        self.qr_code_path = "app/png/qr_code_login.png"
        self.profile_directory = self.get_profile_directory()
        self.edge_options = self.setup_edge_options()
        self.driver = self.setup_driver()
        self.ensure_directories_exist()
        self.login_with_qr()

    def get_edgedriver_patch(self):
        path = os.getenv("PATH_TO_YOUR_EDGE_DRIVER")
        if path is None:
            logging.error(
                "The PATH_TO_YOUR_EDGE_DRIVER environment variable is not set."
            )
            raise EnvironmentError(
                "The PATH_TO_YOUR_EDGE_DRIVER environment variable is not set."
            )
        return os.path.normpath(path)

    def get_profile_directory(self):
        path = os.getenv("PATH_TO_YOUR_BROWSER_PROFILE_DIRECTORY")
        if path is None:
            logging.error(
                "The PATH_TO_YOUR_BROWSER_PROFILE_DIRECTORY environment variable is not set."
            )
            raise EnvironmentError(
                "The PATH_TO_YOUR_BROWSER_PROFILE_DIRECTORY environment variable is not set."
            )
        return os.path.normpath(path)

    def setup_driver(self):
        logging.info("Setting up the driver")
        os.makedirs(self.profile_directory, exist_ok=True)
        service = Service(executable_path=self.get_edgedriver_patch())
        return webdriver.Edge(service=service, options=self.edge_options)

    def setup_edge_options(self):
        logging.debug("Setting up Edge options")
        edge_options = Options()
        edge_options.add_argument(f"user-data-dir={self.profile_directory}")
        edge_options.add_argument("window-size=800,600")
        return edge_options

    def login_with_qr(self):
        logging.info("Accessing WhatsApp Web")
        self.driver.get("https://web.whatsapp.com/")
        try:
            logged_in = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, WhatsAppXpathElements().search_bar)
                )
            )
            if logged_in:
                logging.info("Already logged in.")
                return
            logging.info("Logging in with QR code")
            qr_code_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "canvas[aria-label='Scan me!']")
                )
            )
            self.display_qr_code()
            WebDriverWait(self.driver, 90).until(
                EC.presence_of_element_located(
                    (By.XPATH, WhatsAppXpathElements().search_bar)
                )
            )
            logging.info("Login successful.")
        except TimeoutException as e:
            logging.warning("Timeout waiting for QR code or login completion.")

    def display_qr_code(self):
        logging.debug("Displaying QR code")
        qr_code_element = self.driver.find_element(
            By.CSS_SELECTOR, "canvas[aria-label='Scan me!']"
        )
        qr_code_element.screenshot(self.qr_code_path)
        from PIL import Image
        import matplotlib.pyplot as plt

        img = Image.open(self.qr_code_path)
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    def ensure_directories_exist(self):
        logging.debug("Ensuring directories exist")
        os.makedirs(os.path.dirname(self.qr_code_path), exist_ok=True)

    def send_message(self, contact_name, message):
        logging.info(f"Sending message to {contact_name}")
        self.driver.get("https://web.whatsapp.com/")

        search_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, WhatsAppXpathElements().search_bar)
            )
        )
        search_box.clear()
        search_box.send_keys(contact_name + Keys.ENTER)

        message_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, WhatsAppXpathElements().message_box)
            )
        )

        message_box.click()
        message_box.clear()
        message_box.send_keys(message + Keys.ENTER)
        logging.info("Message sent successfully.")

    def send_attachment(self, contact_name, file_path):
        logging.info(f"Sending attachment to {contact_name}")
        self.send_message(contact_name, "")
        plus_button = self.driver.find_element(
            By.XPATH, WhatsAppXpathElements().plus_button
        )
        plus_button.click()
        send_document = self.driver.find_element(
            By.XPATH, WhatsAppXpathElements().send_document
        )
        send_document.click()
        file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(file_path)
        time.sleep(1)
        send_button = self.driver.find_element(
            By.XPATH, WhatsAppXpathElements().send_button
        )
        send_button.click()
        logging.info("Attachment sent successfully.")

    def get_unread_messages(self):
        logging.info("Getting unread messages")
        self.driver.get("https://web.whatsapp.com/")
        unread_elements = self.driver.find_elements(
            By.XPATH, "//span[@aria-label='unread message']"
        )
        messages = []
        for element in unread_elements:
            contact = element.find_element(By.XPATH, "../..").text.split("\n")[0]
            message_preview = element.text
            messages.append({"contact": contact, "message": message_preview})
        return messages

    def get_messages_with_contact(self, contact_name):
        logging.info(f"Getting messages with {contact_name}")
        self.send_message(contact_name, "")
        message_elements = self.driver.find_elements(
            By.XPATH, WhatsAppXpathElements().message_history
        )
        messages = [message.text for message in message_elements]
        return messages
