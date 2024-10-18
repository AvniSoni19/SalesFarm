from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import pandas as pd
import time


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    ua = UserAgent()
    user_agent = ua.random
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--disable-accelerated-2d-canvas")
    chrome_options.add_argument("--disable-accelerated-jpeg-decoding")
    chrome_options.add_argument("--disable-accelerated-mjpeg-decode")
    chrome_options.add_argument("--disable-app-list-dismiss-on-blur")
    chrome_options.add_argument("--disable-backing-store-limit")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--disable-canvas-aa")
    chrome_options.add_argument("--disable-composited-antialiasing")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-features=TranslateUI")
    chrome_options.add_argument("--disable-hang-monitor")
    chrome_options.add_argument("--disable-ipc-flooding-protection")
    chrome_options.add_argument("--disable-ipv6")
    chrome_options.add_argument("--disable-low-res-tiling")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-prompt-on-repost")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--disable-threaded-animation")
    chrome_options.add_argument("--disable-threaded-scrolling")
    chrome_options.add_argument("--disable-translate")
    chrome_options.add_argument("--disable-vulkan-fallback-to-gl")
    chrome_options.add_argument("--enable-features=NetworkService")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--password-store=basic")
    chrome_options.add_argument("--use-gl=swiftshader")
    chrome_options.add_argument("--window-size=1920,1080")

    chrome_driver_path = 'C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe'
    s = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=s, options=chrome_options)
    return driver


def wait_for_element(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))


def scrape_linkedin_links(df):
    driver = get_driver()

    Linkedin_links = []

    for com, loc in zip(df['Company'], df['Location']):
        search_string = f'{com} {loc} site:linkedin.com'
        search_string = search_string.replace(' ', '+')

        driver.get(f"https://www.google.com/search?q={search_string}&start=")

        link_string = com.replace(' ', '-').lower()
        xpath = f"//div[contains(@class,'yuRUbf')]/a[contains(@href,{link_string})]"

        link_element = wait_for_element(driver, By.XPATH, xpath)
        link = link_element.get_attribute('href')
        Linkedin_links.append(link)
        print(link)
        time.sleep(3)

    driver.quit()

    df1 = pd.DataFrame({"LinkedIn Links": Linkedin_links})
    df1.to_csv("naukri1.com.csv", index=False)


df = pd.read_csv('naukri.com.csv')
scrape_linkedin_links(df)