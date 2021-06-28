from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from .config import desired_cap
from datetime import datetime

def InitDriver(logger, command_executor=""):
	driver = webdriver.Remote(
		command_executor = command_executor or "http://localhost:4723/wd/hub",
		desired_capabilities = desired_cap,
		keep_alive = True
	)
	driver.implicitly_wait(30)
	#webview = driver.contexts[1]
	#driver.switch_to.context(webview)
	startTime = datetime.now()
	logger.logging.info("---------------------------------splash screen invoked---------------------------------")
	logger.logging.info(datetime.now() - startTime)
	return driver
	


#switch to webview
#webview = driver.contexts.last
#driver.switch_to.context(webview)