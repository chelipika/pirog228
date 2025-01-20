import requests
from time import sleep as sl
from user_agents import user_agent_list
from random import randint

loggins = [
    {
        'login': "zhasurpirmatov",
        'password': "7*2iYQFq@M+zFRq"
    },
    {
        'login': 'barnokhonmetinova',
        'password': '123456#'
    },
    {
        'login': 'abdurakhimkaiumov',
        'password': 'uchenik7v'
    }
]


url = 'https://login.emaktab.uz/login'
logout_url = 'https://login.emaktab.uz/logout'
diary_url = 'https://emaktab.uz/marks'

session = requests.Session()

for person in loggins:
    # Log in
    head = {'User-Agent': user_agent_list[randint(0,11)]}
    print(head)
    response = session.post(url, data=person, headers=head)
    print(f'Статус входа для {person["login"]}:', response.status_code)
    
    # Open "Дневник"
    response = session.get(diary_url, headers=head)
    print(f'Открыть статус "Дневник" для {person["login"]}:', response.status_code)
    sl(5)
    # Log out
    response = session.get(logout_url, headers=head)
    print(f'Статус выхода для {person["login"]}:', response.status_code)
    
    # Wait 5 seconds before next login
