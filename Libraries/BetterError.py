from colorama import Fore, Style

def CustomError(strtitle, strtext, fatal):
  if fatal == False:
    print(Fore.RED + f"{strtitle}: {strtext}")
    print(Style.RESET_ALL)
  elif fatal == True:
    print(Fore.RED + Style.DIM + f"{strtitle}: {strtext}")
    print(Style.RESET_ALL)
    exit(9)
  else:
      print(Fore.RED + 'invalid Parameter for "fatal" (boolean) ')
      print(Style.RESET_ALL)

def CustomWarning(strtitle, strtext):
  print(Fore.YELLOW + f"{strtitle}: {strtext}")
  print(Style.RESET_ALL)
