import os
BASE = os.path.dirname(os.path.abspath(__file__))

appName = os.getenv("appName") or "live_testing.apk"
appPath = os.path.abspath(os.path.join(BASE,"../apps",appName))


desired_cap = {
  "deviceName": os.getenv("deviceName") or "emulator-5554",
  "platformName": os.getenv("platformName") or "Android",
  "appPackage": os.getenv("appPackage") or "com.zinghr.app",
  "appWaitActivity": os.getenv("appWaitActivity") or "com.zinghr.app.MainActivity",
  "appActivity": os.getenv("appActivity") or "MainActivity",
  "automationName": os.getenv("automationName") or "UiAutomator2",
  "autoWebview": True,
  #"adbExecTimeout": 0,
  "autoGrantPermissions": "true",
  "chromeOptions": {'w3c': False},
  "chromedriverExecutable": (os.getenv("chromedriverExecutable") and os.path.abspath(os.getenv("chromedriverExecutable"))) or os.path.abspath("../chromedriver/win/chromedriver86.exe")
}

print("Running app ", os.getenv("appPackage"))
if(os.getenv("appPath")=='true'):
	desired_cap["app"] = appPath
	print("From path ", appPath)

if(os.getenv("udid")):
	desired_cap["udid"] = os.getenv("udid")
