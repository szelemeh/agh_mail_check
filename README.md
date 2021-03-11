# Notifications for poczta.agh.edu.pl

*Currently supports only Windows*

## Setup
1. Download `agh_mail_check` folder
2. Install dependencies with `pip install -r requirements.txt`
3. Download chrome webdriver 
   
   1. Check you chrome browser version by looking at first line of the page: `chrome://version/`
   2. Go to this page: https://chromedriver.chromium.org/downloads and download your version of chrome webdriver.
   3. Unzip .exe file into `agh_mail_check/drivers`

4. Add .env file with content:
    ```
    AGH_MAIL_USERNAME="yourmail@student.agh.edu.pl"
    AGH_MAIL_PASSWORD="yourpassword"
    ```
5. Change `agh_mail_check.bat` file so it correctly points to your stuff.
6. Download https://github.com/stbrenner/SilentCMD to run `agh_email_check.bat` silently.
7. Setup Task Scheduler to run `SilendCMD` with argument as path to `agh_email_check.bat`.