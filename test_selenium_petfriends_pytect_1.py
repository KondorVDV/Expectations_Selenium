import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import json

from selenium.webdriver.support.wait import WebDriverWait


def stat_list(a):
    """Преобразование текста статистики в список значений"""
    b = ''

    for i in a:
        if i != ' ':
            b = b+i

    y = b.split('\n')
    return y

def stat_list_1(a):
    b = ''

    for i in a:
        if i != ' ':
            b = b+i

    y = (b.split(':'))[1]
    return y


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\chrome\chromedriver.exe')
    # Переходим на страницу авторизации

    pytest.driver.implicitly_wait(10)



    pytest.driver.get('http://petfriends.skillfactory.ru/login')


    # Вводим email

    pytest.driver.find_element(By.ID, 'email').send_keys('kondorvdv@mail.ru')


    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('Arr65389')


    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


    yield

    pytest.driver.quit()

def test_show_my_pets():
    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()

    """переходим во вкладку "Мои питомцы" """


    r = pytest.driver.find_element(By.XPATH, '/html/head/title')
    title = str(r.get_attribute("textContent"))


    assert title == "PetFriends: My Pets"

def test_were_pets():

    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    time.sleep(1)
    """переходим во вкладку "Мои питомцы" """

    pet = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr')
    quantity_pets = len(pet)
    """Получаем количество питомцев во вкладке мои питомцы"""

    for r in pytest.driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]'):
        pets_stat = stat_list(r.text)
        quantity_pets_stat = stat_list_1(pets_stat[1])
    """Получаем данные из статистики"""

    assert str(quantity_pets) == quantity_pets_stat



def test_pets_foto():

    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    time.sleep(1)
    """переходим во вкладку "Мои питомцы" """

    for r in pytest.driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]'):
        pets_stat = stat_list(r.text)
        quantity_pets_stat = stat_list_1(pets_stat[1])
    """Получаем количество питомцев из статистики пользователя"""


    pets_photos = []
    for pets_foto in pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img'):
        pets_photos.append(pets_foto.get_attribute("src"))
        pets_without_photos = pets_photos.count('')
        """Получаем количество фотографий питомцев во вкладке мои питомцы"""

    assert int(quantity_pets_stat)//2 >= pets_without_photos, "Больше чем у половины питомцев нет фото"


def test_availability_of_pet_data():
    """Проверяем что у всех питомцев есть имя, возраст и порода."""

    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    time.sleep(1)
    """переходим во вкладку "Мои питомцы" """

    for r in pytest.driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]'):
        pets_stat = stat_list(r.text)
        quantity_pets_stat = stat_list_1(pets_stat[1])
    """Получаем количество питомцев из статистики пользователя"""

    pets_names = []
    for pets_data_names in pytest.driver.find_elements(By.XPATH , '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'):
        pets_names.append(pets_data_names.get_attribute("textContent"))
        """Получаем имена питомцев во вкладке мои питомцы"""


    pets_breeds = []
    for pets_data_breeds in pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]'):
        pets_breeds.append(pets_data_names.get_attribute("textContent"))

        """Получаем породы питомцев во вкладке мои питомцы"""

    pets_ages = []
    for pets_data_ages in pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]'):
        pets_ages.append(pets_data_names.get_attribute("textContent"))

        """Получаем возраст питомцев во вкладке мои питомцы"""


    for i in range(len(pets_names)):
        assert pets_names[i] != '', 'Питомец не имеет имени'

    for i in range(len(pets_breeds)):
        assert pets_breeds[i] != '', 'Питомец не имеет породы'

    for i in range(len(pets_ages)):
        assert pets_ages[i] != '', 'Питомец не имеет возраста'

    assert len(pets_names) == len(set(pets_names)), 'У питомцев одинаковые имена'
    """ Проверяем есть ли у питомцев одинаковые имена"""


def test_identical_pets():
    """Проверяем нет ли одинаковых питомцев"""

    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    time.sleep(1)
    """переходим во вкладку "Мои питомцы" """

    pets = []

    n = len(pytest.driver.find_elements(By.XPATH , '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'))
    pets_data = []



    for pet in pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr'):
        pets.append(pet.get_attribute("textContent"))
    for i in range(n):
        a = pets[i]
        b = stat_list(a)
        c = b[2:5]
        pets_data.append(c)

    N = len(pets_data)

    for i in range(N - 1):
        for n in range(i+1, N):
            assert pets_data[i] != pets_data[n], 'Есть одинаковые питомцы!!!'

#
#
#
#
#
#
#
#
