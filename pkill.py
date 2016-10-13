import sys, traceback, os, time, datetime

#The following list must contain the full process name of the intended application to kill.
processList = []


def pkill (process_name):
    '''This function will pass the input parameter to os import library in order to execute a task kill command.'''
    #print("pkill")
    print("Attempting process kill on: " + str(datetime.datetime.now().time()))
    try:
        killed = os.system('taskkill /IM ' + process_name + ' /F')
    except (Exception):
        killed = 0
    return killed
    
        
def checkAppList():
    '''This function will check each item in the process list by executing isAppAlive() on each item, and return True or False.'''
    #print("checkAppList")
    for item in processList:
        #print("item: " + item)
        if isAppAlive(item) == True:
            #print(True)
            pkill(item)
        #print(False)
    
    
def isAppAlive (app):
    '''This function will take an input parameter and call 'tasklist' cmd function to determine if task is currently active within widnows fucntion. '''
    #print("isAppAlive")
    app = os.system('tasklist | findstr ' + '"' + app + '"')
    #print(type(app))
    if app == 1:
        return False
    return True

    
def loopAliveApps(inputSeconds):
    '''This fucntion will execute the checkapplist() fucntion and wait the passed paramater amount of time.'''
    #print("loopAliveApps")
    inputSeconds = int(inputSeconds)
    while True:
        checkAppList()
        #print("Sleeping for " + str(inputSeconds) + " seconds.")
        print(".")
        time.sleep(inputSeconds)

        
def main(time):
    '''This function will loop through process skill script for designated time.'''
    #print("main")
    time = int(time)
    print("Activating 'process kill program'. Will check for apps every " + str(time) + ' seconds. ')
    print("Checking for:\n " + str(processList))
    loopAliveApps(time)

#loopAliveApps(10)    
main(10)    
