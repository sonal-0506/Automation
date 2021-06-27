from .TestModule import *
from extralibs.helpers import take_screenshot_and_browserlog
from extralibs.helpers import start_recording
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ForgotPasswordTest(TestModule):
	def __init__(self, companycode, employeeCode, password):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		
		ModuleName = "ForgotPasswordTest"
		ModuleDesc = "Test for ForgotPassword"
		super().__init__(ModuleName, ModuleDesc)
		# extra properties goes here

	def runtest(self, browser, device_logger):
		start_recording(browser)
		today = datetime.today()
		startTime = datetime.now()
		print(startTime)

		
		#app reset
		browser.reset()
		sleep(2)
		status = "Failed"
		#capturing company code textbox button

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

		sleep(2)

		try:
			var = browser.find_element_by_id("TxtCompanyCode")
			sleep(2)
			var.clear()
			var.send_keys(self.companycode)
			#input_field.send_keys(Keys.RETURN)
		except:
			device_logger.logging.error('Not captured company code textbox')

		try:

			#capturing companycode submit button
			var = browser.find_element_by_id("proceedWithCompanyCode")
			sleep(2)
			var.click()
		except:
			device_logger.logging.error('Not captured Proceed With CompanyCode element')


		try:

			#capturing employeecode textfield
			var = browser.find_element_by_id("employeeCode")
			sleep(2)
			var.clear()
			print("aaaaaaaaaaaaaa")
			var.send_keys(self.employeeCode)
			#input_field2.send_keys(Keys.RETURN)
		except:
			device_logger.logging.error('Not captured employee code textbox')

		try:
			sleep(2)
			#capturing forgotpassword element - forgot_password_section_h
			var = browser.find_element_by_css_selector('a.forgot_password_section_h')
			var.click()
		except:
			device_logger.logging.error('Not captured forgot password section')

			
			return False


		try:
			
			#sendOTPOnRegisteredDetails
			#sleep(8)
			var = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.ID, "sendOTPOnRegisteredDetails")))
			#browser.find_element_by_id("sendOTPOnRegisteredDetails")
			var.click()

		except Exception as e:
			print("EEEEEE : "+e)
			device_logger.logging.error('Not captured Send OTP element')
			return False



		try:
			#sleep(4)
			otp_attempts = "Exceeded limit of OTP Attempts"
			elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
			#browser.find_element_by_class_name('subject_h') #title_h
			print(elem.text)
			
			if otp_attempts in elem.text:	
				take_screenshot_and_browserlog(browser, device_logger, self.Name)
				current_Time = datetime.now() - startTime
				self.writexlslogsln({
					'Status':'Failed',
					'Reason':str(elem.text),
					'TimeTaken':str(current_Time),
					'SubscriptionName':self.companycode,
					'EmployeeCode':self.employeeCode
				})
				device_logger.logging.error('Condition Passed:'+str(elem.text))
				device_logger.logging.info("###### ###### ######")
				device_logger.logging.error("####### ForgotPassword done failed #######")
				device_logger.logging.info("###### ###### ######")

				try:

					#capturing okay or #Exceeded limit of OTP Attempts
					#sleep(2)
					var = browser.find_element_by_css_selector('button.close_h')

					var.click()

				except:
					device_logger.logging.error('Not captured OKAY element')	


				#return False
				try:
					sleep(2)
					#capturing companycode submit button
					var = browser.find_element_by_id("backToLogin")
					#sleep(2)
					var.click()
				except:
					device_logger.logging.error('Not captured Proceed With CompanyCode element')

				return False		

		except:
			device_logger.logging.error('Not captured SUBJECT element')
			

		try:

			#capturing okay or #Exceeded limit of OTP Attempts
			#sleep(8)
			var = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.close_h")))
			#browser.find_element_by_css_selector('button.close_h')

			var.click()

		except:
			device_logger.logging.error('Not captured OKAY element')	
			return False



		try:

			#id - txtPersonalDetailsOtp
			var = browser.find_element_by_id("txtPersonalDetailsOtp")
			sleep(2)
			var.clear()
			var1 = input('enter otp received:')
			var.send_keys(var1)

		except:
			device_logger.logging.error('Not captured txt Personal Details Otp')

		


		self.inputNewPWD(browser, device_logger)

		#sleep(4)
		"""
		try:
			timer = browser.find_element_by_class_name('resend_otp_timer_h')
			print("timer : "+timer.text)
		except:
			device_logger.logging.error('Not captured OTP timer')
		"""
		pwd_change_success = "Password Changed successfully. Please login again with new password"
		
		
		try:
			elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h")))
			#elem = browser.find_element_by_class_name('subject_h') #title_h
			print(elem.text)	
				#Invalid login PIN'
				#'outside your shift timings',
				#alert2 = ['network connectivity issue', 'Invalid login PIN', 'outside your shift timings', 'not allowed at this location']
			
			sleep(2)
			invalid_details = "Invalid details"
			blank_otp = "Please provide valid OTP"
			
			if blank_otp or invalid_details in elem.text:	
				take_screenshot_and_browserlog(browser, device_logger, self.Name)
				current_Time = datetime.now() - startTime
				self.writexlslogsln({
					'Status':'Failed',
					'Reason':str(elem.text),
					'TimeTaken':str(current_Time),
					'SubscriptionName':self.companycode,
					'EmployeeCode':self.employeeCode
				})
				device_logger.logging.error('Condition Passed:'+str(elem.text))
				device_logger.logging.info("###### ###### ######")
				device_logger.logging.error("####### ForgotPassword done failed #######")
				device_logger.logging.info("###### ###### ######")

				try:
					#capturing okay or #Exceeded limit of OTP Attempts
					#sleep(2)
					var = browser.find_element_by_css_selector('button.close_h')
					var.click()
					return False
				except:
					device_logger.logging.error('Not captured OKAY element')	
					
			
			

			while((pwd_change_success not in elem.text)): # or (("" or '"0"') not in timer.text.strip())):
				previous_pwd = 'New password can not be from last 5 previous passwords'
				wrong_pwd = "New Password must have at least 8 characters, must contain at least one lower case letter, one upper case letter, one digit and one special character"
				#invalid_details = "Invalid details"
				#blank_otp = "Please provide valid OTP"
				print("inside while loop")
				if (previous_pwd or wrong_pwd) in elem.text:
					print("inside previous_pwd")
					try:
						var = browser.find_element_by_css_selector('button.close_h')
						var.click()
					except:
						device_logger.logging.error('Not captured OKAY element')

					self.inputNewPWD(browser, device_logger)
				"""

				if invalid_details or blank_otp in elem.text:
					print("inside invalid_details")
					try:
						var = browser.find_element_by_css_selector('button.close_h')
						var.click()
					except:
						device_logger.logging.error('Not captured OKAY element')

					try:

						#id - txtPersonalDetailsOtp
						element = WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.ID, "txtPersonalDetailsOtp")))
						
						#var = browser.find_element_by_id("txtPersonalDetailsOtp")
						#sleep(2)
						
						element.clear()
						var1 = input('enter otp received:')
						element.send_keys(var1)

					except:
						device_logger.logging.error('Not captured txt Personal Details Otp')

					self.inputNewPWD(browser, device_logger)

					
					try:
						reset_Password = browser.find_element_by_id('resetPassword')
						reset_Password.click()
						device_logger.logging.error('Captured Change Password element')
						#self.inputNewPWD(browser, device_logger)
					except:
						device_logger.logging.error('Not captured Change Password element')
					
				"""	

				try:
					elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, "subject_h"))) #title_h
					print(elem.text)

				except:
					device_logger.logging.error('Not captured Subject element')	

				"""
				try:
					timer = browser.find_element_by_class_name('resend_otp_timer_h')
					print("timer : "+timer.text + "len : "+ len(timer.text.strip()))
				except:
					device_logger.logging.error('Not captured OTP timer')


				if (pwd_change_success not in elem.text):
					#if print("inside failed scenario")
					current_Time = datetime.now() - startTime
				"""
			take_screenshot_and_browserlog(browser, device_logger, self.Name)
			self.writexlslogsln({
				'Status':status,
				'Reason':str(elem.text),
				'TimeTaken':str(current_Time),
				'SubscriptionName':self.companycode,
				'EmployeeCode':self.employeeCode
			})
			device_logger.logging.info("--------------------------------- Forgot Password Failed ---------------------------------")

			return False
						
				
		except:
			device_logger.logging.error('Not captured Subject element')	
			return False

		try:
			#sleep(4)
			var = WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.close_h")))
			#browser.find_element_by_css_selector('button.close_h')
			var.click()
		except:
			device_logger.logging.error('Not captured OKAY element')


		sleep(2)
	
		"""

		try:
			#capturing okay or #Exceeded limit of OTP Attempts
			sleep(2)
			var = browser.find_element_by_css_selector('button.close_h')
			var.click()
		except:
			device_logger.logging.error('Not captured OKAY element')
		"""	

		status = "Pass"
		current_Time = datetime.now() - startTime

		take_screenshot_and_browserlog(browser, device_logger, self.Name)
		self.writexlslogsln({
			'Status':status,
			'Reason':pwd_change_success,
			'TimeTaken':str(current_Time),
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
		
		device_logger.logging.info("--------------------------------- Forgot Password done successful ---------------------------------")
		return True;



	def inputNewPWD(self, browser, device_logger):

		try:
			np = browser.find_element_by_id('newPassword')
			#sleep(2)
			np.clear()
			np1 = input('enter new Password to set:')
			np.send_keys(np1)

		except:
			device_logger.logging.error('Not captured New Password element')

		try:
			cp = browser.find_element_by_id('confirmedPassword')
			#sleep(2)
			cp.clear()
			cp.send_keys(np1)
		except:
			device_logger.logging.error('Not captured Confirmed Password element')

		try:
			reset_Password = browser.find_element_by_id('resetPassword')
			reset_Password.click()
			device_logger.logging.error('Captured Change Password element')
			#self.inputNewPWD(browser, device_logger)
		except:
			device_logger.logging.error('Not captured Change Password element')

