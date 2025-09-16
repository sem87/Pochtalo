from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag
from googleteable import *
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

a = 4

options = Options()
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Google Chrome 119.0.6045.160")
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # отключает тестовое ПО
options.add_experimental_option('useAutomationExtension', False)  # прочитать
options.add_argument("--disable-blink-features=AutomationControlled")  # прочитать
# максимальное окно сразу
options.add_argument("start-maximized")
# Запускает браузер в безголовом режиме (без графического интерфейса, фоном), что полезно для автоматизации и тестирования
options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {'source': 'delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array'})
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {'source': 'delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON'})
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {'source': 'delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object'})
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {'source': 'delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise'})
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {'source': 'delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy'})
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {'source': 'delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol'})


def pusk_GisMeteo():
    """ЗАХОДИТ"""
    driver.get("https://www.gismeteo.ru/weather-ufa-4588/10-days/")
    time.sleep(a)


def parsing_GisMeteo():
    """ФУНКЦИЯ ПАРСИНГА"""
    # Получение исходного кода страницы Инициализация Beautiful Soup
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # Находим нужный нам html объект по тегу и его class
    time.sleep(a)
    body_alls = soup.find('div', class_='widget-items js-scroll-item')

    """ДАТА И ДЕНЬ НЕДЕЛИ"""
    try:
        # ЦИФРОЙ В [] УКАЗЫВАЕМ НУЖНЫЙ ПАРАМЕТР
        driver.implicitly_wait(a)
        dni_vses = body_alls.find_all("div", recursive=False)[0]
        nom = 53
        time.sleep(a)
        for den in dni_vses:
            nom = nom + 1
            zna_1 = "O" + str(nom)
            zna_2 = "P" + str(nom)
            if den.div.text:  # isinstance(den, Tag) and
                den_ned = den.find_all("div", recursive=False)[0]
                # print(den_ned.text)
                Izmenenie(Nazvanie_operazii="День недели", diapozon_dannich=f'Данные!{zna_1}',
                          znachenie=[[den_ned.text]])
                chislo = den.find_all("div", recursive=False)[1]
                # print(chislo.text)
                Izmenenie(Nazvanie_operazii="День недели", diapozon_dannich=f'Данные!{zna_2}',
                          znachenie=[[chislo.text]])
    except:
        print("ОШИБКА В : ДАТА И ДЕНЬ НЕДЕЛИ")

    """СОСТОЯНИЕ ПОГОДЫ , ИКОНКИ"""
    try:
        sostoanie_vse = body_alls.find_all("div", recursive=False)[1]
        nom = 53
        time.sleep(a)
        for sostoanie in sostoanie_vse:
            nom = nom + 1
            sost_odin = "Q" + str(nom)
            # ОПРЕДЕЛЯЕМ ЗНАЧЕНИЕ ['data-tooltip']
            sost = str(sostoanie['data-tooltip'])
            Izmenenie(Nazvanie_operazii="День недели", diapozon_dannich=f'Данные!{sost_odin}', znachenie=[[sost]])
    except:
        print("ОШИБКА В : СОСТОЯНИЕ ПОГОДЫ , ИКОНКИ")

    """ТЕМПЕРАТУРА MAX , MIN ЗА ДЕНЬ"""
    try:
        temperatura_vsa = body_alls.find_all("div", recursive=False)[2].div.div
        nom = 53
        time.sleep(a)
        for temperatura in temperatura_vsa:
            nom = nom + 1
            zna_max = "R" + str(nom)
            zna_min = "S" + str(nom)
            # Максимальная температура
            t_max = temperatura.find_all("div", recursive=False)[0]
            Izmenenie(Nazvanie_operazii="Температура", diapozon_dannich=f'Данные!{zna_max}', znachenie=[[t_max.text]])
            # Минимальная температура
            t_min = temperatura.find_all("div", recursive=False)[1]
            Izmenenie(Nazvanie_operazii="Температура", diapozon_dannich=f'Данные!{zna_min}', znachenie=[[t_min.text]])
    except:
        print("ОШИБКА В : ТЕМПЕРАТУРА MAX , MIN ЗА ДЕНЬ")

    """ПОРЫВЫ ВЕТРА"""
    try:
        veter_vse = body_alls.find_all("div", recursive=False)[6]
        nom = 1
        time.sleep(a)
        for veter in veter_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(veter, Tag) and veter.name == 'div':
                nom = nom + 53
                veter_odin = "T" + str(nom)
                # ОПРЕДЕЛЯЕМ ЗНАЧЕНИЕ ['data-tooltip']
                vet = str(veter['data-tooltip'])
                Izmenenie(Nazvanie_operazii="Ветер", diapozon_dannich=f'Данные!{veter_odin}', znachenie=[[vet]])
    except:
        print("ОШИБКА В : ПОРЫВЫ ВЕТРА")

    """ОСАДКИ В ЖИДКОМ ВИДЕ"""
    try:
        osadki_vse = body_alls.find_all("div", recursive=False)[11]
        nom = 53
        time.sleep(a)
        for osadki in osadki_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(osadki, Tag) and osadki.name == 'div':
                nom = nom + 1
                osadki_odin = "U" + str(nom)
                osad = osadki.div.text
                Izmenenie(Nazvanie_operazii="Осадки", diapozon_dannich=f'Данные!{osadki_odin}', znachenie=[[osad]])
    except:
        print("ОШИБКА В : ОСАДКИ В ЖИДКОМ ВИДЕ")

    """ВЫПАДАЮЩИЙ СНЕГ"""
    try:
        sneg_vse = body_alls.find_all("div", recursive=False)[12]
        nom = 53
        time.sleep(a)
        for sneg in sneg_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(sneg, Tag) and sneg.name == 'div':
                nom = nom + 1
                osadki_odin = "V" + str(nom)
                sne = sneg.span.text
                Izmenenie(Nazvanie_operazii="СНЕГ", diapozon_dannich=f'Данные!{osadki_odin}', znachenie=[[sne]])
    except:
        print("ОШИБКА В : ВЫПАДАЮЩИЙ СНЕГ")

    """ВЫСОТА СНЕЖНОГО ПОКРОВА,с начала года"""
    try:
        visota_vse = body_alls.find_all("div", recursive=False)[13].div.div
        nom = 53
        time.sleep(a)
        for visota in visota_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(visota, Tag) and visota.name == 'div':
                nom = nom + 1
                visota_odin = "W" + str(nom)
                visot = visota.text
                Izmenenie(Nazvanie_operazii="ВЫСОТА СНЕГА", diapozon_dannich=f'Данные!{visota_odin}',
                          znachenie=[[visot]])
    except:
        print("ОШИБКА В : ВЫСОТА СНЕЖНОГО ПОКРОВА,с начала года")

    """ДАВЛЕНИЕ"""
    try:
        davlenie_vse = body_alls.find_all("div", recursive=False)[14].div.div
        nom = 53
        time.sleep(a)
        for davlenie in davlenie_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(davlenie, Tag) and davlenie.name == 'div':
                nom = nom + 1
                davlenie_max = "X" + str(nom)
                davlenie_min = "Y" + str(nom)
                # Давление max
                davl_max = davlenie.find_all("div", recursive=False)[0].text
                Izmenenie(Nazvanie_operazii="Давление", diapozon_dannich=f'Данные!{davlenie_max}',
                          znachenie=[[davl_max]])
                # Давление min
                davl_min = davlenie.find_all("div", recursive=False)[1].text
                Izmenenie(Nazvanie_operazii="Давление", diapozon_dannich=f'Данные!{davlenie_min}',
                          znachenie=[[davl_min]])
    except:
        print("ОШИБКА В : ДАВЛЕНИЕ")

    """ОТНОСИТЕЛЬНАЯ ВЛАЖНОСТЬ"""
    try:
        vlaznost_vse = body_alls.find_all("div", recursive=False)[15]
        nom = 53
        time.sleep(a)
        for vlaznost in vlaznost_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(vlaznost, Tag) and vlaznost.name == 'div':
                nom = nom + 1
                vlaznost_odin = "Z" + str(nom)
                vlazn = vlaznost.text
                Izmenenie(Nazvanie_operazii="ВЛАЖНОСТЬ", diapozon_dannich=f'Данные!{vlaznost_odin}',
                          znachenie=[[vlazn]])
    except:
        print("ОШИБКА В : ОТНОСИТЕЛЬНАЯ ВЛАЖНОСТЬ")

    """УФ ИНДЕКС"""
    try:
        yf_vse = body_alls.find_all("div", recursive=False)[16]
        nom = 53
        time.sleep(a)
        for yf in yf_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(yf, Tag) and yf.name == 'div':
                nom = nom + 1
                yf_odin = "AA" + str(nom)
                yf = yf.text
                Izmenenie(Nazvanie_operazii="УФ", diapozon_dannich=f'Данные!{yf_odin}', znachenie=[[yf]])
    except:
        print("ОШИБКА В : УФ ИНДЕКС")

    """Г/м активность, Кп-индекс"""
    try:
        geo_vse = body_alls.find_all("div", recursive=False)[17]
        nom = 53
        time.sleep(a)
        for geo in geo_vse:
            # Пропускает только теги div с помощью .name
            if isinstance(geo, Tag) and geo.name == 'div':
                nom = nom + 1
                geo_odin = "AB" + str(nom)
                kp_odin = "AC" + str(nom)
                # Г/м активность
                ge = str(geo['data-tooltip'])
                Izmenenie(Nazvanie_operazii="Г/м активность", diapozon_dannich=f'Данные!{geo_odin}', znachenie=[[ge]])
                # Кп-индекс
                kp = geo.div.text
                Izmenenie(Nazvanie_operazii="Г/м активность", diapozon_dannich=f'Данные!{kp_odin}', znachenie=[[kp]])
    except:
        print("ОШИБКА В : Г/м активность, Кп-индекс")


"""__________________АНАЛИЗ ДАННЫХ ________________"""


def vivod():
    """СЧИТЫВАЕТ ДАННЫЕ О ПОГОДЕ И ПЫТАЕТСЯ ИЗ ЭТОГО ДЕЛАТЬ РЕКОМЕНДАЦИИ О ПРОДАЖЕ"""
    # Считываем все в список pog_sp
    pog_sp = []
    for num in range(54, 63, 1):
        yacheika = "O" + str(num)
        pogoda = Read(Nazvanie_operazii='ЧИТАЕМ ', range=f"Данные!{yacheika}:AC63")
        # pog_sp.append(pogoda)
        # print(pogoda)

        """____________Начинаем Анализ_____________"""

        """СОСТОЯНИЕ"""  # Добавить состояние
        if str(pogoda[2]) == "Дождь":
            sostoanie = " Люди не хотят мокнуть . "
        elif str(pogoda[2]) == "Снег":
            sostoanie = " Затруднительное движение транспорта . "
        else:
            sostoanie = ""

        """ТЕМПЕРАТУРА, берем max"""
        if int(pogoda[3]) > 24:
            temper = " Жарко : общая слабость,недомогание . "
        elif int(pogoda[3]) > -25:
            temper = ""
        else:
            temper = " Слишком холодно . "

        """ДАВЛЕНИЕ ,MIN"""
        if int(pogoda[10]) < 751:
            davlenie = "Приступы слабости,нервозности,беспокойство . "
        elif int(pogoda[10]) > 763:
            davlenie = "Головные боли и в сердце,давление"
        else:
            davlenie = ""

        """ОТНОСИТЕЛЬНАЯ ВЛАЖНОСТЬ"""
        if int(pogoda[11]) > 70:
            vlaznost = "ШАРЫ не летают"
        elif int(pogoda[11]) > 40:
            vlaznost = " "
        else:
            vlaznost = "СЛИШКОМ СУХОЙ ВОЗДУХ"

        """Г/м активность"""
        if str(pogoda[13]) == "Умеренная буря":
            geo = "Магнитная буря"
        elif str(pogoda[13]) == "Слабая буря":
            geo = "Магнитная буря"
        elif str(pogoda[13]) == "Буря":
            geo = "Магнитная буря"
        else:
            geo = ""

        """_____ПОДИТОЖИМ____"""
        vivod = "AD" + str(num)
        itog = temper + sostoanie + davlenie + vlaznost + geo
        Izmenenie(Nazvanie_operazii="Г/м активность", diapozon_dannich=f'Данные!{vivod}', znachenie=[[itog]])


if __name__ == "__main__":
    pusk_GisMeteo()
    time.sleep(a)
    parsing_GisMeteo()
    driver.close()
    driver.quit()
    vivod()
