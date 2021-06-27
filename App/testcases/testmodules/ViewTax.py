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
import random
#from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.common.action_chains import ActionChains


class ViewTaxTest(TestModule):
	def __init__(self, companycode, employeeCode, password):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		#self.mobile = mobile
		#self.com = com
		ModuleName = "ViewTaxTest"
		ModuleDesc = "Test for ViewTax"
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
			#sleep(2)
			var.clear()
			var.send_keys(self.companycode)
			#input_field.send_keys(Keys.RETURN)
			device_logger.logging.info('captured company code textbox')
		except:
			device_logger.logging.error('Not captured company code textbox')

		try:	
			#capturing companycode submit button
			var = browser.find_element_by_id("proceedWithCompanyCode")
			#sleep(2)
			var.click()
			device_logger.logging.info('captured company code submit button')
		except:
			device_logger.logging.error('Not captured company code submit button')

		try:	
			#capturing employeecode textfield
			var = browser.find_element_by_id("employeeCode")
			#sleep(2)
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
			#sleep(2)
			var.clear()
			var.send_keys(self.password)
			device_logger.logging.info('captured password textbox')
		except:
			device_logger.logging.error('Not captured password textbox')
		
		#input_field3.send_keys(Keys.RETURN) 
		sleep(2)
		try:
			#capturing login button
			var = browser.find_element_by_css_selector(".user_login_h")
			var.click()
			device_logger.logging.info('captured login button')
		except:
			device_logger.logging.error('Not captured login button')
		

		#sleep(8)

		try:
			menu_button = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "menu_button_click_h")))
			#browser.find_element_by_class_name("menu_button_click_h")
			menu_button.click()
			device_logger.logging.info('captured menu button')
		except:
			device_logger.logging.error('Not captured menu button')

		#sleep(6)
		try:
			pay_slip = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "tax_menu_h")))
			#browser.find_element_by_class_name("pay_slips_menu_h")
			pay_slip.click()
			device_logger.logging.info('captured tax button')
		except:
			device_logger.logging.info('not captured tax button')

		#sleep(6)
		
		try:
			summary = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_h")))
			
			summary.click()
		except:
			device_logger.logging.info('not captured summary')
			return False
		
		sleep(2)
		try:
			# tap on create button
			taxYear = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, "taxYear")))
			
			myselect = Select(taxYear)
		
			#myselect.select_by_value("2020-2021") #(str(random.randint(1,12)))
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
			#myselect.select_by_index(random.randint(0,tot_options))
			
			device_logger.logging.info('captured select tax year dropdown')
		except:
			device_logger.logging.info('not captured select tax year dropdown')

		#sleep(8)
		sleep(2)
		try:
			summary_info = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info_h")))
			#browser.find_element_by_class_name('subject_h') #title_h

			summary_info.click()
			device_logger.logging.info('captured summary info button')
		except:
			device_logger.logging.info('not captured summary info button')
			return False

		#sleep(8)
		sleep(2)
		try:
			# tap on create button
			salary = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "salary_h")))
			
			salary.click()

			device_logger.logging.info('captured salary button')
		except:
			device_logger.logging.info('not captured salary button')
			return False

		#sleep(8)
		sleep(2)
		try:
			
			taxYear = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, "taxYear")))
			
			myselect = Select(taxYear)
		
			#myselect.select_by_value("2020-2021")
			#myselect.select_by_value("2020-2021") #(str(random.randint(1,12)))
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
			#myselect.select_by_index(random.randint(0,tot_options))
			device_logger.logging.info('captured tax year dropdown')
		except:
			device_logger.logging.info('not captured tax year dropdown')

		#sleep(6)
		sleep(2)
		try:
			# tap on create button
			exemption = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "exemption_h")))
			
			exemption.click()

			device_logger.logging.info('captured exemption button')
		except:
			device_logger.logging.info('not ccaptured exemption button')
			return False

		#sleep(2)
		try:
			
			taxYear = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, "taxYear")))
			
			myselect = Select(taxYear)
		
			#myselect.select_by_value("2020-2021")
			#myselect.select_by_value("2020-2021") #(str(random.randint(1,12)))
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
			#myselect.select_by_index(random.randint(0,tot_options))
			
			device_logger.logging.info('captured tax year dropdown')
		except:
			device_logger.logging.info('not captured tax year dropdown')

		sleep(2)
		try:
			# tap on create button
			tax = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "tax_h")))
			
			tax.click()

			device_logger.logging.info('captured exemption button')
		except:
			device_logger.logging.info('not ccaptured exemption button')
			return False

		sleep(2)
		try:
			
			taxYear = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, "taxYear")))
			
			myselect = Select(taxYear)
		
			#myselect.select_by_value("2020-2021")
			#myselect.select_by_value("2020-2021") #(str(random.randint(1,12)))
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
			#myselect.select_by_index(random.randint(0,tot_options))
				
			device_logger.logging.info('captured tax year dropdown')
		except:
			device_logger.logging.info('not captured tax year dropdown')

		sleep(4)

		current_Time = datetime.now() - startTime
		print(current_Time)	

		take_screenshot_and_browserlog(browser, device_logger, self.Name)
		self.writexlslogsln({
			'Status':'Pass',
			'Reason':'View Tax successfully executed',
			'TimeTaken':str(current_Time),
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
		
		device_logger.logging.info("########ViewTax done successful########")
		#browser.close_app()
		return True;
		

