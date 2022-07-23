from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

from time import sleep

PATH_CHROME = "./Chromium/chrome.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')

browser = webdriver.Chrome(PATH_CHROME, service=Service(
    ChromeDriverManager().install()), chrome_options=options)


browser.get('https://monkeytype.com')
sleep(10)
print("web Loaded !")

# if needed accept cookie
try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class=" css-47sehv"]'))).click()
except:
    pass

try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="button active acceptAll"]'))).click()
except:
    pass

print("accept cookie !")

try:
    while True:
        line_words_div = browser.find_element(By.ID, "words")
        words = line_words_div.find_elements(By.TAG_NAME, "div")
        keyboard = webdriver.ActionChains(browser)

        for word in words:
            if word.get_attribute("class") == "word active":
                letters = word.find_elements(By.TAG_NAME, "letter")

                for lett in letters:
                    keyboard.send_keys(lett.text)
                keyboard.send_keys(" ")

            keyboard.perform()

finally:
    sleep(20)
    print("Done !")
    browser.close()
