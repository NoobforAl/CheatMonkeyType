"""
    Cheat Monkey type !
       simple selenium app for type !
"""


from install_chromium import DownloadFileChromium, FindChromeFolder

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.remote.webelement import WebElement

from typing import List
from time import sleep

import os


# set option for chrome
# accept all
options: Options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')

# first check can find browser ?
PATH_CHROME = FindChromeFolder()


def _chromeIsExists():
    global PATH_CHROME

    if not os.path.exists(PATH_CHROME):
        print("can't find Chromium Download file started!")
        PATH_CHROME = DownloadFileChromium()
        assert PATH_CHROME == "", "not found chrome!"


def _loadPage(browser: WebDriver) -> None:
    browser.get('https://monkeytype.com')
    sleep(5)
    print("web Loaded !")


def _acceptCookie1(browser: WebDriver) -> bool:
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@class=" css-47sehv"]'))).click()
        return True
    except:
        return False


def _acceptCookie2(browser: WebDriver) -> bool:
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@class="button active acceptAll"]'))).click()
        return True
    except:
        return False


def _acceptCookies(browser: WebDriver) -> None:
    ac1, ac2 = 0, 0

    while True:
        if not _acceptCookie1(browser) and 2 > ac1:
            print("retry for accept cookie")
            ac1 += 1
            continue

        if not _acceptCookie2(browser) and 2 > ac2:
            print("retry for accept cookie")
            ac2 += 1
            continue

        break
    print("accept cookies !")


def _interWords(browser: WebDriver) -> None:

    _loadPage(browser)
    _acceptCookies(browser)

    keyboard: ActionChains = webdriver.ActionChains(browser)

    while True:
        line_words_div: WebElement = browser.find_element(By.ID, "words")
        words: List[WebElement] = line_words_div.find_elements(
            By.TAG_NAME, "div")

        check: WebElement = line_words_div.find_element(
            By.XPATH, "//div[contains(@class, 'word active')]")

        for word in words[words.index(check):]:
            letters: List[WebElement] = word.find_elements(
                By.TAG_NAME, "letter")

            [keyboard.send_keys(lett.text) for lett in letters]
            keyboard.send_keys(" ")
            keyboard.perform()


def run() -> None:
    _chromeIsExists()

    global options
    global PATH_CHROME

    browser: WebDriver = webdriver.Chrome(PATH_CHROME, service=Service(
        ChromeDriverManager().install()), options=options)

    try:
        _interWords(browser)

    except Exception as err:
        print(err)

    finally:
        print("see result!\n after 20s exit!")
        sleep(20)
        print("Finish !")
        browser.close()


if __name__ == "__main__":
    run()
