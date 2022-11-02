import imp
from urllib import response
from bs4 import BeautifulSoup
import pickle
import requests
import json


CONTEST_BASE_URL="https://codeforces.com/contest/"
def submit(session,submittedProblemIndex,csrf_token,contestId,_tta,sourceFile,programTypeId=31,source="",tabSize="4",Content_Type="text/x-python"):
    params=Load_json("/home/rohanailoni/Development/ajax/cookies.json")
    print(params)
    ftaa=params["ftaa"]
    bfaa=params["bfaa"]
    filename=sourceFile.split("/")[-1]

    req={
        "csrf_token":csrf_token,
        "ftaa":ftaa,
        "bfaa":bfaa,
        "action":"submitSolutionFormSubmitted",
        "contestId":contestId,
        "submittedProblemIndex":submittedProblemIndex,
        "programTypeId":programTypeId, # 31 for python
        "source":source,
        "tabSize":tabSize,
        "_tta":_tta
    }
    files={
        "sourceFile":(filename,open(sourceFile,"rb"),Content_Type),
    }
    url_to_post=CONTEST_BASE_URL+contestId+"/"+"submit?csrf_token="+csrf_token

    response=session.post(url_to_post,data=req,files=files)
    return response.text
    

def get_submit_template(session,link,filename,problemId):
    link_split=link.split("/")
    contest_Id=link_split[-2]
    response=session.get(link)
    soup=BeautifulSoup(response.text,'lxml')
    req=["csrf_token","ftaa","bfaa","action",]
    al=soup.find_all("input")
    all_the_given_inputs={

    }
    for x in al:
        all_the_given_inputs[x.get("name")]=x.get("value")
    
    res=submit(session,"A",all_the_given_inputs['csrf_token'],contest_Id,_tta="740",sourceFile=filename)
    return res




## used for testing purpose
if __name__=="__main__":
    from Load_json import Load_json
    from load import load_session
    s=load_session("/home/rohanailoni/Development/ajax/session")
    al=get_submit_template(s,"https://codeforces.com/contest/1742/submit","/home/rohanailoni/Desktop/codeforces/round_827/A.py")
else:
    from utils.Load_json import Load_json
    from utils.load import load_session
    


