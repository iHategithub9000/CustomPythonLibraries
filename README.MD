# _Python libraries:_
### BetterError:
`CustomError(title, text, fatal)`: make an error
`CustomWarning(title, text)`: make a warning
### configparser_mlgmode:

`setupConfigParser()`: Takes no arguments. Basicly installs all the required stuff for this module to work.

`setup_pip()`: Takes no arguments. Installs the package manager. This is automatically ran by setupConfigParser().

`writeConfigData(file_path, section, value, newValueContent)`: Takes 4 strings as arguments, used to write to the config file. Duhhhh. Arguments are preety self-explanatory so i will not explain them ok.

`returnConfigData(file_path, section, value)`: `writeConfigData` but reverse lol

this is literally just simplified configparser

### gitHelp:
~~litterally just 1 function~~  
`gitHelp(gitCommand)`: Opens the documentation of a git command. If `gitCommand` is equal to `"all"`, all documentations open.
