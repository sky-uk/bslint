## BrightScript Linter
[![CircleCI](https://circleci.com/gh/sky-uk/bslint/tree/master.svg?style=shield&circle-token=a9218a324d2d7bebd187a00fdc170b6a11a17462)](https://circleci.com/gh/sky-uk/bslint/tree/master)

*We're hiring!*
[http://developers.sky.com](http://developers.sky.com)

*Ever thought about joining us?*
[Feature Role: Python Developer for Sky Tickets in Osterley](https://goo.gl/AUZh1w)

#Description

This is a tool for linting BrightScript.

This tool has been made because there aren't any tools currently available to help developers keep their coding standards consistent.
The linter validates against the official [BrightScript Language Reference](https://sdkdocs.roku.com/display/sdkdoc/BrightScript+Language+Reference).
Currently the linter only lexes the file and validates styling. We are actively developing a parser which will be integrated into this project.

#Installing bslint via pip3

The package is published on pip3, to install follow the steps below:

1. Ensure that you've got Python3 installed on your machine (https://www.python.org/downloads/).
   To check if python3 is already installed, run `python3 -V` in your terminal.

2. Install `bslint` by running the following command in terminal `pip3 install bslint`.

#Upgrading bslint via pip3

To upgrade `bslint` run the following command in terminal `pip3 install bslint --upgrade`.

#Running bslint from terminal

To run `bslint` from the terminal, `cd` to the directory that you wish to lint and run the command `bslint`.

##Basic Options

You can run `bslint` in multiple ways:
* `bslint` -> Executes on the current directory and all subdirectories
* `bslint -p <directory_path>` -> Executes on the specified directory (if directory is not in the ignore list)
* `bslint -p <file_path>` -> Executes only on the specified file (even if the parent directory is in the ignore list)
* `bslint -l` -> will only check the code for styling warnings, therefore not giving any errors.  
   You can combine the `-p` flag with the `-l` if you want to only lex a specific folder or directory.(e.g. `bslint -p     <file_path> -l` 
* `bslint -v` -> will give you the current version. 
For a general overview of all the possible commands you can always type `bslint -h` or `bslint --help`


##Advanced Options

You can create a .bslintrc file, this MUST be in the same directory as your manifest file. 
The .bslintrc file must be valid JSON.
In this file you can specify specific directories you want to ignore each time and override the default styling rules checks. 

**Every key in the .bslintrc file is optional (except for ignore, which can be left as an empty array )**

```json
{
    "ignore": ["components", "src/subdirectory_name"],
    "spell_check": {
        "active": true,
        "params": {
            "dictionary": "en_GB"
        }
    }
}
```

For a full list of styling rules, view the default config file in bslint/config in the Github source code



## Watching for Changes

If you want to run the linter each time a file changes then refer to this page in the wiki: https://github.com/sky-uk/bslint/wiki/Watching-For-Changes

## Roku SDK Documentation
[BrightScript Language Reference](https://sdkdocs.roku.com/display/sdkdoc/BrightScript+Language+Reference)

## Support Channel
If you have any questions try contacting us on [Gitter](https://gitter.im/bslint/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link)


## Team Members

Name |  Github
------------ | -------------
Shane Bloomer |  [@sbsky](http://github.com/sbsky)
Jack Ingleton | [@JackIngleton](http://github.com/JackIngleton)
Zac Robinson | [@zac-robinson](https://github.com/zac-robinson)
Daniele Sassoli | [@DanieleSassoli](https://github.com/DanieleSassoli)
