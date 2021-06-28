class TestModule {
  constructor(ModuleName, ModuleDesc) {
    this.Name = ModuleName;
    this.Desc = ModuleDesc;
  }
  async run(browser){	
  	console.log(this.Name+" test running");
  	var result = await this.runtest(browser);
  	console.log(this.Name+" test ends with "+(result?"success":"failed"));
  }
  async runtest(browser){
  	
  }
}
module.exports = TestModule