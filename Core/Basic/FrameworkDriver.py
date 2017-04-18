#Framework's Basic Function regarding WebDrivers.
class FrameworkDriver:

	#Standard Variables [ In Case (if any) ]
	#path= "C:\DRIVERS\chromedriver_win32\chromedriver.exe"
	#firefoxDriverPath= "C:\DRIVERS\chromedriver_win32\chromedriver.exe"
	
	def getChromeDriver(self, path):
		#Accessing site/Setting chrome driver with the url params
		FrameworkUtil().log('Getting and returning Chrome Driver....\n')
		driver = webdriver.Chrome(path)
		return driver
		
	def getFirefoxDriver(self, path):
		#Accessing site/Setting chrome driver with the url params
		FrameworkUtil().log('Getting and returning FireFox Driver....\n')
		driver = webdriver.FireFox(path)
		return driver

	def closeWebDriverObject(self, driver):
		FrameworkUtil().log('Closing Given Web Driver....\n')
		driver.close()
		
	def terminateFramework(self):
		FrameworkUtil().log('Terminating FRAMEWORK....\n')
		exit()