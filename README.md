# SelPyBehave

[Required Modules]
This framework is developed in Python 2.7, so used and required modules are
- Selenium Webdriver
- behave

[Runnning the Framework]
just Run the Command in terminal "behave" under the path "./SelPyBehave/"


Since this is very basic prototype of Python+Behave+Selenium Automation Framework, 
so just write a feature file under "./SelPyBehave/Src/Features/"<your_feature_file>.feature, 
and implement the step functions under "./SelPyBehave/Src/steps/<Steps.py | your_python_file>"...
and you thats it.

[Framework Structure]
  SelPyBehave
    |
    |_Core [basic setting related with WebDriver and configurations]
        |_Basic [ Classes for Selenium WebDriver ]
        |_Configuration [Classes for setting configuration for this framework]
    |_Logs [Used for Automation logs, Pending]
    |_Reports [for junit report(xml format) and json raw reports]
    |_Src
        |_Features
            |_your_feature_files.feature
        |_steps
            |_step_definition_in_python_file
