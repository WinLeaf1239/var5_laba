#Нужные модули:
#pip install undetected-chromedriver - обязательно установить
#pip install setuptools - обязательно установить

#Устанавливаем хром 156:
#https://googlechromelabs.github.io/chrome-for-testing/#stable - отсюда скачиваем версию хрома 156

#Доп по коду:
#Не удалось реализовать в полной мере прокси, хоть было потрачено приличное количество времени
#Увы вайлдбериз слишком хорошо защищен, и практически все бесплатные прокси были попробованы, но
#в доказательство того что знаю как применить этот легкий трюк, оставил закоментированную строчку кода

#последняя функция и строчка после всех импортов, это ответ на специфический ошибки специального драйвера undetected_chromedriver

import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
 
uc.Chrome.__del__ = lambda self: None  # фикс ошибки с закрытием драйвера

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36")


def log(event):
    data = {
        "Событие": [str(event).split("\n")[0]],
        "Время": [time.strftime("%Y-%m-%d %H:%M:%S")],
        "Пользователь": [os.environ.get("USERNAME")],
    }
    loger = pd.DataFrame(data)
    loger.to_csv("log.csv", index=False, mode="a", sep=";",
                 header=not os.path.isfile("log.csv"), encoding="utf-8-sig")


class Parcer():

    def __init__(self, link, klas):
        self.link = link
        self.klas = klas
        chrome_156_path = r"D:\chrome-win64\chrome.exe"
 
        self.options = uc.ChromeOptions()
        # self.options.add_argument(f"--proxy-server=Введите прокси") Бесплатных прокси на вайлдбериз нету, которые смог нарыть не подошли. Да и в целом у вайлдбериз очень хорошая защита от проксей
        self.options.add_argument(f"--user-agent={USER_AGENT}")
        self.driver = uc.Chrome(options=self.options, browser_executable_path=chrome_156_path)
        self.driver.get(self.link)
 
        time.sleep(12)
 
    def accept_cookie(self):
        click_cookie = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cookies__btn")))
        click_cookie.click()
        time.sleep(1)
 
    def scroll(self):
        while True:
            then_stranica = self.driver.execute_script("return window.scrollY;")
            self.driver.execute_script("window.scrollBy(0, window.innerHeight * 0.7);")
            time.sleep(0.5)
            after_stranica = self.driver.execute_script("return window.scrollY;")
            if after_stranica == then_stranica:
                break
 
    def getlinks(self):
        items = []
        for element in self.driver.find_elements(By.CLASS_NAME, self.klas):
            title = element.get_attribute('aria-label') or ''
            if 'superlight 2' in title.lower() and 'глайды' not in title.lower():
                items.append((element.get_attribute('href'), title))
        return items
        
 
    def parse_and_save(self, items, filename="var.csv"):
        rows = []
        for href, title in items:
            try:
                self.driver.get(href)
                click_hka = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "btnDetail--OZvtD")))
                click_hka.click()
                time.sleep(1)
 
                row = {"Название": title, "Ссылка": href}
                thes = self.driver.find_elements(By.TAG_NAME, 'th')
                tdes = self.driver.find_elements(By.TAG_NAME, 'td')
                for th, td in zip(thes, tdes):
                    if th.text:
                        row[th.text] = td.text
                rows.append(row)
            except Exception as e:
                log(f"Пропущен товар {href}: {type(e).__name__}")
 
        tablica = pd.DataFrame(rows) 
        tablica.to_csv(filename, index=False, sep=";", encoding="utf-8-sig")
 
    def close(self): #специфическое закрытие специфического браузера
        if self.driver:
            try:
                self.driver.quit()
            except OSError:
                pass
            finally:
                self.driver = None
