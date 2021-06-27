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


class ViewCumulativePaySlipTest(TestModule):
	def __init__(self, companycode, employeeCode, password):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		#self.mobile = mobile
		#self.com = com
		ModuleName = "ViewCumulativePaySlipTest"
		ModuleDesc = "Test for ViewCumulativePaySlip"
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
		#sleep(2)
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
			pay_slip = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "pay_slips_menu_h")))
			#browser.find_element_by_class_name("pay_slips_menu_h")
			pay_slip.click()
			device_logger.logging.info('captured pay slip button')
		except:
			device_logger.logging.info('not captured pay slip button')

		#sleep(6)
		try:
			elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
			#browser.find_element_by_class_name('subject_h') #title_h
			print(elem.text)	
				
			if 'No data for the chosen month. Please select another month' in elem.text:
				var = WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
				#browser.find_element_by_css_selector('button.close_h')
				var.click()

		except:
			device_logger.logging.info('not captured subject. Chosen month correct')

		try:
			# tap on create button
			payslipMonth = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.ID, "payslipMonth")))
			
			myselect = Select(payslipMonth)
			
			myselect.select_by_value(str(random.randint(1,12)))
			
			device_logger.logging.info('captured select month dropdown')
		except:
			#print("not captured select month dropdown")
			device_logger.logging.info('not captured select month dropdown')

		#sleep(8)

		try:
			
			elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
			#browser.find_element_by_class_name('subject_h') #title_h
			print(elem.text)	

			try:
				var = WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
				#browser.find_element_by_css_selector('button.close_h')
				var.click()
			except:
				#print("Chosen month has data button")
				device_logger.logging.info('not captured close button')
				
			while('No data for the chosen month. Please select another month' not in elem.text):
				
				#sleep(2)	
				
				print("inside loop")

				sleep(2)

				try:
				# tap on create menu_button
				#element_located_to_be_selected
					payslipMonth = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.ID, "payslipMonth")))
					myselect = Select(payslipMonth)
					myselect.select_by_value(str(random.randint(1,12)))
					device_logger.logging.info('captured select month dropdown')
				except:
					#print("randint")
					device_logger.logging.info('not captured select month dropdown')

				try:
					elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
					#browser.find_element_by_class_name('subject_h') #title_h
					print(elem.text)	
				except:
					device_logger.logging.info('not captured subject. Chosen month has data')

				try:
					var = WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
					#browser.find_element_by_css_selector('button.close_h')
					var.click()
				except:
					device_logger.logging.info('not captured close button')
					#print("Chosen month has data button")

		except:
			#print("Chosen month has data")
			device_logger.logging.info('not captured subject. Chosen month has data')

		#sleep(8)

		try:
			# tap on create button
			payslipYear = WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.ID, "payslipYear")))
			myselect = Select(payslipYear)
			list_options = myselect.options
			
			tot_options = len(list_options) - 1
			if tot_options > 0:
				myselect.select_by_index(random.randint(0,tot_options))
			else:
				myselect.select_by_index(0)
			#myselect.select_by_index(random.randint(0,tot_options))
			device_logger.logging.info('captured select year dropdown')
		except:
			#print("not captured select year dropdown")
			device_logger.logging.info('not captured select year dropdown')

		#sleep(8)


		try:
			elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
			#browser.find_element_by_class_name('subject_h') #title_h
			print(elem.text)	
				
			if 'No data for the chosen month. Please select another month' in elem.text:
				var = WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
				#browser.find_element_by_css_selector('button.close_h')
				var.click()
				
				

		except:
			device_logger.logging.info('not captured subject. Chosen month correct')

		try:
			
			elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
			#browser.find_element_by_class_name('subject_h') #title_h
			print(elem.text)	

			try:

				var = WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
				#browser.find_element_by_css_selector('button.close_h')
				var.click()
			except:
				#print("Chosen month-year has data button")
				device_logger.logging.info('not captured close button')
				
			while('No data for the chosen month. Please select another month' not in elem.text):
				
				#sleep(2)	
				
				#print("inside loop")

				sleep(2)

				try:
					# tap on create button
					payslipYear = WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.ID, "payslipYear")))
					myselect = Select(payslipYear)
					list_options = myselect.options
					
					tot_options = len(list_options) - 1
					if tot_options > 0:
						myselect.select_by_index(random.randint(0,tot_options))
					else:
						myselect.select_by_index(0)
					#myselect.select_by_index(random.randint(0,tot_options))
					device_logger.logging.info('captured select year dropdown')
				except:
					#print("not captured select year dropdown")
					device_logger.logging.info('not captured select year dropdown')

				try:
					elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
					#browser.find_element_by_class_name('subject_h') #title_h
					print(elem.text)	
				except:
					device_logger.logging.info('not captured subject. Chosen month-year has data')

				try:

					var = WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
					#browser.find_element_by_css_selector('button.close_h')
					var.click()
				except:
					#print("Chosen month-year has data button")
					device_logger.logging.info('not captured close button')

		except:
			#print("Chosen month-year has data")
			device_logger.logging.info('not captured subject. Chosen month-year has data')

		
		
		try:
			
			cumulative_download = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "cumulative_payslip_download_h")))
			#browser.find_element_by_class_name("cumulative_payslip_download_h")
			cumulative_download.click()
			device_logger.logging.info('captured download cumulative payslip')
		except:
			device_logger.logging.info('not download cumulative payslip')

		#sleep(8)

		try:
			success = WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.flex-fill.close_h")))
			#browser.find_element_by_class_name("close_h")
			success.click()

			device_logger.logging.info('captured success OKAY element')
		except:
			device_logger.logging.info('not captured success OKAY element')

		#sleep(8)

		try:		
			view_payslip = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.CLASS_NAME, "view_cumulative_payslip_h")))
			#browser.find_element_by_class_name("view_cumulative_payslip_h")
			view_payslip.click()
			device_logger.logging.info('captured view cumulative payslip button')
		except:
			device_logger.logging.info('not captured view cumulative payslip button')
			current_Time = datetime.now() - startTime
			print(current_Time)	

			take_screenshot_and_browserlog(browser, device_logger, self.Name)
			self.writexlslogsln({
				'Status':'Failed',
				'Reason':'File cumulative payslip not downloaded successfully',
				'TimeTaken':str(current_Time),
				'SubscriptionName':self.companycode,
				'EmployeeCode':self.employeeCode
			})
			
			return False;
			
		"""
		sleep(6)

		try:
			var = browser.find_element_by_class_name('back_button_h')
			var.click()
			device_logger.logging.info('captured back button')
		except:
			device_logger.logging.info('not captured back button')
		"""
		sleep(4)

		current_Time = datetime.now() - startTime
		print(current_Time)	

		take_screenshot_and_browserlog(browser, device_logger, self.Name)
		self.writexlslogsln({
			'Status':'Pass',
			'Reason':'View Cumulative Payslip successfully executed',
			'TimeTaken':str(current_Time),
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
		
		device_logger.logging.info("########ViewCumulativePaySlip done successful########")
		#browser.close_app()
		return True;
		

