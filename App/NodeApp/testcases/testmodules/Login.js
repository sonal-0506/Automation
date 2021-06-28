const thisTest = module.exports.LoginTest = new (require('../TestModule.js'))(
	"Login",
	"Used For Login Tests"
);
thisTest.runtest = async function(browser){
   console.log('new method');
   const inputElem = await browser.$('#TxtCompanyCode')
   await inputElem.setValue('cngyzing')	
   const submitBtn = await browser.$('#proceedWithCompanyCode')
   await submitBtn.click()
   console.log(await browser.getTitle())
   //await client.deleteSession();
}
