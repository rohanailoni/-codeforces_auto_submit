# Codeforces-Auto-submit
This is a small kink project where we can submit our code while in codeforces contest from the command line with one click


# CheckList
- [ ] Create a Javascript Frontend Extension to read problem and its test cases
- [ ] create a local Python server to get info from frontend(use only Socket.io as to decrease dependency on other module also the server is running on a local machine so no security is required to be handled)

- [ ] Make all the Below features and all the arguments (use argparse)
	- [x] Create the Login functionality
	- [x] Create submit functionality
	- [x] Creating a get_csrf function to get CSRF from the HTML page
	- [x] Creating a pickle for session so the cookies can be saved as the request.Session object()
	- [ ] A way to Handle errors(Ig this is quite hard as even if there is an error like wrong password the codeforces sends an HTTP 200 but the HTML tags will have the errors)
- [ ] A way to make a executable by wrapping the whole modular code
