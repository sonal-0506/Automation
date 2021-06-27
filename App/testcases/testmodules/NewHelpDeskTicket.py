from .TestModule import *
from extralibs.helpers import take_screenshot_and_browserlog
from extralibs.helpers import start_recording
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from datetime import date
from sys import exit
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.common.action_chains import ActionChains


class NewHelpDeskTicketTest(TestModule):
	def __init__(self, companycode, employeeCode, password, ticketID):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		#self.mobile = mobile
		self.ticketID = ticketID
		#self.com = com
		ModuleName = "NewHelpDeskTicketTest"
		ModuleDesc = "Test for NewHelpDeskTicket"
		super().__init__(ModuleName, ModuleDesc)
		# extra properties goes here

	def runtest(self, browser, device_logger):
		start_recording(browser)
		today = datetime.today()
		startTime = datetime.now()
		browser.reset()
		print(startTime)
		#sleep(4)

		try:
			#switch context to web view
			web = browser.contexts[1]
			browser.switch_to.context(web)
			sleep(2)
		except:
			print('unable to switch context')

		try:
			#capturing company code textbox button
			#var = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "cancel_callback_h")))
			var = browser.find_element_by_class_name("cancel_callback_h")
			sleep(2)
			var.click()
			#input_field.send_keys(Keys.RETURN)
			device_logger.logging.info('captured new in this realease')
		except:
			device_logger.logging.error('Not captured new in this realease')

		try:
			#capturing company code textbox button
			var = browser.find_element_by_id("TxtCompanyCode")
			sleep(2)
			var.clear()
			var.send_keys(self.companycode)
			#input_field.send_keys(Keys.RETURN)
			device_logger.logging.info('captured company code textbox')
		except:
			device_logger.logging.error('Not captured company code textbox')

		try:	
			#capturing companycode submit button
			var = browser.find_element_by_id("proceedWithCompanyCode")
			sleep(2)
			var.click()
			device_logger.logging.info('captured company code submit button')
		except:
			device_logger.logging.error('Not captured company code submit button')

		try:	
			#capturing employeecode textfield
			var = browser.find_element_by_id("employeeCode")
			sleep(2)
			var.clear()
			print("aaaaaaaaaaaaaa")
			var.send_keys(self.employeeCode)
			#input_field2.send_keys(Keys.RETURN)
			device_logger.logging.info('captured employeecode textbox')
		except:
			device_logger.logging.error('Not captured employeecode textbox')

		try:	
			#capturing employeepassword field
			var = browser.find_element_by_id("employeePassword")
			sleep(2)
			var.clear()
			var.send_keys(self.password)
			device_logger.logging.info('captured password textbox')
		except:
			device_logger.logging.error('Not captured password textbox')
		
		#input_field3.send_keys(Keys.RETURN) 
		try:
			#capturing login button
			var = browser.find_element_by_css_selector(".user_login_h")
			var.click()
			device_logger.logging.info('captured login button')
		except:
			device_logger.logging.error('Not captured login button')
		
		#sleep(6)

		try:
			menu_button = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "menu_button_click_h")))
			#menu_button = browser.find_element_by_class_name("menu_button_click_h")
			menu_button.click()
			device_logger.logging.info('captured menu button')
		except:
			device_logger.logging.error('Not captured menu button')

		#sleep(6)
		try:
			help_desk = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "help_desk_menu_h")))
			#help_desk = browser.find_element_by_class_name("help_desk_menu_h")
			#sleep(4)
			help_desk.click()
			device_logger.logging.info('captured help desk button')
		except:
			device_logger.logging.error('not captured help desk button')


		sleep(4)

		try:
			# tap on create button
			create_ticket = browser.find_element_by_xpath('//div[@class="slider-item-custom help_desk_status_h"][@data-src="N1"]')
			create_ticket.click()
			device_logger.logging.info('captured reopen ticket button')
		except:
			device_logger.logging.info('not captured reopen ticket button')

		#sleep(2)

		try:
			ticket_id = self.ticketID #"22534" #"22533" #"22532" #input("Enter ticket ID : ")
			ticket_chosen = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, ticket_id)))
			#ticket_chosen = browser.find_element_by_xpath('//div[@class="col-12 p-0 card-group support_item ticket_click_h"][@id=ticket_id]')
			#ticket_chosen = browser.find_element_by_id(ticket_id)
			sleep(2)
			ticket_chosen.click()
			device_logger.logging.info('captured ticket element')
		except:
			device_logger.logging.info('not captured ticket element')

		sleep(2)

		try:
			support_query = browser.find_element_by_class_name("support_query_text_h")
			support_query.clear()
			support_query.send_keys("Okay")
			device_logger.logging.info('captured support query element')
		except:
			device_logger.logging.info('not captured support query element')

		#sleep(2)

		try:		
			sub_category = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "send_query_h")))
			#sub_category = browser.find_element_by_class_name("send_query_h")
			sub_category.click()
			device_logger.logging.info('captured send query icon')
		except:
			device_logger.logging.info('not captured send query icon')

		
			"""
			print(current_Time)	

			take_screenshot_and_browserlog(browser, device_logger, self.Name)
			self.writexlslogsln({
				'Status':'Failed',
				'Reason':'Cannot send query the request',
				'TimeTaken':str(current_Time),
				'SubscriptionName':self.companycode,
				'EmployeeCode':self.employeeCode
			})
			
			return False;
			"""
		#sleep(4)

		try:
			success = WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
			#browser.find_element_by_class_name("close_h")
			success.click()
			"""
			var = browser.find_element_by_css_selector('button.close_h')
			sleep(2)
			if var.is_displayed():
				if var.is_enabled():
					var.click()
			#var.click()
			"""
			device_logger.logging.info('captured okay button')
		except:
			device_logger.logging.info('not captured okay button')
			current_Time = datetime.now() - startTime
			print('not captured okay button')
			take_screenshot_and_browserlog(browser, device_logger, self.Name)
			self.writexlslogsln({
				'Status':'Failed',
				'Reason':'Cannot update the request',
				'TimeTaken':str(current_Time),
				'SubscriptionName':self.companycode,
				'EmployeeCode':self.employeeCode
			})
			
			device_logger.logging.error("########NewHelpDeskTicket Failed########")
			browser.close_app()
			return False
			

		sleep(4)
		
		current_Time = datetime.now() - startTime
		print(current_Time)	

		take_screenshot_and_browserlog(browser, device_logger, self.Name)
		self.writexlslogsln({
			'Status':'Pass',
			'Reason':self.ticketID +' successfully updated',
			'TimeTaken':str(current_Time),
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
		
		device_logger.logging.info("########NewHelpDeskTicket done successful########")
		#browser.close_app()
		return True;
		
