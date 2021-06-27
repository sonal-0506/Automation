# Automation
# zing-mobile-testing repository
## NodeApp :
  - Clone this repository first
  - Go to NodeApp folder and run `npm install` on terimnal
  - Create `.env` file in the same folder and put content like this
  
      ```appPath=false
      platformName=Android
      platformVersion=8
      deviceName="Real Device 2"
      appPackage=com.zinghr.app
      appActivity=MainActivity
      appWaitActivity=com.zinghr.app.MainActivity
      chromedriverExecutable="../chromedriver/win/chromedriver80.exe"
  - Enter `npm start` in terminal for testing
  - Add new testing modules in **`testcases/testmodules`** folder see example of `Login.js` file in same folder

## PythonApp :
  - Clone this repository first
  - Go to PythonApp folder create virtual environment by running `virtualenv venv` on terimnal (install virtualenv if not available using `pip install virtualenv`)
  - This will create python virtual environment named as venv, now activate this enviornment it by using commmand `venv\Scripts\activate` for windows and `source venv/bin/activate` for linux/macos
  - Run commmand  `pip install -r requirements.txt` to install python dependencies
  - Create `.env` file in the same folder and put content like this
  
      ```appPath=false
      platformName=Android
      platformVersion=8
      deviceName="Real Device 2"
      appPackage=com.zinghr.app
      appActivity=MainActivity
      appWaitActivity=com.zinghr.app.MainActivity
      chromedriverExecutable="../chromedriver/win/chromedriver80.exe"
  - Enter `python index.py` in terminal for testing
  - Add new testing modules in **`testcases/testmodules`** folder see example of `Login.py` file in same folder
  - Add this entry in **`testcases/testmodules/__init__.py`** file so that it will available on testing scripts

## Installl chromium driver from this [Link](https://chromedriver.storage.googleapis.com/index.html)
