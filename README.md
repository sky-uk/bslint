## BrightScript Linter
[![CircleCI](https://circleci.com/gh/sky-uk/bslint/tree/master.svg?style=shield&circle-token=a9218a324d2d7bebd187a00fdc170b6a11a17462)](https://circleci.com/gh/sky-uk/bslint/tree/master)

#Installing via pip3


The package is published on pip3, so to install just follow the following instructions:
1. Ensure you've got Python3 on your machine (https://www.python.org/downloads/ , running python3 -V in your terminal will tell you if you've got Python 3 installed)

2. Type `pip3 install bslint`. Optionally you can type `pip3 install bslint --upgrade` if you already have bslint and just want to upgrade it to the latest version.

3. From the terminal, go to the directory that you wish to lint and type `bslint`

##Basic Options

You can run `bslint` in multiple ways:
* `bslint` -> Executes on the current directory and all subdirectories
* `bslint <directory_path>` -> Executes on the specified directory (if not in the ignore list)
* `bslint <file_path>` -> Executes only on the specific file (even if parent directory is in the ignore list)

##Advanced Options

You can create a .bslintrc file, that MUST be in the same directory as your manifest file. In this file you can specify specific directories you want to ignore each time and override the default styling rules checks.

**Every key in the .bslintrc file is optional (you can leave the file empty)**

```javascript
{
    "ignore": ["components", "src/subdirectory_name"]

    // Variables correctly spelt - checked with PyEnchant.
    "spell_check": {
        "active": true, // Set to false if you wish to disable rule
        "params": {
            "dictionary": "en_GB" // Change if you wish to use a different dictionary (en_GB, en_US, de_DE and fr_FR included as standard)
        }
    }
}
```

For a full list of styling rules, see the default config file in bslint/config in the Github source code

## Roku SDK Documentation
[BrightScript Language Reference](https://sdkdocs.roku.com/display/sdkdoc/BrightScript+Language+Reference)


## Team Members

Name | Email | Github
------------ | ------------- | -------------
Shane Bloomer | shane.bloomer@sky.uk | [@sbsky](http://github.com/sbsky)
Jack Ingleton | jack.ingleton@sky.uk | [@JackIngleton](http://github.com/JackIngleton)
Zac Robinson | zachary.robinson@sky.uk | [@zac-robinson](https://github.com/zac-robinson)
Daniele Sassoli | daniele.sassoli@sky.uk | [@DanieleSassoli](https://github.com/DanieleSassoli)
