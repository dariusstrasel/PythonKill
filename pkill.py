import sys, logging, traceback, os, time, datetime
from processListConfig import PROCESS_LIST
from processListConfig import SECONDS_TO_LOOP_FOR

# The processList is imported from the processListConfig.py file
# The processListConfig file should contain the full process name, such as:
# defaultList = ["chromedriver.exe"]



def pkill (process_name):
    '''This function will pass the input parameter to os import library in order to execute a task kill command.'''
    logging.debug('pkill')
    print("Attempting process kill on: " + str(datetime.datetime.now().time()))
    try:
        killed = os.system('taskkill /IM ' + process_name + ' /F')
    except (Exception):
        killed = 0
    return killed
    
        
def checkAppList():
    '''This function will check each item in the process list by executing isAppAlive() on each item, and return True or False.'''
    logging.debug("checkAppList")
    for process_to_kill in PROCESS_LIST:
        #print("item: " + item)
        if isAppAlive(process_to_kill) == True:
            pkill(process_to_kill)
    
    
def isAppAlive (app):
    '''This function will take an input parameter and call 'tasklist' cmd function to determine if task is currently active within widnows fucntion. '''
    logging.debug("isAppAlive")
    app = os.system('tasklist | findstr ' + '"' + app + '"')
    
    logging.debug(type(app))
    if app == 1:
        return False
    return True

    
def loopAliveApps(inputSeconds):
    '''This fucntion will execute the checkapplist() fucntion and wait the passed paramater amount of time.'''
    logging.debug("loopAliveApps")

    inputSeconds = int(inputSeconds)
    if inputSeconds != 0:
        while True:
        	checkAppList()
        	#print("Sleeping for " + str(inputSeconds) + " seconds.")
        	print(".")
        	time.sleep(inputSeconds)
    else:
        checkAppList()

        
def main(time):
    '''This function will loop through process skill script for designated time.'''
    logging.debug("main")
    time = int(time)
    print("Activating 'process kill program'. Will check for apps every " + str(time) + ' seconds. ')
    print("Checking for:\n " + str(PROCESS_LIST))
    loopAliveApps(time)

   
main(SECONDS_TO_LOOP_FOR)    
