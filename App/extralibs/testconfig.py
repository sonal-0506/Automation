import datetime
import os
import logging
from .helpers import ensure_dir
from .helpers import _init_get_workbook


def test_configure(config):
    if not hasattr(config, 'input'):
        current_day = '{:%Y_%m_%d_%H_%S}'.format(datetime.datetime.now())
        # ensure_dir(os.path.join(os.path.dirname(__file__),'../Logs', 'input', current_day))
        result_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'../Logs', 'results', current_day))
        ensure_dir(result_dir)
        result_dir_test_run = result_dir
        ensure_dir(os.path.join(result_dir_test_run, 'video'))
        ensure_dir(os.path.join(result_dir_test_run, 'screenshots'))
        ensure_dir(os.path.join(result_dir_test_run, 'logcat'))
        config.screenshot_dir = os.path.join(result_dir_test_run, 'screenshots')
        config.logcat_dir = os.path.join(result_dir_test_run, 'logcat')
        config.video_dir = os.path.join(result_dir_test_run, 'video')
        logging.basicConfig(
            filename = os.path.join(config.logcat_dir,'alllogs.txt'), 
            filemode='w',
            level=logging.DEBUG,
            format='%(asctime)s %(message)s'
        )
        config.logging = logging
        config.workbook = _init_get_workbook(config, "AllTestCases", config.getxlscolumns())
        
class DeviceLogger:
    def __init__(self, logcat_dir, screenshot_dir, video_dir):
        self.screenshot_dir = screenshot_dir
        self.logcat_dir = logcat_dir
        self.video_dir = video_dir
        self.logging = None
        self.workbook = None
        self.workbookcolumnstemp = {}
        self.workbookcolumns = {
            "Index":"A",
            "Testcase":"B",
            "SubscriptionName":"C",
            "EmployeeCode":"D",
            "Date":"E",
            "Status":"F",
            "Reason":"G",
            "TimeTaken":"H",
            "Comments":"I"
        }
        self.workbookrowscount = 1
    def getxlscolumns(self):
        for key,val in self.workbookcolumns.items():
            self.workbookcolumnstemp[key] = val+str(self.workbookrowscount)
        return self.workbookcolumnstemp

def device_logger(logcat_dir='logcat', screenshot_dir='screenshots', video_dir='video'):
    config = DeviceLogger(logcat_dir, screenshot_dir, video_dir)
    test_configure(config)
    return config
