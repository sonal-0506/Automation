from .TestModule import *
from extralibs.helpers import take_screenshot_and_browserlog
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select


class CreateNewHelpdeskTicketTest(TestModule):
	def __init__(self, companycode, employeeCode, password):
		self.companycode = companycode
		self.employeeCode = employeeCode
		self.password = password
		ModuleName = "CreateNewHelpdeskTicketTest"
		ModuleDesc = "Test for CreateNewHelpdeskTicket"
		super().__init__(ModuleName, ModuleDesc)
		# extra properties goes here

	def runtest(self, browser, device_logger):
		
		#capturing company code textbox button
		var = browser.find_element_by_id("TxtCompanyCode")
		sleep(2)
		var.clear()
		var.send_keys(self.companycode)
		#input_field.send_keys(Keys.RETURN)

		#capturing companycode submit button
		var = browser.find_element_by_id("proceedWithCompanyCode")
		sleep(2)
		var.click()

		#capturing employeecode textfield
		var = browser.find_element_by_id("employeeCode")
		sleep(2)
		var.clear()
		print("aaaaaaaaaaaaaa")
		var.send_keys(self.employeeCode)
		#input_field2.send_keys(Keys.RETURN)

		#capturing employeepassword field
		var = browser.find_element_by_id("employeePassword")
		sleep(2)
		var.clear()
		var.send_keys(self.password)
		
		#input_field3.send_keys(Keys.RETURN) 

		#capturing login button
		var = browser.find_element_by_css_selector(".user_login_h")
		var.click()

		#capturing hamberger menu icon
		#var = browser.find_element_by_xpath('//*[@id="headerRegion"]/div/a/div[1]')
		var = browser.find_element_by_css_selector('div.menu-icon')
		var.click()

		#capturing menu search element
		var = browser.find_element_by_css_selector('.menu_search_text_h[placeholder="Search"]')
		sleep(2)
		var.clear()
		var.send_keys('help')

		sleep(2)

		#capturing helpdesk card displayed after searching
		var = browser.find_element_by_css_selector('li.help_desk_menu_h')
		var.click()
		sleep(2)

		#capturing xpath of create new ticket icon
		var = browser.find_element_by_xpath('//*[@id="bodyRegion"]/div/div[1]/div/div[1]')
		var.click()

		#capturing main category dropdown list
		#var = browser.find_element_by_class_name('main_category_h')
		#var.click()

		varr = input('please select the main category') # from the below options provided into which you want to create ticket: \n 14 - Admin Requests \n 36 - Application Requests \n 34 - Azure Cloud Requests \n 39 - Barracuda WAF Requests \n 33 - Client Request \n 37 - Form 16 Upload \n 38 - HR RELATED QUERIES \n 17 - IT HelpDesk \n 19 - New Development \n 35 - SQL/ DB requests \n 32 - User Management. \n choose any appropriate value from the above mentioned values: \n ')

		#capturing main category dropdown list
		var = Select(browser.find_element_by_class_name('main_category_h'))
		var.select_by_index(int(varr))
		"""
		print('''
			14 - Admin Requests-----------------
			40 - Admin Request
			41 - Stationery
			75 - Sitting arrangement

			36 - Application Requests-----------
			119 - Share Connection.Config/Web.config/Page or Bin from Servers
			120 - Share Folder details from Blob Store of Customer
			121 - Make New Virtual Directory - Mobile App Server
			122 - All Clients Patch
			123 - QA Patch
			133 - Make New Virtual Directory - WEB App Server
			134 - Mobile App Server changes
			135 - New Publish from Live App to Staging Server
			142 - Open Ports on App Severs
			143 - RDP App Server Access
			144 - Whitelisting of M-Services IPs on Live DB Servers

			34 - Azure Cloud Requests----------------
			100 - Creation of New VM's
			102 - Cloud VM Upscale or Downscale
			103 - Add New Storage disk Std or Premium
			107 - Make New Azure Key Vault
			108 - Setting up VPN Connection on Cloud
			136 - ChatBot Creation

			39 - Barracuda WAF Requests--------------
			139 - URL fixing
			140 - URL redirection ''') """
		varrr = input(str('please select the sub category')) # after reading above sub categories for the main category:'))
		

		#capturing subcategory - sub_category_h

		var = Select(browser.find_element_by_class_name('sub_category_h'))
		var.select_by_index(int(varrr))

		#capturing subject text box
		var = browser.find_element_by_id('requestSubject')
		var.send_keys('test ticket')

		#Capturing description box element
		var = browser.find_element_by_id('requestDescription')
		var.send_keys('test description')

		#capturing priority dropdwon list - request_priority_h

		var3 = input(str('give your priority from below: \n 1 - Urgent \n 2 - Normal \n 3 - VeryUrgent \n please give no out of above 3 values:'))

		var = Select(browser.find_element_by_class_name('request_priority_h'))
		var.select_by_index(int(var3))

		#capturing submit button
		var = browser.find_element_by_css_selector('button.submit_request_h')
		var.click()

		#capturing okay button after success message
		var = browser.find_element_by_css_selector('button.close_h')
		var.click()











		take_screenshot_and_browserlog(browser, device_logger, self.Name)
		self.writexlslogsln({
			'Status':'Pass',
			'TimeTaken':2,
			'SubscriptionName':self.companycode,
			'EmployeeCode':self.employeeCode
		})
		
		device_logger.logging.info("--------------------------------- CreateNewHelpdeskTicket done successful ---------------------------------")
		return True;
