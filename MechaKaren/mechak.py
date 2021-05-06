from requests.exceptions import HTTPError
import requests
from colorama import Fore, Back, Style
import io

# --------------------------------------------------------

key = None

# --------------------------------------------------------

def config(api_key):
        global key
        key = api_key

# --------------------------------------------------------

def chatbot(message):
    if key is None:
        return print(Fore.RED + 'ERROR: You have not specified an API Key! Get one at https://api.mechakaren.xyz.' + Style.RESET_ALL)
    else:
        lol = requests.post(
            "https://api.mechakaren.xyz/v1/chatbot",
            headers = {'Authorization': key},
            json = {'message': message}
        )
    one = lol.json()
    if lol.status_code == 400:
        return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
    if lol.status_code == 404:
        return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
    if lol.status_code == 401:
        return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
    if lol.status_code == 405:
        return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
    if lol.status_code == 429:
        return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
    else:
        last = one['response']['answer']
        return(last)

# --------------------------------------------------------

def anime(category):
    if key is None:
        return print(Fore.RED + 'ERROR: You have not specified an API Key! Get one at https://api.mechakaren.xyz.' + Style.RESET_ALL)
    else:
        lol = requests.get(
            f"https://api.mechakaren.xyz/v1/anime?category={category}",
            headers = {'Authorization': key})
        one = lol.json()
        if lol.status_code == 400:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 404:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 401:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 405:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 429:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        else:
            final = one['data'][0]
            return(final.replace('\\', ''))

# --------------------------------------------------------

def math(equation):
    if key is None:
        return print(Fore.RED + 'ERROR: You have not specified an API Key! Get one at https://api.mechakaren.xyz.' + Style.RESET_ALL)
    else:
        lol = requests.post(
            "https://api.mechakaren.xyz/v1/math",
            headers = {'Authorization': key},
            json = {'equation': equation}
        )
        one = lol.json()
        if lol.status_code == 400:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 404:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 401:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 405:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 429:
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        else:
            last = one['Results']['Output']
            return(last)

# --------------------------------------------------------

def return_img(data):
    return io.BytesIO(data)

# --------------------------------------------------------

def image(filter_type, image_url):
    if key is None:
        return print(Fore.RED + 'ERROR: You have not specified an API Key! Get one at https://api.mechakaren.xyz.' + Style.RESET_ALL)
    else:
        lol = requests.post(
            f"https://api.mechakaren.xyz/v1/image?filter={filter_type}",
            headers = {'Authorization': key},
            json = {"image_url": image_url}
        )
        if lol.status_code == 400:
            one = lol.json()
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 404:
            one = lol.json()
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 401:
            one = lol.json()
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 405:
            one = lol.json()
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        if lol.status_code == 429:
            one = lol.json()
            return print(Fore.RED + 'API Raised an Exception: %s' % (one['error']) + Style.RESET_ALL)
        else:
            image = lol.content
            _bytes = return_img(image)
            return _bytes

# --------------------------------------------------------

import random
import string


# --------------------------------------------------------

def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# --------------------------------------------------------

def save_filter_image(filter_responce=None):
    if filter_responce == None:
        return print(Fore.RED + 'ERROR: Please add a filter output.' + Style.RESET_ALL)
    else:
        pass
        kek = get_random_string(15)
        open(f"img-{kek}.png", 'wb').write(filter_responce.read())

# --------------------------------------------------------
