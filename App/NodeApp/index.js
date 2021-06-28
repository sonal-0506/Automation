require('dotenv').config();
const wdio = require("webdriverio");
const {Browser} = require('./setup/driversetup.js');
const tests = require('./testcases');
async function main () {
	const browser = await Browser();
	await tests.LoginTest.run(browser);
   	//
   //console.log(tests);
   // //await client.url('https://duckduckgo.com')
   // const inputElem = await browser.$('#TxtCompanyCode')
   // await inputElem.setValue('cngyzing')	
   // const submitBtn = await browser.$('#proceedWithCompanyCode')
   // await submitBtn.click()
   // console.log(await browser.getTitle())
  // await client.deleteSession();
}

//console.log(tests);
main();
