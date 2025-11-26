import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

def get_driver():
    log.info("Запуск драйвера")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,720")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)