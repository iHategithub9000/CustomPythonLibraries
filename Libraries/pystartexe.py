def startExeTable(t):
    import os
    if type(t) is list:
        for i in t:
            os.system("taskkill /im "+i+" /f")
            os.system("start "+i)
    else:
        raise NameError("Please define a list of .exe files to open.")
    
def startExe(t):
    import os
    if type(t) is str:
        os.system("taskkill /im "+i+" /f")
        os.system("start "+i)
    else:
        raise NameError("Please define an .exe file to open.")
    
