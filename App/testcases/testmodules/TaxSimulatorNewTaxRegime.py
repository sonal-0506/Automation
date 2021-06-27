from .TestModule import *
from extralibs.helpers import take_screenshot_and_browserlog
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
from selenium.webdriver.common.action_chains import ActionChains
import random
import traceback
#from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.common.action_chains import ActionChains


class TaxSimulatorNewTaxRegimeTest(TestModule):
	def __init__(self, companycode, employeeCode, password):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		#self.mobile = mobile
		#self.com = com
		ModuleName = "TaxSimulatorNewTaxRegimeTest"
		ModuleDesc = "Test for TaxSimulatorNewTaxRegime"
		super().__init__(ModuleName, ModuleDesc)
		# extra properties goes here

	def runtest(self, browser, device_logger):
		
		today = datetime.today()
		startTime = datetime.now()
		print(startTime)

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
			tax_sim = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "tax_simulator_menu_h")))
			#browser.find_element_by_class_name("pay_slips_menu_h")
			tax_sim.click()
			device_logger.logging.info('captured tax simulator button')
		except:
			device_logger.logging.info('not captured tax simulator button')

		sleep(15)
		
		try:
			calculate = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.btn-solid.w-100.calculate_tax_h")))
			
			calculate.click()
		except:
			device_logger.logging.info('not captured calculate tax button')
			return False
		
		try:
			sleep(4)
			# tap on create button
			#newTaxRegime = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.ID, "newTaxRegime")))
			#("input[type='radio'][value='SRF']")
			newTaxRegime = browser.find_element_by_id("newTaxRegime")
			#newTaxRegime.click()
			if newTaxRegime.is_selected():
				print("newTaxRegime radio button already selected")
			else:
				newTaxRegime.click()
		
			device_logger.logging.info('captured new Tax Regime radiobutton')
		except Exception as e:
			print(e)
			device_logger.logging.info('not captured new Tax Regime radiobutton')

		#sleep(8)

		try:
			sleep(4)
			#checkTaxRegime = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, "taxRegimeTnCCheckBox")))
			#checkTaxRegime=WebDriverWait(browser,4).until(EC.presence_of_element_located((By.ID,"taxRegimeTnCCheckBox")))
			checkTaxRegime = browser.find_element_by_xpath(".//input[@type='checkbox' and @id='taxRegimeTnCCheckBox']")
			location = checkTaxRegime.location #{'x': 29, 'y': 1604}
			size = checkTaxRegime.size #{'height': 17, 'width': 14}
			print(location)
			print(size) 
			

			ActionChains(browser).move_to_element(checkTaxRegime).click(checkTaxRegime).perform()
			"""
			checkTaxRegime = browser.find_element_by_css_selector("input[type='checkbox'][id='taxRegimeTnCCheckBox']")#find_element_by_xpath(".//input[@type='checkbox' and @id='taxRegimeTnCCheckBox']")#("taxRegimeTnCCheckBox")
			checkTaxRegime.click()
			"""
			device_logger.logging.info('captured Tax Regime Check check box')
		except Exception as e:
			print(e)
			traceback.print_exc()
			device_logger.logging.info('not captured new Tax Regime Check check box')

		#sleep(8)

		try:
			# tap on create button
			history = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.tax_history_h.btn.btn-primary.btn-solid.w-100")))
			
			history.click()

			device_logger.logging.info('captured tax history button')
		except:
			device_logger.logging.info('not captured tax history button')


		try:
			close = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-danger.w-50.m-auto.close_h")))
			#browser.find_element_by_class_name("close_h")
			close.click()
			"""
			if success.is_displayed():
				if success.is_enabled():
					success.click()
			"""
			device_logger.logging.info('captured close element')
		except:
			device_logger.logging.info('not captured close element')

		#sleep(8)

		try:
			# tap on create button
			disclaimer = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.btn-solid.w-100.show_disclaimer_h")))
			
			disclaimer.click()

			device_logger.logging.info('captured disclaimer button')
		except:
			device_logger.logging.info('not captured disclaimer button')


		#sleep(6)

		try:
			close = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-danger.w-50.m-auto.okay_close_h")))
			#browser.find_element_by_class_name("close_h")
			close.click()
			"""
			if success.is_displayed():
				if success.is_enabled():
					success.click()
			"""
			device_logger.logging.info('captured okay button')
		except:
			device_logger.logging.info('not captured okay button')

		try:
			# tap on create button
			declaration = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.btn-solid.w-100.show_self_declaration_h")))
			
			declaration.click()

			device_logger.logging.info('captured declaration button')
		except:
			device_logger.logging.info('not captured declaration button')

		try:
			sleep(4)
			#checkSection = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.ID, "newTaxRegimeCheckSection")))
			#checkSection=WebDriverWait(browser,4).until(EC.visibility_of_element_located((By.ID,"newTaxRegimeCheckSection")))
			checkSection = browser.find_element_by_xpath(".//input[@type='checkbox' and @id='newTaxRegimeCheckSection']")
			print("checkSection")
			#checkSection = browser.find_element_by_xpath(".//input[@type='checkbox' and @id='newTaxRegimeCheckSection']")#("newTaxRegimeCheckSection")
			#checkSection.click()
			#checkSection.screenshot('../ss.png')
			location = checkSection.location #{'x': 51, 'y': 532}
			size = checkSection.size  #{'height': 17, 'width': 14}
			print(location) 
			print(size)
			#for i in range(40):
			new_x = 51 + 28 +7
			new_y = 532 - 8
			#ActionChains(browser).move_to_element(checkSection).click(checkSection).perform()
			ActionChains(browser).move_to_element_with_offset(checkSection, new_x, new_y).click().perform()
			"""
			for i in range(51, 111):
				new_x = i

				try:
					ActionChains(browser).move_to_element_with_offset(checkSection, new_x, new_y).click().perform()
				except Exception as e:
					traceback.print_exc()
			
			
			label = browser.find_element_by_xpath(".//div[@class='custom-control.custom-checkbox.notice_check_section_h']") #browser.find_element_by_xpath(".//label[@for='newTaxRegimeCheckSection']")
			print("label")
			location_label = label.location #{'x': 111, 'y': 532}
			size_label = label.size  #{'height': 17, 'width': 198}
			print(location_label) 
			print(size_label)
			#ActionChains(browser).move_to_element_with_offset(checkSection, new_x, new_y).click().perform()
			device_logger.logging.info('captured Tax Regime Check checkbox')
			"""
		except:
			traceback.print_exc()
			device_logger.logging.info('not captured new Tax Regime Check checkbox')



		try:
			close = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-danger.w-50.m-auto.okay_close_h")))
			#browser.find_element_by_class_name("close_h")
			close.click()
			"""
			if success.is_displayed():
				if success.is_enabled():
					success.click()
			"""
			device_logger.logging.info('captured okay button')
		except:
			device_logger.logging.info('not captured okay button')

		

		try:
			# tap on create button
			submit = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.submit_selected_regime_h.btn.btn-primary.btn-solid.w-100")))
			
			submit.click()

			device_logger.logging.info('captured submit button')
		except:
			device_logger.logging.info('not captured submit button')
			current_Time = datetime.now() - startTime
			print(current_Time)	

			take_screenshot_and_browserlog(browser, device_logger, self.Name)
			self.writexlslogsln({
				'Status':'Failed',
				'Reason':'Tax Simulation request not submitted',
				'TimeTaken':str(current_Time),
				'SubscriptionName':self.companycode,
				'EmployeeCode':self.employeeCode
			})
			
			return False

			

		current_Time = datetime.now() - startTime
		print(current_Time)	

		take_screenshot_and_browserlog(browser, device_logger, self.Name)
		self.writexlslogsln({
			'Status':'Pass',
			'Reason':'successfully executed',
			'TimeTaken':str(current_Time),
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
		
		device_logger.logging.info("########TaxSimulatorNewTaxRegimeTest done successful########")
		browser.close_app()
		return True;
		

