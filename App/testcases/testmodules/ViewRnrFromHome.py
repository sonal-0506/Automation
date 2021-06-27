from .TestModule import *
from extralibs.helpers import take_screenshot_and_browserlog
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from datetime import date
from sys import exit
from selenium.common.exceptions import NoSuchElementException


class ViewRnrFromHomeTest(TestModule):
	def __init__(self, companycode, employeeCode, password):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		ModuleName = "ViewRnrFromHomeTest"
		ModuleDesc = "Test for ViewRnrFromHome"
		super().__init__(ModuleName, ModuleDesc)
		# extra properties goes here

	def runtest(self, browser, device_logger):
		

		today = datetime.today()
		startTime = datetime.now()
		print(startTime)
		
		status="Failed"
		
		#capturing company code textbox button
		input_field = browser.find_element_by_id("TxtCompanyCode")
		sleep(2)
		input_field.clear()
		input_field.send_keys(self.companycode)
		#input_field.send_keys(Keys.RETURN)

		#capturing companycode submit button
		input_field7 = browser.find_element_by_id("proceedWithCompanyCode")
		sleep(2)
		input_field7.click()

		#capturing employeecode textfield
		input_field2 = browser.find_element_by_id("employeeCode")
		sleep(2)
		input_field2.clear()
		print("aaaaaaaaaaaaaa")
		input_field2.send_keys(self.employeeCode)
		#input_field2.send_keys(Keys.RETURN)

		#capturing employeepassword field
		input_field3 = browser.find_element_by_id("employeePassword")
		sleep(2)
		input_field3.clear()
		input_field3.send_keys(self.password)
		
		#input_field3.send_keys(Keys.RETURN) 

		#capturing login button
		input_field4 = browser.find_element_by_css_selector(".user_login_h")
		input_field4.click()
		
		sleep(8)

		
		try:
			#browser.implicitly_wait(120)
			input_field4 = browser.find_element_by_css_selector("span.view_all_rnr_widget_h")
			input_field4.click()
			device_logger.logging.info('captured viewall element for rewards')
		except NoSuchElementException as e:
			
			device_logger.logging.error(' not captured viewall element for rewards ')

			return False;

		else:
			take_screenshot_and_browserlog(browser, device_logger, self.Name)
		
			try:
			#Learderboard
				var = browser.find_element_by_class_name('find_element_by_class_name')
				var.click()
				device_logger.logging.info('captured Leaderboard card element for rewards')
			except:
				device_logger.logging.error('not captured Leaderboard card element for rewards')	

			try:	
				#leaderboard top givers
				var = browser.find_element_by_xpath('//*[@id="myTab"]/li[2]/a')
				var.click()
				device_logger.logging.info('captured top givers in leaderboard element for rewards')
			except:
				device_logger.logging.error('not captured top givers in leaderboard element for rewards')	
			
			try:	
				#My Rewards
				var = browser.find_element_by_class_name('show_rewards_h')
				var.click()
				device_logger.logging.info('captured my rewards element ')
			except:
				device_logger.logging.error('not captured my rewards element ')

			try:
				#capturing hamburger icon
				var = browser.find_element_by_class_name('menu-icon')
				var.click()
				device_logger.logging.info('captured hamberger menu icon element ')
			except:
				device_logger.logging.error('not captured hamberger menu icon element ')

			try:
				#home screen	
				var = browser.find_element_by_class_name('home_menu_h')
				var.click()
				device_logger.logging.info('captured home screen element element')
			except:
				device_logger.logging.error('not captured home screen element')

			sleep(4)
			
			device_logger.logging.info("--------------------------------- ViewRnrFromHome done successful ---------------------------------")
			return True;

			status="Pass"

		finally:

			current_Time = datetime.now() - startTime
			print(current_Time)

			self.writexlslogsln({
				'Status':status,
				'TimeTaken':str(current_Time),
				'SubscriptionName':self.companycode,
				'EmployeeCode':self.employeeCode
			})
			
			