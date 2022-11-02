def Auth_login_session(session_obj,username,password):
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    LOGIN_URL = 'https://codeforces.com/enter?back=%2F'
    response = session_obj.get(LOGIN_URL, headers=headers, verify=False)

    #headers['Cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
    headers['content-type'] = 'application/x-www-form-urlencoded'
    
    csrf_token=get_csrf(response)
    if  csrf_token== None:
        return "No CSRF token has been found"
    #login_creds=Load_json("cred.json")
    new_payload={
        "csrf_token":csrf_token,
        "action":"enter",
        "ftaa":"gnqqqx99q9h5a60oik",
        "bftaa":"10664068841c4f6b8b67418eef2cfeed",
        "handleOrEmail":username,
        "password":password,
        "_tta":"516"
    }
    
    response = session_obj.post(LOGIN_URL, data=new_payload, headers=headers, verify=False)
    
    
    return response.text







## used for testing purpose
if __name__=="__main__":
    from Load_json import Load_json
    from get_csrf import get_csrf
else:
    from utils.Load_json import Load_json
    from utils.get_csrf import get_csrf