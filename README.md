# Tinder-Autoswiper-Bot

This program is a bot which autoswipes right for you on tinder to save a tinder user's time.

## Structure
- `main.py` runs the entirety of the program and performs the swipes

## Dependencies & Configurations
1. The [Selenium API](https://www.selenium.dev/documentation/webdriver/) is used for logging into Tinder and Swiping to find matches
   - Please retrieve your tinder email and password and enter them into the `tinder_email` & `tinder_password` respectively
   - The number of swipes you wish to perform can be adjustsed by the user with the `NUMBER_OF_SWIPES` variable
   - **NOTE**: There are 2 sections of the program that require the user to manually perform an action. Without performing the below 2 actions the program will not run, hence why ample time has been given for you to click the button and can be adjusted as well with the `WAIT` variables.
       1. After the program clicks login, you must click ***login through google***
       2. After the program has logged into tinder and given location permissions, you must click ***allow tinder to use your location***. This will appear as a popup.
2. This application is only compatible with google chrome and requires you to have the [undetected_chromedriver library](https://stackoverflow.com/questions/59515561/this-browser-or-app-may-not-be-secure-error-while-attempting-to-login-in-to-gm) in order to bypass any security issues.
3. Since this application uses your email, it assumes you have 2FA on. To bypass through, the program uses the [pytop library](https://stackoverflow.com/questions/55870489/how-to-handle-google-authenticator-with-selenium) which retrieves a code from your [google authenticator app](https://letzdotesting.com/how-to-automate-two-factor-authentication-with-google-authenticator-using-selenium/)

4. 
