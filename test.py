from requests import head
from bs4 import BeautifulSoup
import requests
import json
from utils.get_csrf import get_csrf
from utils.Auth_session import Auth_login_session
from utils.Load_json import Load_json

LOGIN_URL = 'https://codeforces.com/enter?back=%2F'
session_obj=requests.Session()


def Auth_login():
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    response = requests.get(LOGIN_URL, headers=headers, verify=False)

    headers['Cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
    headers['content-type'] = 'application/x-www-form-urlencoded'
    
    csrf_token=get_csrf(response)
    if  csrf_token== None:
        return "No CSRF token has been found"
    login_creds=Load_json("cred.json")
    print(login_creds['username'],login_creds['password'])

    new_payload={
        "csrf_token":csrf_token,
        "action":"enter",
        "ftaa":"gnqqqx99q9h5a60oik",
        "bftaa":"10664068841c4f6b8b67418eef2cfeed",
        "handleOrEmail":login_creds['username'],
        "password":login_creds['password'],
        "_tta":"516"
    }
    
    headers['Cookie']+=";lastOnlineTimeUpdaterInvocation=1666273534853;X-User=; X-User-Sha1="
    print(headers['Cookie'])
    response = requests.post(LOGIN_URL, data=new_payload, headers=headers, verify=False)
    # headers['cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
    for x in response.cookies:
        print(x)
    return response.text
def Auth_login_session():
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    response = session_obj.get(LOGIN_URL, headers=headers, verify=False)

    #headers['Cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
    headers['content-type'] = 'application/x-www-form-urlencoded'
    
    csrf_token=get_csrf(response)
    if  csrf_token== None:
        return "No CSRF token has been found"
    login_creds=Load_json("cred.json")
    print(login_creds['username'],login_creds['password'])

    new_payload={
        "csrf_token":csrf_token,
        "action":"enter",
        "ftaa":"gnqqqx99q9h5a60oik",
        "bftaa":"10664068841c4f6b8b67418eef2cfeed",
        "handleOrEmail":login_creds['username'],
        "password":login_creds['password'],
        "_tta":"516"
    }
    
    #headers['Cookie']+=";lastOnlineTimeUpdaterInvocation=1666273534853;X-User=; X-User-Sha1="
    #print(headers['Cookie'])
    response = session_obj.post(LOGIN_URL, data=new_payload, headers=headers, verify=False)
    # headers['cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
    for x in response.cookies:
        print(x)
    return response.text


def Load_json(filepath):
    """
    return none if the file is empty
    or parsed json in python dictionary
    """
    f = open(filepath)
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        "The file is either empty or not json file"
        return None

    return data

def test():
    test_url="https://codeforces.com/"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    headers['Cookie']="JSESSIONID=1C79D99688C569A727C47CDB57699E1C-n1; 39ce7=CFaPMC5Z;"

    response = requests.get(test_url, headers=headers, verify=False)
    print(response.text)
"""
cookies that are required
* JSESSIONID
* 39ce7(given at time of login)
* X-User-Sha1
* lastOnlineTimeUpdaterInvocation
* X-User(should be empty for now)
* evercookie_etag
* evercookie_cache
* evercookie_png
* 70a7c28f3de
"""
print(Auth_login_session())