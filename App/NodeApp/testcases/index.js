const glob = require("glob");

let allOfThem = {};
glob.sync(`${__dirname}/testmodules/*.js`).forEach((file) => {
  /* see note about this in example below */

  allOfThem = { ...allOfThem, ...require(file) };

});
module.exports = allOfThem;