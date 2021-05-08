from requests.exceptions import HTTPError
import requests
from colorama import Fore, Back, Style
import io

key = None

def config(api_key):
        global key
        key = api_key

def chatbot(message):
    if key is None:
        return print(Fore.RED + 'ERROR: You have not specified an API Key! Get one at https://api.mechakaren.xyz.' + Style.RESET_ALL)
    else:
        response = requests.post(
            "https://api.mechakaren.xyz/v1/chatbot",
            headers = {'Authorization': key},
            json = {'message': message}
        )
    json = response.json()
    if not response.ok:
        return print(Fore.RED + 'API Raised an Exception: %s' % (json['error']) + Style.RESET_ALL)
    else:
        answer = json['response']['answer']
        return answer

def anime(category):
        if not key:
                return print(Fore.RED + 'ERROR: You have not specified an API Key! Get one at https://api.mechakaren.xyz.' + Style.RESET_ALL)
        response = requests.get(
                f"https://api.mechakaren.xyz/v1/anime?category={category}",
                headers = {'Authorization': key})
        json = response.json()
        if not response.ok:
                return print(Fore.RED + 'API Raised an Exception: %s' % (json['error']) + Style.RESET_ALL)
        else:
                final = one['data'][0]
                return(final.replace('\\', ''))

def math(equation):
        response = requests.post(
            "https://api.mechakaren.xyz/v1/math",
            json = {'equation': equation}
        )
        json = response.json()
        if not response.ok:
                return print(Fore.RED + 'API Raised an Exception: %s' % (json['error']) + Style.RESET_ALL)

        answer = json['Results']['Output']
        return answer

def return_img(data):
    return io.BytesIO(data)

def image(filter_type, image_url):
    if key is None:
        return print(Fore.RED + 'ERROR: You have not specified an API Key! Get one at https://api.mechakaren.xyz.' + Style.RESET_ALL)
    else:
        response = requests.post(
            f"https://api.mechakaren.xyz/v1/image?filter={filter_type}",
            headers = {'Authorization': key},
            json = {"image_url": image_url}
        )
        json = response.json()
        if not response.ok:
                return print(Fore.RED + 'API Raised an Exception: %s' % (json['error']) + Style.RESET_ALL)
        else:
            image = response.content
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

def save_filter_image(filter_response=None, filename = None):
        if filter_responce == None:
                return print(Fore.RED + 'ERROR: Please add a filter output.' + Style.RESET_ALL)

        filename = filename or get_random_string(15)
        open(f"{filename}.png", 'wb').write(filename.read())
        return filename + '.png'

# --------------------------------------------------------
