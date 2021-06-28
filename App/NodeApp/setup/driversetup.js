const wdio = require("webdriverio");
const {
  opts
} = require('./config.js');
async function Browser() {
   const browser = await wdio.remote(opts);
   return browser;
}
module.exports={
	Browser
}