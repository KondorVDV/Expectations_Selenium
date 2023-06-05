from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_checking_pet_cards():
    browse = webdriver.Chrome('C:\chrome\chromedriver.exe')
    browse.implicitly_wait(5)
    '''Устанавливаем неявное ожидание'''
    browse.get('https://petfriends.skillfactory.ru')
    '''Переходим на страницу: https://petfriends.skillfactory.ru'''

    browse.find_element(By.CSS_SELECTOR,'div.text-center button').click()
    '''Нажимаем кнопку Зарегистрироваться'''

    browse.find_element(By.CSS_SELECTOR, 'div.text-center a').click()
    '''Нажимаем на ссылку "У меня уже есть аккаунт"'''

    browse.find_element(By.ID, 'email').send_keys('kondorvdv@mail.ru')
    '''Вводим почту'''
    browse.find_element(By.ID, 'pass').send_keys('Arr65389')
    '''Вводим пароль'''
    browse.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    '''Нажимаем на кнопку "Войти"'''

    browse.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    '''Нажимаем на кнопку "Мои питомцы"'''

    r = browse.find_element(By.XPATH, '/html/head/title')
    title = str(r.get_attribute("textContent"))

    assert title == "PetFriends: My Pets"



def test_pet_friends_add_pet():
    browse = webdriver.Chrome('C:\chrome\chromedriver.exe')
    browse.get('https://petfriends.skillfactory.ru')
    wait = WebDriverWait(browse, 10)

    reg_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.text-center button')))
    '''Дожидаемся появления кнопки зарегистрироваться'''
    reg_button.click()
    '''Нажимаем на кнопку "Зарегистрироваться"'''

    have_an_account = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.text-center a')))
    '''Дожидаемся появления ссылки "У меня уже есть аккаунт"'''
    have_an_account.click()
    '''Нажимаем на ссылку "У меня уже есть аккаунт"'''

    browse.find_element(By.ID, 'email').send_keys('kondorvdv@mail.ru')
    '''Вводим почту'''
    browse.find_element(By.ID, 'pass').send_keys('Arr65389')
    '''Вводим пароль'''
    browse.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    '''Нажимаем на кнопку "Войти"'''

    my_pets = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/my_pets']")))
    '''Дожидаемся появления ссылки на вкладку"Мои питомцы"'''
    my_pets.click()
    '''Нажимаем на кнопку "Мои питомцы"'''

    add_pet = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-8.right.fill div button')))
    '''Дожидаемся появления кнопки "Добавить питомца"'''
    add_pet.click()
    '''Нажимаем на кнопку "Добавить питомца"'''

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#addPetsModal > div > div')))
    '''Дожидаемся появления формы для добавления питомца'''

    browse.find_element(By.ID, 'name').send_keys('Вася')
    browse.find_element(By.ID, 'animal_type').send_keys('Британец')
    browse.find_element(By.ID, 'age').send_keys(1)
    '''Заполняем форму
    '''
    browse.find_element(By.CSS_SELECTOR, 'button.btn.btn-success').click()
    '''Нажимаем на кнопку "Добавить"'''



    pets_names = []

    for name in browse.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'):
        pets_names.append(name.get_attribute("textContent"))
        """Получаем список имен питомцев во вкладке мои питомцы"""


    assert ' Вася ' in pets_names, 'Питомец не добавлен'
    '''Проверяем есть ди имя добавленного питомца в списке имен питомцев'''













