var appName = process.env.appName || "ApiDemos.apk";
var appPath = __dirname+"/apps/"+appName;
const {resolve} = require("path");
const opts = {
  path: '/wd/hub',
  port: 4723,
  capabilities: {
    platformName: process.env.platformName || "Android",
    platformVersion: process.env.platformVersion || "8",
    deviceName: process.env.deviceName || "Real Device",
    //app: appPath,
    appPackage: process.env.appPackage || "com.zinghr.app",
    appActivity: process.env.appActivity || "MainActivity",
    automationName: process.env.automationName || "UiAutomator2",
    autoWebview: true,
    chromeOptions: {'w3c': false},
    chromedriverExecutable: (process.env.chromedriverExecutable && resolve(process.env.chromedriverExecutable)) || resolve("../chromedriver/win/chromedriver.exe")
  }
};
console.log(process.env.appPath);
if(process.env.appPath=='true'){
    opts.capabilities.app = appPath;
}
module.exports={
  opts
};
