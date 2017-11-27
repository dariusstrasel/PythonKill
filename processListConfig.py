import os

defaultList = ["chromedriver.exe"]

processList = defaultList if os.environ.get('processList') == None else os.environ.get('processList')