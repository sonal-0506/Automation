from dotenv import load_dotenv
load_dotenv(override=True)
from extralibs.testconfig import device_logger
from testcases import testmodules as tests
from time import sleep
from datetime import datetime
from datetime import date




logger = None
def main():
	global logger
	## setting up logger
	print("######### Configuring Logger ############")
	logger = device_logger()
	## setting up driver
	from setup.driversetup import InitDriver
	browser = InitDriver(logger)
	print("######### Starting test cases ############")
	
	print('Accessing data from the local file stored...')
	with open('./credentials.txt') as file:
		for line in file:
			fields = line.strip().split(',')
			#print('credentials stored in file are utilized')
			#print(fields[0])
			#print(fields[1])
			#print(fields[2])
		#v1 = fields[0]
		#v2 = fields[1]
		#v3 = fields[2]



	companycode = fields[0]
	employeeCode = fields[1]
	password = fields[2]
	mobile = fields[3]
	pin1 = fields[4]
	pin2 = fields[5]
	pin3 = fields[6]
	pin4 = fields[7]
	com = fields[8]
	ticketID = fields[9]
	

	print("\n")
	print("This will run all Helpdesk Testcases:")
	print("\n")

	today = datetime.today()
	Testsuite_startTime = datetime.now()
	print('Testexecution started', Testsuite_startTime)

	
	
	"""
	createTest = tests.CreateHelpDeskTicketTest(companycode, employeeCode, password, mobile)
	createTest.run(browser, logger)

	
	
	newTest = tests.NewHelpDeskTicketTest(companycode, employeeCode, password, ticketID)
	newTest.run(browser, logger)
	
	closeTest = tests.ClosedHelpDeskTicketTest(companycode, employeeCode, password, ticketID)
	closeTest.run(browser, logger)
	
	"""
	reopenTest = tests.ReOpenHelpDeskTicketTest(companycode, employeeCode, password, ticketID)
	reopenTest.run(browser, logger)
	"""
	paySlipTest = tests.ViewPaySlipTest(companycode, employeeCode, password)
	paySlipTest.run(browser, logger)
	
	paySlipTest = tests.ViewCumulativePaySlipTest(companycode, employeeCode, password)
	paySlipTest.run(browser, logger)
	
	taxTest = tests.ViewTaxTest(companycode, employeeCode, password)
	taxTest.run(browser, logger)
	
	#taxSimulatorTest = tests.TaxSimulatorNewTaxRegimeTest(companycode, employeeCode, password)
	#taxSimulatorTest.run(browser, logger)
	
	nonCTCclaim = tests.ApplyNonCTCClaimTest(companycode, employeeCode, password)
	nonCTCclaim.run(browser, logger)
	"""

	Testsuite_currentTime = datetime.now() - Testsuite_startTime
	print('\n Testcase Total Execution Time is:', Testsuite_currentTime, '\n')

	
	
if __name__=="__main__":
	try:
		main()
		logger.workbook.close()
	except Exception as e:
		print('All Tests Exception ',e)
		logger.logging.error('All Tests Exception: ' + str(e))
		logger.workbook.close()













# import os
# from setup.driversetup import driver
# from selenium.webdriver.common.keys import Keys 
# from time import sleep
# print(driver)
# input_field = driver.find_element_by_id("TxtCompanyCode")
# print(input_field)	
# sleep(1)
# input_field.clear()
# input_field.send_keys('Appium User')
# input_field.send_keys(Keys.RETURN)
# test that everything is a-ok
# source = driver.page_source
# print(source)