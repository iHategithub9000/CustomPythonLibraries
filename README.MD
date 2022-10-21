# _Python libraries:_
### BetterError:
`CustomError(title, text, fatal)`: make an error  
`CustomWarning(title, text)`: make a warning
### configparser_mlgmode:

`setupConfigParser()`: Takes no arguments. Basicly installs all the required stuff for this module to work.

`setup_pip()`: Takes no arguments. Installs the package manager. This is automatically ran by `setupConfigParser()`.

`writeConfigData(file_path, section, value, newValueContent)`: Takes 4 strings as arguments, used to write to the config file. Duhhhh. Arguments are preety self-explanatory so i will not explain them ok.

`returnConfigData(file_path, section, value)`: `writeConfigData` but reverse lol

this is literally just simplified configparser

### gitHelp:
~~litterally just 1 function~~  
`gitHelp(gitCommand)`: Opens the documentation of a git command. If `gitCommand` is equal to `"all"`, all documentations open.

### variables:
`VARS`
variables.intlimit = 2147483647
variables.negativeintlimit = -2147483648
variables.pi = 3.141592653589793

`Functions`
rand(a,b)                       random number  
add(a,b)                        add two numbers  
substract(a,b)                  substract numbers.  
multiply(a,b)                   multiply numbers.  
divide(a,b)                     divide numbers.      returns "No." if dividing by 0  
exp(a,b)                        a to power of b  
printtype(var)                  prints type of variables without <class ''> jibberish  
killuser()                      kills its user  

# _Install guide:_  
just paste the library .py file to the directory with your python file and then import it  
