import os
import sys
from selenium.common.exceptions import InvalidSessionIdException
from datetime import datetime
import logging
import xlsxwriter
import base64
import traceback

def ensure_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)



def take_screenshot_and_browserlog(driver, device_logger, calling_request):
	__save_log_type(driver, device_logger, calling_request, 'browser')

def take_screenshot_and_browserlog(driver, device_logger, calling_request):
	__save_log_type(driver, device_logger, calling_request, 'browser')

def take_screenshot_and_driverlog(driver, device_logger, calling_request):
	__save_log_type(driver, device_logger, calling_request, 'driver')

def start_recording(driver):
    driver.start_recording_screen()


def __save_log_type(driver, device_logger, calling_request, type):
	logcat_dir = device_logger.logcat_dir
	screenshot_dir = device_logger.screenshot_dir
	video_dir = device_logger.video_dir 
	print("saving screenshot in ",screenshot_dir)
	print("saving video in ",video_dir)
	try:
		screen_video = driver.stop_recording_screen()
		video_name = os.path.join(video_dir, calling_request + '.mp4')

	except InvalidSessionIdException:
		traceback.print_exc() 
		screen_video = ''

	with open(video_name, "wb") as video_file:
		video_file.write(base64.b64decode(screen_video))

	try:
		driver.save_screenshot(os.path.join(screenshot_dir, calling_request + '.png'))
		logcat_data = driver.get_log(type)
	except InvalidSessionIdException:
		logcat_data = ''
	

	with open(os.path.join(logcat_dir, '{}_{}.log'.format(calling_request, type)), 'w') as logcat_file:
		for data in logcat_data:
			data_string = '%s:  %s\n' % (data['timestamp'], data['message'].encode('utf-8'))
			logcat_file.write(data_string)


def _init_get_workbook(device_logger, calling_request, workbookcolumns):
	logcat_dir = device_logger.logcat_dir
	logfilepath = os.path.join(logcat_dir, '{}.xlsx'.format(calling_request))
	workbook = xlsxwriter.Workbook(logfilepath,{'default_date_format':'dd-mm-yyyy hh:mm:ss.000'})
	bold = workbook.add_format({'bold': True})
	worksheet = workbook.add_worksheet(name="testcaseresults")
	for key,val in  workbookcolumns.items():
		worksheet.write(val, key, bold)
	worksheet.set_column('A:Z', 22)

	# worksheet.write('A1', 'Index', bold)
	# worksheet.write('B1', 'Testcase', bold)
	# worksheet.write('C1', 'Date', bold)
	# worksheet.write('D1', 'Status', bold)
	# worksheet.write('E1', 'Reson', bold)
	# worksheet.write('F1', 'TimeTaken', bold)
	# worksheet.write('G1', 'Comments', bold)
	return workbook
		
def write_xls_logs(workbook):
	worksheet = workbook.get_worksheet_by_name("testcaseresults")

