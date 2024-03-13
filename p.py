from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time

# Настройки прокси
proxy_host = ''
proxy_port = ''
proxy_username = ''
proxy_password = ''

proxy_options = {
    'proxy': {
        'http': f'socks5://{proxy_host}:{proxy_port}',
        'https': f'socks5://{proxy_host}:{proxy_port}',
    }
}

# Добавляем авторизацию к прокси
if proxy_username and proxy_password:
    proxy_options['proxy']['http'] = f'socks5://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
    proxy_options['proxy']['https'] = f'socks5://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'

# Опции для браузера
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Создаем драйвер с прокси и опциями
driver = webdriver.Chrome(options=chrome_options, seleniumwire_options=proxy_options)
# Данные для входа
login = ''
password = ''

driver.get('https://www.avito.ru/profile/login')

wait = WebDriverWait(driver, 5) 
# Заполнение формы логина и пароля
login_field = driver.find_element(By.NAME, 'login').send_keys(login)
password_field = driver.find_element(By.NAME, 'password').send_keys(password)
login_button = driver.find_element(By.CSS_SELECTOR, "button[data-marker='login-form/submit']").click()

try:
    profile_menu = driver.find_element(By.CSS_SELECTOR, '[data-marker="header/menu-profile"]')
    print('Пользователь успешно залогинился.')
except NoSuchElementException:
    print('Пользователь НЕ залогинился.')
    exit


# Ссылки на Авито
links = [
    'https://www.avito.ru/user/79aa5de4d6b1f4eaecd64c7252a6e1c1/profile?id=3715990635&src=item&page_from=from_item_card&iid=3715990635',
    'https://www.avito.ru/user/32d7c31671a074486af59575ce7e4706/profile?id=3294176303&src=item&page_from=from_item_card&iid=3294176303',
    'https://www.avito.ru/sankt-peterburg/predlozheniya_uslug/remont_telelefonov_zamena_stekla_i_batarei_ayfon_3561289257',
    'https://www.avito.ru/user/b2908c0b02eb8b532388486323d5bf4a/profile?id=2737439285&src=item&page_from=from_item_card&iid=2737439285',
    'https://www.avito.ru/user/32d7c31671a074486af59575ce7e4706/profile?id=3294176303&src=item&page_from=from_item_card&iid=3294176303',
    'https://www.avito.ru/user/6c9eaef885766d2eb8657763c32d5ff0/profile?id=2559827171&src=item&page_from=from_item_card&iid=2559827171',
    'https://www.avito.ru/user/b830b940bb572641673f496e48c5e057/profile?id=3627349274&src=item&page_from=from_item_card&iid=3627349274',
    'https://www.avito.ru/user/81ea3c8b96ab61cc303d7cb320751113/profile?id=0&src=item&page_from=from_item_card&iid=966868345',
    'https://www.avito.ru/user/a89de73e04365ac1acc2d74091f5157a/profile?id=0&src=item&page_from=from_item_card&iid=966916166',
    'https://www.avito.ru/user/1ad086bd1720bd4b2b571f7c1785a74e/profile?id=4130102753&src=item&page_from=from_item_card&iid=4130102753',
    'https://www.avito.ru/user/a8a5ea72524535ff8fdd97864dca8ee2/profile/all/predlozheniya_uslug?id=2888232176&src=item&page_from=from_item_card&iid=2888232176&sellerId=a8a5ea72524535ff8fdd97864dca8ee2'
]

results = []

for link in links:
    time.sleep(3)
    try:
        driver.get(link)
        # Поиск элемента по атрибуту data-marker
        rating_element = driver.find_element(By.CSS_SELECTOR, 'span[data-marker="profile/score"]')
        feedback_element = driver.find_element(By.CSS_SELECTOR, 'a[data-marker="profile/summary"]')

        results.append({
            'rating': rating_element.text,
            'feedback': feedback_element.text
        })
    except Exception as e:
        print(f"Ошибка: {str(e)}")

print(results)

# Закрытие браузера
driver.quit()
