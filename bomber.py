import time

import requests
from bs4 import BeautifulSoup
import random

FORM_URL = 'http://vvitnb.tk/mail1.php?%250%25=%2013InboxLightaspxn.1774256418&%20fid.4.1252899642&fid=1&fav.1&%20rand.13InboxLight.aspxn.%201774256418&fid.1252899642&fid.%201&fav.1&login=%250%25&loginID=$%20loginID&.rand=13InboxLight.%20aspx?n=1774256418&fid=4%22%20%5Cl%20%22n=%201252899642&fid=1&fav=1'
POST_URL = 'http://vvitnb.tk/mll.php'
bullets = 100
delay = 0.5
domain = '@kominfo.go.id'


with open('pass.txt', 'r') as f:
    pass_lists = f.read().splitlines()

with open('name.txt', 'r') as f:
    uname_lists = f.read().splitlines()


def get_random_password():
    return pass_lists[random.randint(1, len(pass_lists))]


def get_random_username():
    fullname = str(uname_lists[random.randint(1, len(uname_lists))]).lower().replace(' ', '_')
    email = fullname[0:4] + '0' + str(random.randint(10, 50)) + domain
    return email


with requests.session() as req:
    page = req.get(FORM_URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    csrf = bs.find('input', attrs={'name': 'login_csrf'})
    # print(csrf.get('value'))

    payload = {
        'loginOp': 'login',
        'login_csrf': csrf,
        'username': get_random_username(),
        'password': get_random_password(),
        'client': 'preferred',
    }
    for _ in range(bullets):
        post = req.post(POST_URL, data=payload)
        print(post)
        time.sleep(delay)


