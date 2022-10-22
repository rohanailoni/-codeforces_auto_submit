from requests import head
from bs4 import BeautifulSoup
import requests
import json
from utils.get_csrf import get_csrf
from utils.Auth_session import Auth_login_session
from utils.Load_json import Load_json
from utils.dump import dump_session
from utils.load import load_session
import pickle
import os

here = os.path.dirname(os.path.abspath(__file__))


s=requests.Session()
print(Auth_login_session(s))
print(s.cookies)

dump_session(s,"session")

# s=load_session("session")
# print(s.cookies)