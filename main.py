#!/usr/bin python
import argparse
import os
from Execptions.Arguments import submitargnotfound,fileargnotfound,problemIdargnotfound,wrongproblemId,userpassrequired
from Execptions.Custom import SessionNotFound
from utils import Auth_session,dump,load,submit
import requests
DEF_PROBLEM_ID="ABCDEFGHIJK" # defualt problem ID's

LOGIN_URL = 'https://codeforces.com/enter?back=%2F'
CONTEST_LINK="https://codeforces.com/contest/"
SUBMIT_URL="https://codeforces.com/contest/{}/submit"
BASE_DIR=os.path.expanduser('~/.config')+"/codeforces"
DEF_SESSION_PATH=BASE_DIR+"/session"
import argparse
# for creating a default config files
def check_config_files():
    BASE_PATH=os.path.expanduser("~/.config")
    BASE_DIR=os.path.join(BASE_PATH,"codeforces")
    
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

check_config_files()




ap = argparse.ArgumentParser(
                    prog = 'codeforces sub',
                    description = 'this is a cli program to auto submit to codeforces',
                    epilog = 'An interactive tool to fast submit your solutions')
# first set of arguments
ap.add_argument("-c", "--contestId",
   help="This argument is required for codefoces contest ID ")

ap.add_argument("-s","--submit",action="store_true",    
   help="this argument is required for weather they have to submit or not")

ap.add_argument("-p","--problemId",action="store",    
   help="the id of problem like A,B,C,D ... as given in the codefoces refernce")

ap.add_argument("-f","--file",action="store",
   help="file path is required must be relative if executable is not global else file path is absolute to the code")

# second set of arguments for handling login 
ap.add_argument("-U","--username",action="store",    
   help="This is for mentioning user name for creation of login")
ap.add_argument("-P","--password",action="store",    
   help="This is password required for login")

args = vars(ap.parse_args())
print(args)
if args["contestId"]!=None:
    if args["file"]==None:
        raise fileargnotfound()
    else:
        if args["problemId"]==None:
            raise problemIdargnotfound()
        elif args["problemId"] not in DEF_PROBLEM_ID:
            raise wrongproblemId(args["problemId"],DEF_PROBLEM_ID)
        else:
            if args["submit"]==False:
                raise submitargnotfound()
            else:
                print("checking if the session folder is present ")
                if(os.path.exists(DEF_SESSION_PATH)==False):
                    raise SessionNotFound()
                else:
                    # all params passed
                    session=load.load_session(DEF_SESSION_PATH)
                    URL=SUBMIT_URL.format(args["contestId"])
                    res=submit.get_submit_template(session,URL,args["file"],args["problemId"])
                    print(res)
else:
    if args["username"]!=None and args["password"]!=None:
        session=requests.Session()
        res=Auth_session.Auth_login_session(session,args["username"],args["password"])
        dump.dump_session(session,DEF_SESSION_PATH)
        
    else:
        raise userpassrequired()

                








