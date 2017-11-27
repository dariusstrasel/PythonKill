import os

DEFAULT_LIST = ["chromedriver.exe"]
SECONDS_TO_LOOP_FOR = 0
PROCESS_LIST = DEFAULT_LIST if os.environ.get('processList') == None else os.environ.get('processList')