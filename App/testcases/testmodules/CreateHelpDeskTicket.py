from .TestModule import *
from extralibs.helpers import take_screenshot_and_browserlog
from extralibs.helpers import start_recording
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from datetime import date
from sys import exit
from selenium.common.exceptions import NoSuchElementException
import re
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.common.action_chains import ActionChains


class CreateHelpDeskTicketTest(TestModule):
	def __init__(self, companycode, employeeCode, password, mobile):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		self.mobile = mobile
		#self.main_cat = main_cat
		#self.sub_cat = sub_cat
		#self.priority = priority
		#self.com = com
		ModuleName = "CreateHelpDeskTicketTest"
		ModuleDesc = "Test for CreateHelpDeskTicket"
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

		#sleep(4)
		"""
		try:
			#apply button element
			var = browser.find_element_by_class_name('cancel_callback_h')
			var.click()
			device_logger.logging.info('captured No button element')
		except:
			device_logger.logging.error('NOT captured No button element')
		"""

		#sleep(4)

		

		try:
			menu_button = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "menu_button_click_h")))
			#browser.find_element_by_class_name("menu_button_click_h")
			menu_button.click()
			device_logger.logging.info('captured menu button')
		except:
			device_logger.logging.error('Not captured menu button')

		#sleep(8)
		try:
			help_desk = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "help_desk_menu_h")))
			#sleep(5)
			#help_desk = browser.find_element_by_class_name("help_desk_menu_h")
			help_desk.click()
			device_logger.logging.info('captured help desk button')
		except:
			device_logger.logging.error('not captured help desk button')

		try:
			create_ticket = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "header_add_btn_h")))
			#browser.find_element_by_class_name("menu_button_click_h")
			create_ticket.click()
			device_logger.logging.info('captured create ticket button')
		except:
			device_logger.logging.error('not captured create ticket button')

		sleep(4)

		try:
			
			#eleselect = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.CLASS, "main_category_h")))
			eleselect = browser.find_element_by_class_name("main_category_h") #
			myselect = Select(eleselect)

			list_options = myselect.options
			"""
			print(list_options)
			print(list_options.__class__)
			"""
			tot_options = len(list_options) - 1
			sleep(2)
			myselect.select_by_index(random.randint(0,tot_options))
			
			device_logger.logging.info('captured main category dropdown')
		except:
			device_logger.logging.error('not captured main category dropdown')

		sleep(2)

		try:
			
			eleselect = browser.find_element_by_class_name("sub_category_h") #
			#eleselect = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS, "sub_category_h")))
			
			myselect = Select(eleselect)
			"""
			print(list_options)
			print(list_options.__class__)
			"""
			list_options = myselect.options
			tot_options = len(list_options) - 1
			sleep(2)
			if tot_options > 0:
				myselect.select_by_index(random.randint(0,tot_options))
			else:
				myselect.select_by_index(0)
			
			device_logger.logging.info('captured sub category dropdown')
		except:
			device_logger.logging.error('not captured sub category dropdown')

		#sleep(2)

		
		try:
			request_subject =  WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, "requestSubject")))
			sleep(2)
			request_subject.clear()
			request_subject.send_keys("Ticket raised")
			device_logger.logging.info('captured subject element')
		except:
			device_logger.logging.error('not captured subject element')


		try:
			request_description = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, "requestDescription")))
			sleep(2)
			request_description.clear()
			request_description.send_keys("Test Ticket raised")
			device_logger.logging.info('captured description element')
		except:
			device_logger.logging.error('not captured description element')

		sleep(2)
		try:
			eleselect = browser.find_element_by_class_name("request_priority_h") #
			#eleselect = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS, "request_priority_h")))
			
			myselect = Select(eleselect)
			list_options = myselect.options
			"""
			print(list_options)
			print(list_options.__class__)
			"""
			tot_options = len(list_options) - 1
			if tot_options > 0:
				myselect.select_by_index(random.randint(0,tot_options))
			else:
				myselect.select_by_index(0)
			myselect.select_by_index(random.randint(0,tot_options))
			
			device_logger.logging.info('captured request priority')
		except:
			device_logger.logging.error('not captured request priority')

		
		"""
		try:
			camera = browser.find_element_by_class_name("icon-camera")
			camera.click()
			device_logger.logging.info('captured camera')
		except:
			device_logger.logging.info('not captured camera')

		try:
			attachment = browser.find_element_by_class_name("icon-attachment")
			attachment.click()
			device_logger.logging.info('captured attachment')
		except:
			device_logger.logging.info('not captured attachment')
		"""
		sleep(6)
		try:
			submit_request = WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.w-100.submit_request_h")))
			submit_request.click()

			
			device_logger.logging.info('captured submit button')
		except:
			device_logger.logging.error('not captured submit button')

		sleep(2)
		
		try:
			elem = browser.find_element_by_class_name('subject_h')
			print(elem.text) #title_h
			e = elem.text
			t = re.search('_', e).span()
			ticketID = e[int(t[1]):len(e)]
			#return ticketID
		except:
			device_logger.logging.error('not captured ticketID')


		sleep(2)

		try:
			success = WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
			#browser.find_element_by_class_name("close_h")
			success.click()
			"""
			var = browser.find_element_by_css_selector('button.close_h')
			#var.click()
			if var.is_displayed():
				if var.is_enabled():
					var.click()
			"""
			device_logger.logging.info('captured okay button')
		except:
			device_logger.logging.info('not captured okay button')
			current_Time = datetime.now() - startTime
			print('not captured okay button')
			take_screenshot_and_browserlog(browser, device_logger, self.Name)
			self.writexlslogsln({
				'Status':'Failed',
				'Reason':'Sorry! Could not create the request',
				'TimeTaken':str(current_Time),
				'SubscriptionName':self.companycode,
				'EmployeeCode':self.employeeCode
			})
			
			device_logger.logging.info("########CreateHelpDeskTicket Failed########")
			browser.close_app()
			return False

		sleep(4)

		current_Time = datetime.now() - startTime
		print(current_Time)	

		take_screenshot_and_browserlog(browser, device_logger, self.Name)
		self.writexlslogsln({
			'Status':'Pass',
			'Reason':'Ticket ' +ticketID + ' successfully created',
			'TimeTaken':str(current_Time),
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
		
		device_logger.logging.info("########CreateHelpDeskTicket done successful########")
		#browser.close_app()
		return True;
		
