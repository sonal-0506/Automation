from .TestModule import *
from extralibs.helpers import take_screenshot_and_browserlog
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from datetime import date
from sys import exit
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class 	ViewDayStatsFromAttendanceTest(TestModule):

	def __init__(self, companycode, employeeCode, password, com):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		self.com = com
		ModuleName = "ViewDayStatsFromAttendanceTest"
		ModuleDesc = "Test for ViewDayStatsFromAttendance"
		super().__init__(ModuleName, ModuleDesc)
		# extra properties goes here

	def runtest(self, browser, device_logger):
		

		today = datetime.today()
		startTime = datetime.now()
		print(startTime)

		
		#app reset
		browser.reset()
		sleep(2)
		
		status="Failed"

		try:
			#switch context to web view
			web = browser.contexts[1]
			browser.switch_to.context(web)
			sleep(2)
		except:
			print('unable to switch context')
		
		
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
		
		#sleep(8)
		
		browser.implicitly_wait(10)

		try:
			#apply button element
			var = browser.find_element_by_class_name('cancel_callback_h')
			var.click()
			device_logger.logging.info('captured apply button element')
		except:
			device_logger.logging.error('NOT captured apply button element')

		


		try:



			var = browser.find_element_by_css_selector("span.attendance_view_h")
			actions = ActionChains(browser)
			actions.move_to_element(var).click().perform()
			
		


			action = TouchActions(browser)
			value = input('enter date (no only) from current month for stats check like 03:')

			


	    	

			

			element = browser.find_element_by_css_selector('.fc-widget-content[data-date="2020-12-'+value+'"]')

			print("long_press started")

			action.tap(element).long_press(element).perform()

			print("long_press ends")
				
				
			device_logger.logging.info("captured day date from calendar to view stats")
		except Exception as e:	
			print(e)	
			device_logger.logging.error("NOT captured day date from calendar for view stats")
			return False
			
			sleep(3)

			"""
			var1 = browser.find_element_by_css_selector('button.close_h')
			actions = ActionChains(browser)
			actions.move_to_element(var1).perform()
			
			for i in range(4):
				touch = TouchAction(browser)
				touch.press(x=756, y=1898).move_to(x=717, y=1078).release().perform()
				sleep(2)

			try:
				var1 = browser.find_element_by_css_selector('button.close_h')
				var1.click()
				device_logger.logging.info("captured okay for stats button")
			except:		
				device_logger.logging.error(" NOT captured okay for stats button")
				#return False
			sleep(2)	
			var2 = browser.find_element_by_class_name('regularization_button_h')
			actions = ActionChains(browser)
			actions.move_to_element(var2).perform()	

			try:
				var2 = browser.find_element_by_class_name('regularization_button_h')
				var2.click()
				device_logger.logging.info("captured regularization button")
			except:		
				device_logger.logging.error(" NOT captured regularization button")
				#return False
					try:
				var = browser.find_element_by_class_name('subject_h')
				print(var.text)
				#sleep(2)
				current_Time = datetime.now() - startTime
				take_screenshot_and_browserlog(browser, device_logger, self.Name)
				self.writexlslogsln({
					'Status':'Failed',
					'Reason':str(elem.text),
					'TimeTaken':str(current_Time),
					'SubscriptionName':self.companycode,
					'EmployeeCode':self.employeeCode
				})
				device_logger.logging.error(str(elem.text))
				device_logger.logging.info("###### ###### ######")
				device_logger.logging.error("####### ApplyRegularizeFromAttendance done failed #######")
				device_logger.logging.info("###### ###### ######")
				browser.close_app()
				return False
				#pass
				#exit()
				#quit()
				#else:
					#print("no Alert found")
			except NoSuchElementException:
				device_logger.logging.error("------Alert NOT captured--------")
				pass	

			try:
				var = browser.find_element_by_class_name('close_h')
				var.click()
				device_logger.logging.info("captured okay button for alert")
			except NoSuchElementException:	
				device_logger.logging.error(" NOT captured okay button for alert")
				pass
			
			sleep(7)

			try:
				var = browser.find_element_by_id('regularizeSelectAction')
				var.click()
				device_logger.logging.info("captured regularize action dropdownlist element")
			except NoSuchElementException:	
				device_logger.logging.error(" NOT captured regularize action dropdownlist element")



			try:
				var = browser.find_element_by_xpath('//*[@id="regularizeSelectAction"]/option[2]')
				var.click()
				device_logger.logging.info('captured regularization option from dropdown')
			except:
				device_logger.logging.info('NOT captured regularization option from dropdown')				


			try:
				var = browser.find_element_by_id('regularizeSelectAction')
				var.click()
				device_logger.logging.info("captured regularize action dropdownlist element")
			except NoSuchElementException:	
				device_logger.logging.error(" NOT captured regularize action dropdownlist element")	

			try:
				var = browser.find_element_by_id('applyRegularizeClockIn')
				var.click()
				device_logger.logging.info("captured regularize In time element")
			except NoSuchElementException:	
				device_logger.logging.error(" NOT captured regularize In time element")

			try:
				native = browser.contexts[0]
				browser.switch_to.context(native)

				context = browser.current_context
				print(context)
				device_logger.logging.info('switched context from web to native view')
			except:
				device_logger.logging.error(' not able to switch context fro web to native')
			
			try:
				#capture hour xpath regularize in time
				var = browser.find_element_by_xpath('//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="10"]')
				var.click()
				device_logger.logging.info('captured hour element for regularize in time')
			except:
				device_logger.logging.error(' not captured hour element for regularize in time')

			try:
				#capture min xpath regularize in time
				var = browser.find_element_by_xpath('//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="0"]')
				var.click()
				device_logger.logging.info('captured min element for regularize in time')
			except:
				device_logger.logging.error(' not captured min element for regularize in time')	

			try:
				#am for regularize in time
				var = browser.find_element_by_id('android:id/am_label')
				var.click()
				device_logger.logging.info('captured am element for regularize in time')
			except:
				device_logger.logging.error(' not captured am element for regularize in time')


			try:
				#capturing ok in native view after selecting regularize in time
				var = browser.find_element_by_id('android:id/button1')
				var.click()
				device_logger.logging.info('captured ok element in native')
			except:
				device_logger.logging.error('NOT captured ok element in native')


			try:
				web = browser.contexts[1]
				browser.switch_to.context(web)
				device_logger.logging.info('switched context from native to web view')
			except:
				device_logger.logging.error(' not able to switch context fro native to web')
			

			try:
				var = browser.find_element_by_id('applyRegularizeClockOut')
				var.click()
				device_logger.logging.info('captured regularize out time element')
			except:
				device_logger.logging.error('NOT captured regularize out time element')

			
			try:
				native = browser.contexts[0]
				browser.switch_to.context(native)

				context = browser.current_context
				print(context)
				device_logger.logging.info('switched context from web to native view')
			except:
				device_logger.logging.error(' not able to switch context fro web to native')
			
			try:
				#capture hour xpath regularize out time
				var = browser.find_element_by_xpath('//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="8"]')
				var.click()
				device_logger.logging.info('captured hour element for regularize in time')
			except:
				device_logger.logging.error(' not captured hour element for regularize in time')

			try:
				#capture min xpath regularize out time
				var = browser.find_element_by_xpath('//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="0"]')
				var.click()
				device_logger.logging.info('captured min element for regularize in time')
			except:
				device_logger.logging.error(' not captured min element for regularize in time')	

			try:
				#pm for regularize out time
				var = browser.find_element_by_id('android:id/pm_label')
				var.click()
				device_logger.logging.info('captured am element for regularize in time')
			except:
				device_logger.logging.error(' not captured am element for regularize in time')


			try:
				#capturing ok in native view after selecting regularize in time
				var = browser.find_element_by_id('android:id/button1')
				var.click()
				device_logger.logging.info('captured ok element in native')
			except:
				device_logger.logging.error('NOT captured ok element in native')


			try:
				web = browser.contexts[1]
				browser.switch_to.context(web)
				device_logger.logging.info('switched context from native to web view')
			except:
				device_logger.logging.error(' not able to switch context fro native to web')		
				
			try:
				#regularization Remark
				var = browser.find_element_by_id('regularizationRemark')
				sleep(2)
				var.clear()
				var.send_keys(self.com)
				device_logger.logging.info('captured regularization remark')
			except:
				device_logger.logging.error('NOT captured regularization remark')


			var = browser.find_element_by_class_name('ok_callback_h')
			actions = ActionChains(browser)
			actions.move_to_element(var).perform()


			try:
				#apply button element
				var = browser.find_element_by_class_name('ok_callback_h')
				var.click()
				device_logger.logging.info('captured apply button element')
			except:
				device_logger.logging.error('NOT captured apply button element')

			
			try:
				#alert msg for blank fields
				var = browser.find_element_by_class_name('heading title_h')
				var.click()
				device_logger.logging.info('captured alert for blank field')
			except NoSuchElementException:
				device_logger.logging.error('NOT captured alert for blank field')
			
			
			try:
				#okay element
				var = browser.find_element_by_class_name('close_h')
				var.click()
				device_logger.logging.info('captured okay success button element')
			except NoSuchElementException:
				device_logger.logging.error('NOT captured okay success button element')	
			
			"""

		take_screenshot_and_browserlog(browser, device_logger, self.Name)
				

		sleep(3)

		status = "Pass"

		current_Time = datetime.now() - startTime
		print(current_Time)

			
		self.writexlslogsln({
			'Status':status,
			'Reason':'successfully executed',
			'TimeTaken':str(current_Time),
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
			
		device_logger.logging.info("########ApplyRegularizeFromAttendance done successful########")
		browser.close_app()
		return True;

