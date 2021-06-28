from extralibs.helpers import _init_get_workbook
from datetime import datetime
class TestModule:
	def __init__(self, ModuleName, ModuleDesc):
		self.Name = ModuleName
		self.Desc = ModuleDesc
		self.workbook = None
		self.worksheet = None
		self.logger = None
		print(ModuleName,' initialized')
		self.isPassed = False
		# switch context and browser rest code can be added over here...
	
	def run(self,browser, device_logger):
		self.logger = device_logger
		self.__initlogger()
		print(self.Name+" test running")
		try:
			self.isPassed = self.runtest(browser, self.logger);
		except Exception as e:
			print("Exception occured in test",e)
			device_logger.logging.error('Exception: ' + str(e))
		#self.workbook.close()	
		print(self.Name+" done")
		print(self.Name+" test ends with "+("success" if self.isPassed else "failed"))
	
	def __initlogger(self):
		#self.workbook = _init_get_workbook(device_logger, self.Name, self.logger.workbook.getxlscolumns())
		self.workbook = self.logger.workbook;
		self.worksheet = self.workbook.get_worksheet_by_name("testcaseresults")
		#self.date_format = self.workbook.add_format({'num_format': 'dd-mm-yyyy hh:mm:ss.000'})
		self.addrow()

	def writexlslogs(self, colsdicts):
		for key,val in colsdicts.items():
			if(key=='Status'):
				cell_format = self.workbook.add_format({
					'bold': True, 
					'font_color': 'red' if val.lower()=='failed' else 'green'
				})
				self.worksheet.write(self.logger.workbookcolumnstemp[key], val, cell_format)
			else:
				self.worksheet.write(self.logger.workbookcolumnstemp[key], val)		
		self.writexlsdefaultlogs(colsdicts)

	def writexlsdefaultlogs(self, colsdicts):
		if('Index' not in colsdicts):
			self.worksheet.write(self.logger.workbookcolumnstemp['Index'], self.logger.workbookrowscount-1)
		if('Testcase' not in colsdicts):
			self.worksheet.write(self.logger.workbookcolumnstemp['Testcase'], self.Name)
		if('Date' not in colsdicts):
			today = datetime.today()
			date_time = datetime.strptime(str(today), '%Y-%m-%d %H:%M:%S.%f')
			self.worksheet.write_datetime(self.logger.workbookcolumnstemp['Date'], date_time)

	def writexlslogsln(self, colsdicts):
		self.writexlslogs(colsdicts)
		#self.addrow()

	def addrow(self):
		self.logger.workbookrowscount +=1
		self.logger.getxlscolumns()

	def runtest(browser, device_logger):
		pass