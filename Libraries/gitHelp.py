print("this module has only one function so just use 'from gitHelp import gitHelp'")
def gitHelp(gitCommand):
    import os
    if gitCommand == "all":
        gitCmds = ["clone","init","add","mv","restore","rm","bisect","diff","grep","log","show","status","branch","commit","merge","rebase","reset","switch","tag","fetch","pull","push"]
        for each in gitCmds:
            os.system(f"git help {each}")
    else:
        os.system(f"git help {gitCommand}")
gitHelp("all")