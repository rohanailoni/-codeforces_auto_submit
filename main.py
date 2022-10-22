from bs4 import BeautifulSoup
import requests
import json
from utils.get_csrf import get_csrf
from utils.Auth_session import Auth_login_session
from utils.Load_json import Load_json
from utils.dump import dump_session
from utils.load import load_session
import pickle
from bs4 import BeautifulSoup
LOGIN_URL = 'https://codeforces.com/enter?back=%2F'
CONTEST_LINK="https://codeforces.com/contest/1749"
SUBMIT_URL="https://codeforces.com/contest/1742/submit"




s=load_session("session")
res=s.get(SUBMIT_URL)
soup = BeautifulSoup(res.text, 'lxml')
# print(soup.find("form").find_all("input",recursive=False))
all_inputs=soup.find_all("input")

for x in all_inputs:
    print(type(x))







