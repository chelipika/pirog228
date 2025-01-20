import requests
from time import sleep as sl
from user_agents import user_agent_list
from random import randint
import random

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

# --- Proxy Management ---
def get_proxies(proxy_file="proxies.txt"):
    """
    Reads a list of proxies from a file (one proxy per line).
    Format: http://IP:PORT or http://USERNAME:PASSWORD@IP:PORT (and https://)

    Args:
        proxy_file (str): Path to the proxy file.

    Returns:
        list: A list of proxy dictionaries.
    """
    proxies = []
    try:
        with open(proxy_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    if line.startswith('http://') or line.startswith('https://'):
                        proxy = {
                            'http': line if line.startswith('http://') else None,
                            'https': line if line.startswith('https://') else None
                        }
                        proxies.append(proxy)
                    else:
                        print(f"Invalid proxy format: {line}")
    except FileNotFoundError:
        print(f"Error: Proxy file '{proxy_file}' not found.")
    print(proxies)
    return proxies

def get_random_proxy(proxies):
    """
    Selects a random proxy from the list.

    Args:
        proxies (list): A list of proxy dictionaries.

    Returns:
        dict: A randomly chosen proxy dictionary.
    """
    if proxies:
      return random.choice(proxies)
    else:
      return None

# --- Main loop ---

#Load proxies from file
proxies = get_proxies()

for person in loggins:
    session = requests.Session() # Create a new session for each login
    
    # Choose a random proxy
    proxy = get_random_proxy(proxies)
    if proxy:
      print(f"Using proxy: {proxy['http']}") 

    # Log in
    head = {'User-Agent': random.choice(user_agent_list)} #Correct way to use User-Agent
    try:
        response = session.post(url, data=person, headers=head, proxies=proxy, timeout=10) # Add proxy and timeout
        print(f'Статус входа для {person["login"]}:', response.status_code)

        # Open "Дневник"
        response = session.get(diary_url, headers=head, proxies=proxy, timeout=10)
        print(f'Открыть статус "Дневник" для {person["login"]}:', response.status_code)

        # Log out
        response = session.get(logout_url, headers=head, proxies=proxy, timeout=10)
        print(f'Статус выхода для {person["login"]}:', response.status_code)
    
    except requests.exceptions.RequestException as e:
        print(f"Error for {person['login']}: {e}")

    # Wait 5 seconds before next login
    sl(5)
