import importlib
def magicimport(lib):
  try:
    successlib = importlib.import_module(lib)
  except:
      print(lib+' is not installed. Installing...')
      time.sleep(0.5)
      try:
          try:
              from pip import main as pipmain
              time.sleep(0.5)
          except:
              from pip._internal import main as pipmain
              time.sleep(0.5)
          pipmain(['install',lib])
          time.sleep(0.5)
      except:
        print("Installation failed. pip is not installed. Please install pip before running this app.")
        time.sleep(0.5)
      exit(0)
  return successlib
