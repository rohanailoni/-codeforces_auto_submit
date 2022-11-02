<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/rohanailoni/Codeforces-Auto-Submit/">
    <img src="https://github.com/rohanailoni/GIT-SDK-TOOLING/blob/main/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Codeforces Auto Submit</h3>

  <p align="center">
    A tool which makes submit to codeforces easier
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rohanailoni/Codeforces-Auto-Submit">View Demo</a>
    ·
    <a href="https://github.com/rohanailoni/Codeforces-Auto-Submit/issues">Report Bug</a>
    ·
    <a href="https://github.com/rohanailoni/Codeforces-Auto-Submit/issues">Request Feature</a>
  </p>
</div>
This is a small kink project where we can submit our code while in codeforces contest from the command line with one click
# installation :-(linux,macos)
## create and activate virtualenv
```bash
virtualenv venv
```

```bash
source venv/bin/activate
```

## Install these 2 modules
```
pip install beautifulsoup4 requests
```

`we have eleminated more dependecy by using  html.parser which is default rather than lxml`

# usage:-

## first of all the steps login using

```bash 
python main.py -U username -P password 
```
### this will login the user and create a session bytes object in `~/.config/codeforces`
## use this to submit the problem
```bash
python main.py -c <contestId> -p <problem Id like A or B> -f <file location> -s
```

### file location should be absolute until we create some executable


# CheckList
- [ ] Create a Javascript Frontend Extension to read problem and its test cases
- [ ] create a local Python server to get info from frontend(use only Socket.io as to decrease dependency on other module also the server is running on a local machine so no security is required to be handled)
	- [ ] creating Async Python server

- [ ] Make all the Below features and all the arguments (use argparse)
	- [x] Create the Login functionality
	- [x] Create submit functionality
	- [x] Creating a get_csrf function to get CSRF from the HTML page
	- [x] Creating a pickle for session so the cookies can be saved as the request.Session object()
	- [ ] A way to Handle errors(Ig this is quite hard as even if there is an error like wrong password the codeforces sends an HTTP 200 but the HTML tags will have the errors)
- [ ] A way to make a executable by wrapping the whole modular code

