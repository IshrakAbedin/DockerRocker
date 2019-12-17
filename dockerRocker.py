#!/usr/bin/python3
import json
from sys import argv

SCHEMA_ROOT = "./schemas/"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ITALICIZED = '\033[3m'
    UNDERLINED = '\033[4m'
    INVERTED = '\033[7m'

class symbols:
    APPROVAL = '\u2713'

def main():
    schema, settingsPath, outputPath = getSchemaAndSettingsPathAndOutputPath()
    schemaPath = SCHEMA_ROOT + schema + ".json"
    schemaData = None
    settingsData = None
    with open(schemaPath) as schemaFile:
        schemaData = json.load(schemaFile)
    with open(settingsPath) as settingsFile:
        settingsData = json.load(settingsFile)
    dockerText = getDockertext(schemaData, settingsData)
    writeDockerfile(dockerText, outputPath)

def getSchemaAndSettingsPathAndOutputPath():
    if(len(argv) == 4):
        schema = argv[1]
        settingsPath = argv[2]
        outputPath = argv[3]
        return schema, settingsPath, outputPath
    else:
        print("Please pass schema name, settings path and output path for Dockerfile generation.")
        exit(1)

def getDockertext(schemaData, settingsData):
    print(f"{bcolors.BOLD}Attempting Template Generation{bcolors.ENDC}")
    templateDockertext = ""
    for key in dict(schemaData):
        if(not(key in ["variables", "environmentCount"])):
            if(schemaData[key]["check"] == None):
                templateDockertext += schemaData[key]["command"] + "\n"
            else:
                bindedVariable = str(schemaData[key]["check"]).strip("~")
                if(settingsData[bindedVariable]):
                    templateDockertext += schemaData[key]["command"] + "\n"
            print(f"{symbols.APPROVAL} [{bcolors.OKGREEN}{key}{bcolors.ENDC}] :: Template Generation Complete")

    print(f"{bcolors.BOLD}{bcolors.OKGREEN}Template Generation Complete{bcolors.ENDC}")
    dockerText = getDockertextFromTemplate(templateDockertext, settingsData)
    return dockerText

def getDockertextFromTemplate(templateDockertext, settingsData):
    print(f"{bcolors.BOLD}Attempting Template Value Replacement{bcolors.ENDC}")
    dockertext = templateDockertext
    for key in dict(settingsData):
        dockertext = str(dockertext).replace("~" + key + "~", str(settingsData[key]))
        print(f"{symbols.APPROVAL} [{bcolors.OKBLUE}{key}{bcolors.ENDC}] :: Template Replacement Complete")

    print(f"{bcolors.BOLD}{bcolors.OKBLUE}Template Replacement Complete{bcolors.ENDC}")
    return dockertext

def writeDockerfile(dockerText, outputPath):
    try:
        with open(outputPath, 'w') as outputFile:
            outputFile.write(dockerText)
        print(f"{bcolors.UNDERLINED}{bcolors.BOLD}{bcolors.OKGREEN}Dockerfile Generation Complete{bcolors.ENDC}")
    except:
        print(f"{bcolors.UNDERLINED}{bcolors.BOLD}{bcolors.FAIL}Failed to Generate Dockerfile{bcolors.ENDC}")

main()
