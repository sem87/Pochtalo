import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import emoji

'''ДРУГИЕ БИБЛИОТЕКИ'''
import os
from pyrogram import Client
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import InputMediaPhoto
import random
import pickle
import pyautogui
from googleteable2tab import *
from dotenv import find_dotenv, load_dotenv
from Pogod import *

load_dotenv(find_dotenv())

'''ВХОДНЫЕ ДАННЫЕ'''
# Данные телеграмма

api_id = '' "
api_hash = '' "
client = Client(name='zzz', api_id=api_id, api_hash=api_hash, parse_mode=ParseMode.HTML)

client.start()

# Время
a = 4
b = 26
# driver.implicitly_wait(a)   МОЖЕТ И ПРИМЕНИТЬ ГДЕ
inst = 29
text_vk = []
foto = [r'C:\ПРОГРАММЫ\КОДЫ РОБОТОВ\Код РОБОТОВ\Файлы\SEM.jpg']
'''Для ВАТСАПП'''
spisok = ['ГНОМ магазин детских товаров']
text = []
"СПИСОК НАЗВАНИЯ ГРУПП В ВАТСАПП ,У МЕНЯ ИХ ОКОЛО 200"
spisok_w = ['Привет', 'Доска объявлений. Башкирия. Г. Уфа.', 'БашкортТоргПлощадка Уфа','_____КОНЕЦ_____']

ssilki_gruppi = ['ССЫЛКИ РЕКЛАМА ОБЪЯВЛЕНИЯ', 'Обмен ссылками', 'Ссылки Давлеканово, Раевка, Чишмы',
                 'Ссылочная РБ 702рус', '`Ссылочная102rus', 'Ссылочная Башкортостан', '💥Полезная ссылочка💥',
                 'Ссылочная 02 102 702']
# ХРОМ ДРАЙВЕР950
options = Options()
# Указываем путь сохранения по умолчанию и название
prefs = {"download.default_directory": r'C:\ПРОГРАММЫ\Файлы',
         "download.default_filename": "hel"}
options.add_experimental_option("prefs", prefs)
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Google Chrome 119.0.6045.160")
# отключает тестовое ПО
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# отключает использование расширения автоматизации
options.add_experimental_option('useAutomationExtension', False)
# Отключает функцию, связанную с автоматизированным управлением браузером.
# Это часто используется для обхода обнаружения автоматизации веб-сайтами,
# которые стремятся предотвратить автоматизированный доступ.
options.add_argument(
    "--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

'''_____________________НАЧАЛО КОДА_________________'''


def nashalo_koda():
    """__________________Открываем ВАТСАПП________________________"""
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    time.sleep(60)


def zapominaet_soobshenie():
    """ЗАПОМИНАЕТ ФОТО И ТЕКСТ"""
    try:
        for gruppa in spisok:
            poisk_gr = driver.find_element(By.CLASS_NAME, '_ai04').find_element(By.TAG_NAME, 'p')
            # poisk_gr = driver.find_element(By.CSS_SELECTOR, '[aria-label="Текстовое поле поиска"]')
            time.sleep(a)
            # очищаем от эмодзи
            poisk_gr.send_keys(emoji.replace_emoji(gruppa, replace=''))
            time.sleep(a)
            # Заходим в группу
            driver.find_element(By.CSS_SELECTOR, f'span[title="{gruppa}"]').click()
            # ЧТО БЫ СИНХРОНИЗИРОВАТЬ ДАННЫЕ ВРЕМЯ УВЕЛИЧИТЬ ,А ТАК b
            time.sleep(120)
            # найти текст
            tekst = \
                driver.find_elements(By.CSS_SELECTOR, '[aria-label="Открыть изображение"][role="button"]')[
                    -1].find_element(
                    By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'div')[-1].find_element(By.TAG_NAME,
                                                                                           'img').get_attribute('alt')
            text.append(tekst)
            # найти и сохранить изображение
            driver.find_elements(By.CSS_SELECTOR, '[aria-label="Открыть изображение"][role="button"]')[-1].click()
            time.sleep(40)
            driver.find_elements(By.CSS_SELECTOR, '[aria-label="Скачать"][title="Скачать"]')[-1].click()
            time.sleep(a)
            # Переименовывает фото
            os.chdir(r'C:\ПРОГРАММЫ\КОДЫ РОБОТОВ\Код РОБОТОВ\Файлы')
            for name in os.listdir('.'):
                if name.startswith('WhatsApp Image'):
                    os.rename(name, 'SEM.jpg')
                    break
    except Exception as ex:
        print(ex)
        print('ВАТСАП не запомнил сообщение')
        driver.close()
        driver.quit()
    finally:
        pass


def gruppi_watapp():
    """Формирует отправку в ВАТСАПП"""
    # foto = [r'C:\ПРОГРАММЫ\Файлы\SEM.jpg']
    textadres = [
        ' По вопросам пишите ватсап ',
        ' По вопросам ватсап ']
    text_w = str(str(''.join(random.sample(text, 1))) + str(''.join(random.sample(textadres, 1))))
    print(text_w)
    photo = random.sample(foto, 1)
    print(photo)
    otpravka_soobshenii(text=text_w, photo=photo)
    print('___________________________ВСЕ ПО Группам ВАТСАП РАЗОСЛАНО_________________')


def otpravka_soobshenii(text, photo):
    """Функция пересылает сообщение в ВАТСАПП"""
    counter = 0
    vipolneno = []
    oshibka = []

    driver.find_element(By.CSS_SELECTOR, '[title="Закрыть"]').click()
    for gruppa in spisok_w:
        try:
            poisk_gr = driver.find_element(By.CLASS_NAME, '_ai04').find_element(By.TAG_NAME, 'p')
            # poisk_gr = driver.find_element(By.CSS_SELECTOR, '[aria-label="Текстовое поле поиска"]')
            time.sleep(a)
            # очищаем от эмодзи
            poisk_gr.send_keys(emoji.replace_emoji(gruppa, replace=''))
            time.sleep(a)
            driver.find_element(By.CSS_SELECTOR, f'span[title="{gruppa}"]').click()
            time.sleep(a)
            # вводим текст
            driver.find_element(By.CSS_SELECTOR, '[aria-placeholder="Введите сообщение"]').send_keys(text)
            time.sleep(a)
            # Плюс
            driver.find_element(By.CSS_SELECTOR, 'button[title="Прикрепить"]').click()
            time.sleep(a)
            # Загрузка фотографии
            driver.find_element(By.CSS_SELECTOR,
                                'input[accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(photo)
            time.sleep(a)
            # Подтверждение отправки фотографии
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Отправить"]').click()
            time.sleep(a)
            vipolneno.append(gruppa)
            print('УСПЕШНО : ' + gruppa)
            # Данные для гугл таблици ,должно быть 2 списка [[]]
            spgoogle = []
            spgoogle1 = []
            spgoogle1.append(gruppa)
            spgoogle1.append("успешно")
            spgoogle.append(spgoogle1)
            # print(spgoogle)
            # # ДОБАВЛЯЕМ УСПЕШНЫЕ ДАННЫЕ В ГУГЛ ТАБЛИЦУ   Для  C2 пишем
            # time.sleep(a)
            # Dobavlenie2(Nazvanie_operazii='ДОБАВЛЯЕМ В ТАБЛИЦУ', diapozon_dannich='ВАТСАП КОНТРОЛЬ!C2:C',
            #             znachenie=spgoogle)
        except ValueError:
            print('ValueError          ВНИМАНИЕ ЭТО ОПЫТ    ')
        except:
            # Очистка поля ввода
            poisk_gr = driver.find_element(By.CLASS_NAME, '_ai04').find_element(By.TAG_NAME, 'p')
            # poisk_gr = driver.find_element(By.CSS_SELECTOR, '[aria-label="Текстовое поле поиска"]')
            p = 0
            time.sleep(a)
            while p < 70:
                driver.find_element(By.CLASS_NAME, '_ai04').find_element(By.TAG_NAME, 'p').send_keys(Keys.BACKSPACE)
                time.sleep(0.05)
                p = p + 1
            counter += 1
            oshibka.append(gruppa)
            print('ошибка : ' + gruppa)
            # Данные для гугл таблици ,должно быть 2 списка [[]]
            spgoogle = []
            spgoogle1 = []
            spgoogle1.append(gruppa)
            spgoogle1.append("ОШИБКА")
            spgoogle.append(spgoogle1)
            # print(spgoogle)
            # # ДОБАВЛЯЕМ УСПЕШНЫЕ ДАННЫЕ В ГУГЛ ТАБЛИЦУ   Для С2 пишем
            # Dobavlenie2(Nazvanie_operazii='ДОБАВЛЯЕМ В ТАБЛИЦУ', diapozon_dannich='ВАТСАП КОНТРОЛЬ!C2:C',
            #             znachenie=spgoogle)
        finally:
            pass
    print('чаты которые РАБОТАЮТ !!!', 'количество :', len(vipolneno), vipolneno)
    print('чаты с ОШИБКОЙ !!!', 'количество :', len(oshibka), oshibka)


def otpravka_ssilki():
    """Функция пересылает ССЫЛКИ в ВАТСАПП ГРУППЫ"""
    text_ssilki = 'ссылки: https://t.me/ - телеграм  , https://vk.com/ - группа ВК '  # группа магазина
    counter = 0
    vipolneno = []
    oshibka = []
    for gruppa_ssilki in ssilki_gruppi:
        try:
            poisk_gr = driver.find_element(By.CLASS_NAME, '_ai04').find_element(By.TAG_NAME, 'p')
            # poisk_gr = driver.find_element(By.CSS_SELECTOR, '[aria-label="Текстовое поле поиска"]')
            time.sleep(a)
            # очищаем от эмодзи
            poisk_gr.send_keys(emoji.replace_emoji(gruppa_ssilki, replace=''))
            time.sleep(a)
            driver.find_element(By.CSS_SELECTOR, f'span[title="{gruppa_ssilki}"]').click()
            time.sleep(a)
            # вводим текст
            driver.find_element(By.CSS_SELECTOR, '[aria-placeholder="Введите сообщение"]').send_keys(text_ssilki)
            time.sleep(a)
            # Подтверждение отправки фотографии
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Отправить"]').click()
            time.sleep(a)
            vipolneno.append(gruppa_ssilki)
        except ValueError:
            print('ValueError          ВНИМАНИЕ ЭТО ОПЫТ    ')
        except:
            # Очистка поля ввода
            poisk_gr = driver.find_element(By.CLASS_NAME, '_ai04').find_element(By.TAG_NAME, 'p')
            # poisk_gr = driver.find_element(By.CSS_SELECTOR, '[aria-label="Текстовое поле поиска"]')
            p = 0
            while p < 70:
                driver.find_element(By.CLASS_NAME, '_ai04').find_element(By.TAG_NAME, 'p').send_keys(Keys.BACKSPACE)
                time.sleep(0.05)
                p = p + 1
            counter += 1
            oshibka.append(gruppa_ssilki)
        finally:
            pass
    print('ССЫЛКИ РАБОТАЮТ !!!', 'количество :', len(vipolneno), vipolneno)
    print('ССЫЛКИ с ОШИБКОЙ !!!', 'количество :', len(oshibka), oshibka)


# _________________ТЕЛЕГРАМ______________
def telegram_otpravka_gnom():
    gr = ["zzzzz"]
    list_media = []
    media_1 = InputMediaPhoto(r'C:\ПРОГРАММЫ\Файлы\SEM.jpg', caption=text[0])
    list_media.append(media_1)
    for gruppa in gr:
        try:
            client.send_chat_action(gruppa, ChatAction.UPLOAD_PHOTO)
            time.sleep(a)
            client.send_chat_action(gruppa, ChatAction.TYPING)
            client.send_media_group(gruppa, list_media)
            print('ТЕЛЕГРАМ рассылка в группу ВЫПОЛНЕНО')
        except:
            print('ТЕЛЕГРАМ   ОШИБКА !!!')


def telegram_otpravka_gruppi():
    gr = ['izruk02', 'itsdematb', 'yarkiy_obyavleniya']  # НУЖНО КАК МОЖНО ГРУПП У МЕНЯ ИХ ОКОЛО 100

    list_media = []
    textadres = [
        '\n ☎️☎️☎️Телефон  ',
        '\n <b>Для справок</b> \n☎️☎️☎️ <b>телефон</b>  \n ']
    textrandom = str(str(text[0]) + str(''.join(random.sample(textadres, 1))))
    media_1 = InputMediaPhoto(r'C:\ПРОГРАММЫ\SEM.jpg', caption=textrandom)
    list_media.append(media_1)
    counter = 0
    chi = 0
    vipolneno = []
    oshibka = []
    for gruppa in gr:
        try:
            client.send_chat_action(gruppa, ChatAction.UPLOAD_PHOTO)
            time.sleep(a)
            client.send_chat_action(gruppa, ChatAction.TYPING)
            client.send_media_group(gruppa, list_media)
            counter += 1
            vipolneno.append(gruppa)
            # Данные для гугл таблици ,должно быть 2 списка [[]]
            spgoogle = []
            spgoogle1 = []
            spgoogle1.append(gruppa)
            spgoogle1.append("успешно")
            spgoogle.append(spgoogle1)
            # print(spgoogle)
            # # ДОБАВЛЯЕМ УСПЕШНЫЕ ДАННЫЕ В ГУГЛ ТАБЛИЦУ   Для Альбины C2:C пишем
            # Dobavlenie2(Nazvanie_operazii='ДОБАВЛЯЕМ В ТАБЛИЦУ', diapozon_dannich='ТЕЛЕГА КОНТРОЛЬ!C2:C',
            #             znachenie=spgoogle)
        except:
            chi += 1
            oshibka.append(gruppa)
            # Данные для гугл таблици ,должно быть 2 списка [[]]
            spgoogle = []
            spgoogle1 = []
            spgoogle1.append(gruppa)
            spgoogle1.append("ОШИБКА")
            spgoogle.append(spgoogle1)
            # print(spgoogle)
            # # ДОБАВЛЯЕМ УСПЕШНЫЕ ДАННЫЕ В ГУГЛ ТАБЛИЦУ
            # Dobavlenie2(Nazvanie_operazii='ДОБАВЛЯЕМ В ТАБЛИЦУ', diapozon_dannich='ТЕЛЕГА КОНТРОЛЬ!C2:C',
            #             znachenie=spgoogle)
        finally:
            pass
    print('чаты которые РАБОТАЮТ телеграмм !!!', 'количество :', len(vipolneno), vipolneno)
    print('чаты с ОШИБКОЙ телеграмм!!!', 'количество :', len(oshibka), oshibka)


# _________________ТЕЛЕГРАМ ЗАКОНЧЕНО______________
# _________________ВКОНТАКТЕ НАЧАЛО______________

def otkritie_vk():
    """Открытие в контакте"""
    driver.get("https://vk.com")
    driver.maximize_window()
    time.sleep(b)


def registrazia_vk(login, password, name):
    """Регистрируется в ВКОНТАКТЕ , ПОЛУЧАЕТ И ЗАПИСЫВАЕТ КУКИ"""
    try:
        try:
            """ДЛЯ ВЫХОДА В ДРУГОЙ АККАУНТ"""
            time.sleep(a)
            driver.find_element(By.XPATH, "//span[contains(text(), 'Войти в другой аккаунт')]").click()
            time.sleep(b)
        except:
            time.sleep(a)
        try:
            time.sleep(a)
            driver.find_element(By.XPATH,
                                "//span[@class='vkuiButton__content' and text()='Войти другим способом']").click()
            time.sleep(a)
        except:
            time.sleep(a)
        driver.find_element(By.CSS_SELECTOR, "input[name='login'][inputmode='tel']").send_keys(login)
        time.sleep(a)
        driver.find_element(By.XPATH, "//span[contains(@class, 'vkuiText') and text()='Сохранить вход']").click()
        time.sleep(a)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Войти')]").click()
        time.sleep(a)
        driver.find_element(By.CLASS_NAME, 'vkuiButton__content').click()
        time.sleep(a)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Пароль')]").click()
        time.sleep(a)
        driver.find_element(By.NAME, 'password').send_keys(password)  # СТАРАЯ ФОРМА СРАЗУ
        time.sleep(a)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Продолжить')]").click()
        time.sleep(a)
        pickle.dump(driver.get_cookies(), open(os.getcwd() + "albina.pcl", 'wb'))  # Записали все куки
        print(name + 'РЕГИСТРАЦИЮ ПРОШЛИ ,КУКИ ЗАПИСАЛИ!')
    except:
        print(name + 'С РЕГИСТРАЦИЕЙ ПРОВАЛ')


def podstavlaet_cookies_vk():
    """Подставляет куки в ВКОНТАКТЕ"""
    # driver.delete_all_cookies()
    time.sleep(a)
    cookies = pickle.load(open(os.getcwd() + "vkalbinacookie.pcl", 'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
    print('20 сек подожди еще')
    time.sleep(b)
    driver.refresh()
    time.sleep(b)


def rand():
    """Делает рандом из текста и соединяет его"""
    textadres = [
        '\n Телефон  . ',
        '\n Телефон  ']
    hechtegi = ['#уфа'']
    text_vk_rand = str(
        str(text[0]) + str(''.join(random.sample(textadres, 1))) + str(' '.join(random.sample(hechtegi, 8))))
    text_vk.append(text_vk_rand)


def propis_ssilki():
    """ПРОПИСЫВАЕТ ПУТЬ ССЫЛКИ ДЛЯ ФОТО .ВКЛАДКА НУЖНА АНГЛ"""
    pyautogui.write('C:\\', interval=0.25)
    pyautogui.hotkey('alt', 'shift')
    # Путь прописывать по англ как по-русски
    pyautogui.write('GHJUHFVVS\\RJLS HJ,JNJD\\Rjl HJ,JNJD\\Afqks', interval=0.1)
    pyautogui.hotkey('alt', 'shift')
    pyautogui.write(r'\SEM.jpg', interval=0.25)
    pyautogui.press('enter')


def stories_gruppi_vk(name_gruppi, ID):
    """ВЫКЛАДЫВАЕТ СТОРИС В ГРУППЕ"""
    try:
        time.sleep(a)
        driver.find_element(By.ID, ID).click()
        time.sleep(b)
        driver.find_element(By.CLASS_NAME, 'redesigned-group-avatar').click()
        time.sleep(a)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Создать историю')]").click()
        time.sleep(a)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Загрузить истории')]").click()
        time.sleep(a)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Выбрать файлы')]").click()
        time.sleep(a)
        propis_ssilki()
        time.sleep(b)
        driver.find_element(By.ID, 'stories_publish_btn').click()
        time.sleep(a)
        print('СТОРИС ВЫЛОЖЕНА ВК ГРУППА ' + name_gruppi)
    except:
        print('ОШИБКА СТОРИС ВК ГРУППА ' + name_gruppi)


def stories_lishnaya_vk(name_vk):
    """ВЫКЛАДЫВАЕТ СТОРИС НА ЛИЧНОЙ СТРАНИЦЕ"""
    try:
        time.sleep(a)
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(a)
        # клик по лента
        driver.find_element(By.ID, 'l_nwsf').click()
        time.sleep(b)
        time.sleep(a)
        # НАЖИМАЕТ ИСТОРИЯ
        driver.find_element(By.CLASS_NAME, "vkitStoryCard__avatar--zUHZi").click()
        time.sleep(a)
        # НАЖИМАЕТ выбрать файл
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='add-file-button']").click()
        time.sleep(a)
        propis_ssilki()
        time.sleep(b)
        # НАЖИМАЕТ опубликовать
        driver.find_element(By.XPATH,
                            '//button[contains(@class, "vkitButton__root--RejCB") and contains(., "Опубликовать")]').click()
        time.sleep(b)
    except:
        print('ОШИБКА ДЛЯ СТОРИС В ЛИЧНОЙ СТРАНИЦЕ В ВК ДЛЯ ' + name_vk)


def vk_otpravka(Name, ID):
    """ВЫКЛАДЫВАЕТ ПОСТ НА ЛИЧНОЙ СТРАНИЦЕ И В ГРУППАХ.НУЖНО : Name,ID """
    try:
        driver.find_element(By.XPATH,
                            "//div[@data-testid='leftmenuitem-text' and text()='Профиль']").click()  # клик по Профиль
        time.sleep(b)
        driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(a)
        driver.find_element(By.XPATH,
                            "//span[@class='vkuiButton__content' and text()='Создать пост']").click()  # клик по создать пост
    except:
        print(f'ОШИБКА ВК {Name} клик по создать пост ')
    # очищает поле ввода
    try:
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='Напишите что-нибудь...']").clear()
    except:
        time.sleep(a)
    # вводит текст
    try:
        time.sleep(b)
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='Напишите что-нибудь...']").send_keys(text_vk[0])
    except:
        print(f'ОШИБКА ВВОДА ТЕКСТА ВК {Name}')

    # вводит фото
    try:
        time.sleep(b)
        driver.find_element(By.XPATH, "//label[contains(@class, 'vkuiButton')]").click()
        time.sleep(b)
        propis_ssilki()
        time.sleep(b)
    except:
        print(f'ОШИБКА ВВОДА КАРТИНКИ ВК {Name}')
    # жмет кнопку опубликовать
    try:
        driver.find_element(By.XPATH,
                            "//span[@class='vkuiButton__content' and text()='Далее']").click()
        time.sleep(b)
        driver.find_element(By.XPATH,
                            "//span[@class='vkuiButton__content' and text()='Опубликовать']").click()
        time.sleep(b)
    except:
        print(f'НЕ НАЖАЛ ОПУБЛИКОВАТЬ ВК {Name}')


def vk_otpravka_gruppa_gelev_chari():
    """ВЫКЛАДЫВАЕТ ПОСТ В ГРУППАХ """
    # try:
    time.sleep(a)
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(a)
    driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()
    time.sleep(b)
    driver.execute_script("window.scrollTo(0, 1200);")
    time.sleep(a)
    try:
        time.sleep(a)
        driver.find_element(By.XPATH,
                            "//span[@class='vkuiButton__content' and text()='Создать пост']").click()  # клик по создать пост
    except:
        print(f'ОШИБКА ВК ПОСТ В ГРУППЕ  клик по создать пост ')
    # очищает поле ввода
    try:
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='Напишите что-нибудь...']").clear()
    except:
        print(f'ОШИБКА ВК ГРУППЕ  очищает поле ввода ')
    # вводит текст
    try:
        time.sleep(b)
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='Напишите что-нибудь...']").send_keys(text_vk[0])
    except:
        print(f'ОШИБКА ВВОДА ТЕКСТА ВК ГРУППЕ ')

    # вводит фото
    try:
        time.sleep(b)
        driver.find_element(By.XPATH, "//label[contains(@class, 'vkuiButton')]").click()
        time.sleep(b)
        propis_ssilki()
        time.sleep(b)
    except:
        print(f'ОШИБКА ВВОДА КАРТИНКИ ВК ГРУППЕ ')
    # жмет кнопку опубликовать
    try:
        driver.find_element(By.XPATH,
                            "//span[@class='vkuiButton__content' and text()='Далее']").click()
        time.sleep(b)
        driver.find_element(By.XPATH,
                            "//span[@class='vkuiButton__content' and text()='Опубликовать']").click()
        time.sleep(b)
    except:
        print(f'НЕ НАЖАЛ ОПУБЛИКОВАТЬ ВК ГРУППЕ ')
    # except:
    #     print(f'НЕ ОПУБЛИКОВАЛ ВК ГРУППЕ  ')


def vk_otpravka_gruppa_magaz_gnom():
    """ВЫКЛАДЫВАЕТ ПОСТ В ГРУППАХ """
    try:
        time.sleep(a)
        driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(a)
        driver.find_element(By.CSS_SELECTOR, "a[href='/gnomufa']").click()
        time.sleep(b)
        driver.execute_script("window.scrollTo(0, 1200);")
        time.sleep(a)
        try:
            time.sleep(a)
            driver.find_element(By.XPATH,
                                "//span[@class='vkuiButton__content' and text()='Создать пост']").click()  # клик по создать пост
        except:
            print(f'ОШИБКА ВК ПОСТ В ГРУППЕ МАГАЗИН  клик по создать пост ')
        # очищает поле ввода
        try:
            driver.find_element(By.CSS_SELECTOR, "span[aria-label='Напишите что-нибудь...']").clear()
        except:
            print(f'ОШИБКА ВК ГРУППЕ МАГАЗИН  очищает поле ввода ')
        # вводит текст
        try:
            time.sleep(b)
            driver.find_element(By.CSS_SELECTOR, "span[aria-label='Напишите что-нибудь...']").send_keys(text_vk[0])
        except:
            print(f'ОШИБКА ВВОДА ТЕКСТА ВК ГРУППЕ МАГАЗИН ')

        # вводит фото
        try:
            time.sleep(b)
            driver.find_element(By.XPATH, "//label[contains(@class, 'vkuiButton')]").click()
            time.sleep(b)
            propis_ssilki()
            time.sleep(b)
        except:
            print(f'ОШИБКА ВВОДА КАРТИНКИ ВК ГРУППЕ МАГАЗИН ')
        # жмет кнопку опубликовать
        try:
            driver.find_element(By.XPATH,
                                "//span[@class='vkuiButton__content' and text()='Далее']").click()
            time.sleep(b)
            driver.find_element(By.XPATH,
                                "//span[@class='vkuiButton__content' and text()='Опубликовать']").click()
            time.sleep(b)
        except:
            print(f'НЕ НАЖАЛ ОПУБЛИКОВАТЬ ВК ГРУППЕ МАГАЗИН ')
    except:
        print(f'НЕ ОПУБЛИКОВАЛ ВК ГРУППЕ МАГАЗИН ')


def vichod_iz_vk(name):
    try:
        driver.find_element(By.ID, 'top_profile_link').click()
        time.sleep(a)
        # КНОПКА ВЫЙТИ
        driver.find_element(By.XPATH, "//span[contains(text(), 'Выйти')]").click()
        time.sleep(a)
        # НАЖИМАЕТ ПОЛЗУНОК
        driver.find_element(By.CLASS_NAME, 'vkuiSwitch__inputFake').click()
        time.sleep(a)
        # ВЫХОДИТ
        driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Выйти')]]").click()
        time.sleep(b)
        try:
            """ДЛЯ ВЫХОДА В ДРУГОЙ АККАУНТ"""
            time.sleep(a)
            driver.find_element(By.XPATH, "//span[contains(text(), 'Войти в другой аккаунт')]").click()
            time.sleep(b)
        except:
            time.sleep(a)
    except:
        print(name + 'Не вышел ,не получилось!')


# _________________ВКОНТАКТЕ КОНЕЦ______________


# _________________ИНСТАГРАММ НАЧАЛО (СМЕНА ПРОКСИ,СЕЛЕНИУМ ВИРЕ)______________
def otpravka_post_instagram(login, parol):
    """ОТКРЫВАЕТ НОВЫЙ ДРАЙВЕР И МЕНЯЕТ ПРОКСИ"""
    try:
        '''Selenium Wire ЛОГИН И ПАРОЛЬ ОТ ПРОКСИ , САМ ПРОКСИ ПРОПИСЫВАЕТСЯ ЧУТЬ НИЖЕ'''
        from seleniumwire import webdriver
        proxy_username = 'Y'
        proxy_password = ''
        seleniumwire_options = {
            'proxy': {
                'http': f'http://{proxy_username}:{proxy_password}@100.100.27.50:47090',
                'verify_ssl': False,
            },
        }
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  seleniumwire_options=seleniumwire_options)
    except:
        print('ИНСТАГРАМ СМЕНА ПРОКСИ ОШИБКА')
    """РЕГИСТРИРУЕТСЯ В ИНСТАГРАМ ,НУЖНО УКАЗЫВАТЬ ЛОГИН И ПАРОЛЬ"""
    try:
        driver.get("https://www.instagram.com/")
        driver.maximize_window()
        time.sleep(a)
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Телефон, имя пользователя или эл. адрес"]').send_keys(login)
        time.sleep(a)
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Пароль"]').send_keys(parol)
        time.sleep(a)
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    except:
        print('ИНСТАГРАМ РЕГИСТРАЦИЯ ОШИБКА')
    """ВЫКЛАДЫВАЕТ ПОСТ В ИНСТАГРАМ"""
    try:
        time.sleep(inst)
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Новая публикация"]').click()
        time.sleep(inst)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Публикация')]").click()
        time.sleep(inst)
        # ВЫБЕРАЕМ ФОТО
        driver.find_element(By.XPATH,
                            "//button[contains(text(), 'Выбрать на компьютере')]").click()
        time.sleep(a)
        propis_ssilki()
        time.sleep(inst)
        # ЗАГРУЗКА ФОТОГРАФИИ
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Выбрать размер и обрезать"]').click()
        time.sleep(a)
        # РАЗМЕР 4:5
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Значок обрезки в портной ориентации"]').click()
        time.sleep(a)
        # ДАЛЕЕ, ДАЛЕЕ 2
        driver.find_element(By.XPATH, "//div[contains(text(), 'Далее')]").click()
        time.sleep(a)
        driver.find_element(By.XPATH, "//div[contains(text(), 'Далее')]").click()
        time.sleep(a)
        # ВВОД ТЕКСТА
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Добавьте подпись…"]').send_keys(
            text[
                0] + '#возду')
        time.sleep(a)
        driver.find_element(By.XPATH, "//div[contains(text(), 'Поделиться')]").click()
        time.sleep(inst)
        print('ИНСТАГРАМ ОТПРАВКА ПОСТА ВЫПОЛНЕНО')
        driver.quit()
    except:
        print('ИНСТАГРАМ ОТПРАВКА ПОСТА ОШИБКА')


# _________________ИНСТАГРАММ КОНЕЦ______________


if __name__ == "__main__":
    nashalo_koda()  # ЗАХОДИТ В ВАТСАП
    zapominaet_soobshenie()  # ЗАХОДИТ В ГРУППУ ВАТСАП ГНОМ СОХРАНЯЕТ ФОТО,ТЕКСТ
    time.sleep(a)
    gruppi_watapp()  # РАССЫЛКА ПО ГРУППАМ ВАТСАП
    time.sleep(a)
    otpravka_ssilki()  # РАССЫЛКА ССЫЛКИ ПО ГРУППАМ ВАТСАП
    time.sleep(a)
    telegram_otpravka_gnom()  # ОТПРАВКА В ТЕЛЕГУ
    time.sleep(a)
    telegram_otpravka_gruppi()  # РАССЫЛКА В ГРУППЫ ТЕЛЕГИ
    time.sleep(a)
    try:
        otkritie_vk()  # ОТКРЫВАЕТ ВКОНТАКТЕ
        time.sleep(a)
        registrazia_vk(login='0', password='',
                       name='')  # ПРОХОДИТ РЕГИСТРАЦИЮ ВК И ЗАПИСЫВАЕТ В ФАЙЛ КУКИ
        time.sleep(a)
        rand()  # ДЕЛАЕТ РАНДОМНЫЙ ТЕКСТ
        time.sleep(a)
        vk_otpravka(Name='', ID='')  # ВЫКЛАДЫВАЕТ ПОСТ ВК АЛЬБИНА ЛИЧНАЯ СТРАНИЦА
        time.sleep(b)
        stories_lishnaya_vk(name_vk='')  # ВЫКЛАДЫВАЕТ СТОРИС НА ЛИЧНОЙ СТРАНИЦЕ
        time.sleep(a)
        vk_otpravka_gruppa_gelev_chari()  # ВЫКЛАДЫВАЕТ ПОСТ ВК ГРУППА ГЕЛИЕВЫЕ ШАРЫ
        time.sleep(a)
        vk_otpravka_gruppa_magaz_gnom()  # ВЫКЛАДЫВАЕТ ПОСТ ВК ГРУППА МАГАЗИН ГНОМ
        time.sleep(a)
        vichod_iz_vk(name='')  # ВЫХОДИТ ИЗ ВК
    except:
        print(' НЕ СРАБОТАЛ ВК')
    try:
        # time.sleep(a)
        # driver.execute_script("window.open('about:blank', 'new tab')")  # ОТКРЫВАЕТ НОВУЮ ВКЛАДКУ
        # time.sleep(a)
        # driver.switch_to.window(driver.window_handles[1])  # АКТИВИРУЕТ НОВУЮ ВКЛАДКУ
        time.sleep(a)
        otkritie_vk()  # ОТКРЫВАЕТ ВКОНТАКТЕ
        time.sleep(a)
        registrazia_vk(login='', password='/p0',
                       name='')  # ПРОХОДИТ РЕГИСТРАЦИЮ ВК И ЗАПИСЫВАЕТ В ФАЙЛ КУКИ
        time.sleep(a)
        rand()  # ДЕЛАЕТ РАНДОМНЫЙ ТЕКСТ
        time.sleep(a)
        vk_otpravka(Name='', ID='')  # ВЫКЛАДЫВАЕТ ПОСТ ВК  ЛИЧНАЯ СТРАНИЦА
        time.sleep(b)
        stories_lishnaya_vk(name_vk='')  # ВЫКЛАДЫВАЕТ СТОРИС НА ЛИЧНОЙ СТРАНИЦЕ
        time.sleep(a)
        vichod_iz_vk(name='')  # ВЫХОДИТ ИЗ ВК
    except:
        print(' НЕ СРАБОТАЛ ВК')
    try:
        # time.sleep(a)
        # driver.execute_script("window.open('about:blank', 'new tab')")  # ОТКРЫВАЕТ НОВУЮ ВКЛАДКУ
        # time.sleep(a)
        # driver.switch_to.window(driver.window_handles[1])  # АКТИВИРУЕТ НОВУЮ ВКЛАДКУ

        time.sleep(a)
        otkritie_vk()  # ОТКРЫВАЕТ ВКОНТАКТЕ
        time.sleep(a)
        registrazia_vk(login='', password='',
                       name='')  # ПРОХОДИТ РЕГИСТРАЦИЮ ВК И ЗАПИСЫВАЕТ В ФАЙЛ КУКИ
        time.sleep(a)
        rand()  # ДЕЛАЕТ РАНДОМНЫЙ ТЕКСТ
        time.sleep(a)
        vk_otpravka(Name='', ID='')  # ВЫКЛАДЫВАЕТ ПОСТ ВК  ЛИЧНАЯ СТРАНИЦА
        time.sleep(b)
        stories_lishnaya_vk(name_vk='')  # ВЫКЛАДЫВАЕТ СТОРИС НА ЛИЧНОЙ СТРАНИЦЕ
        time.sleep(a)
        vichod_iz_vk(name='')  # ВЫХОДИТ ИЗ ВК
    except:
        print(' НЕ СРАБОТАЛ ВК')
    try:
        time.sleep(a)
        otkritie_vk()  # ОТКРЫВАЕТ ВКОНТАКТЕ
        time.sleep(a)
        registrazia_vk(login='', password='',
                       name='')  # ПРОХОДИТ РЕГИСТРАЦИЮ ВК И ЗАПИСЫВАЕТ В ФАЙЛ КУКИ
        time.sleep(a)
        rand()  # ДЕЛАЕТ РАНДОМНЫЙ ТЕКСТ
        time.sleep(a)
        vk_otpravka(Name='', ID='')  # ВЫКЛАДЫВАЕТ ПОСТ ВК  ЛИЧНАЯ СТРАНИЦА
        time.sleep(b)
        stories_lishnaya_vk(name_vk='')  # ВЫКЛАДЫВАЕТ СТОРИС НА ЛИЧНОЙ СТРАНИЦЕ
        time.sleep(a)
        vichod_iz_vk(name='')  # ВЫХОДИТ ИЗ ВК
    except:
        print(' НЕ СРАБОТАЛ ВК')

    #

    """Погода"""
    pusk_GisMeteo()
    time.sleep(a)
    parsing_GisMeteo()
    vivod()
    """конец Погоды"""
    driver.close()
    driver.quit()
    os.remove('SEM.jpg')  # удаляет фото
