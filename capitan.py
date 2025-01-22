import requests
from time import sleep
from random import choice

# Add a comprehensive list of user agents
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/91.0",
    # Add more user agents here
]

loggins = [
    {'login': "zhasurpirmatov", 'password': "7*2iYQFq@M+zFRq"},
    {'login': 'barnokhonmetinova', 'password': '123456#'},
    {'login': 'abdurakhimkaiumov', 'password': 'uchenik7v'},
    {'login': 'khusniddinkazakov', 'password': '123456#'},
    {'login': 'mirzarakhmatovam', 'password': 'uchenik7v'},
    {'login': 'muslimafaizullaeva20', 'password': '12345678'},
    {'login': 'mustafobekibrokhimov', 'password': 'mustafo11V'},
    {'login': 'zliumova', 'password': 'uchenik7v'},
    {'login': 'shokhsanamisomiddino', 'password': 'uchenik7v'},
    {'login': 'sharipov_sherzodbek', 'password': '123456#'}
]

url = 'https://login.emaktab.uz/login'
logout_url = 'https://login.emaktab.uz/logout'
diary_url = 'https://emaktab.uz/marks'

session = requests.Session()

for person in loggins:
    # Log in
    headers = {'User-Agent': choice(user_agent_list)}
    print(f"Attempting login for {person['login']}...")

    response = session.post(url, data=person, headers=headers)

    # Detect CAPTCHA by checking response content
    if "captcha" in response.text.lower() or "Введите символы с картинки" in response.text:
        print(f"CAPTCHA detected for {person['login']}. Login halted.")
        continue

    if response.status_code == 200 and "logout" in response.text:
        print(f"Login successful for {person['login']}.")
    else:
        print(f"Login failed for {person['login']}. Response code: {response.status_code}")
        continue

    # Open "Дневник"
    response = session.get(diary_url, headers=headers)
    print(f"Open 'Дневник' status for {person['login']}: {response.status_code}")
    sleep(5)

    # Log out
    response = session.get(logout_url, headers=headers)
    print(f"Logout status for {person['login']}: {response.status_code}")
    sleep(5)
