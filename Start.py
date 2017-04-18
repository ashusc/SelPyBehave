#############################
# Automation Framework		#
# @Author: Ashutosh Mishra	#
# @Init: 17April2017		#
# Python-Selenium-Behave	#
#############################

#InBuilt Import Section.
import os
from selenium import webdriver
from behave import *
#################################################################################

#Local Import[Mine Wrote Python Classes]
from Src.Utils.Logger import Logger as Logger
from Src.Utils.Printer import Printer as Printer
from Src.Definitions.Steps import Steps as Steps
#################################################################################

#################################################################################
#	Framework Execution Point													#
#################################################################################
Printer().printInitiation()
#
# x = FrameworkDriver()
# driver = x.getChromeDriver()
#
# y = FrameworkUtil()
# driver = y.navigate(driver, 'https://www.google.com')
#
# x.closeWebDriverObject(driver)

#################################################################################
#	Framework End Point															#
#################################################################################
