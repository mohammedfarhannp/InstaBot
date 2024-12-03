# InstaBot GUI Application
GUI Application for InstaBot. InstaBot is tool to retrive user information from Instagram social media platform. InstaBot can be used to look up details of user either by providing a username or a userid.

## Functionality of GUI Application
1. Search by username or userid
2. Save the retrived result to file named as the *userid.txt*
3. Download the user's posts if user account is public

## About the GUI Application
This GUI Application is created using *tkinter* module, This application asks user for user's Instagram credentials, this creds are used to login to the user account each time the user tries to get a target's information. This step is necessary as Instagram redirect the requests without login to login page causing errors. The password is masked with *stdiomask* third party module at the time of input.

This Application also makes use of multithreading through a built-In module of python namely *threading* so that the button functions can run in the background not freezing the application.

*instaloader* is the third party module used for interacting with Instagram through command line interface making all the logging in and getting user details possible.

*pyshortener* third party module is used to shorten URLs, like the image URL of profile pictures of users are shortened by this module.

## Disclaimer
This is an amazing tool which is not to be used for malicious purposes. I am not responsible for any damages or crimes commited by use of this piece of code. Be safe and responsible. Your actions do have consequences.

## Usage
1. First install required modules, `pip3 install -r requirements.txt`.
2. To use the script `python main.py` or `python3 main.py`.
3. Enter your Instagram Credentials.
4. Enjoy the GUI Application of InstaBot.

### Screenshot of GUI Application
![Screenshot](https://github.com/mohammedfarhannp/InstaBot/blob/master/imgs/Screenshot.png)
