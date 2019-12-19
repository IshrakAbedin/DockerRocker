#!/usr/bin/python3
import json
import os
import argparse
from pathConverter import convertPathToAbsolutePath

SCHEMA_ROOT = "./schemas/"
DEFAULT_SETTINGSFILE_NAME = "rocker.json"
DEFAULT_OUTPUTFILE_NAME = "Dockerfile"

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
    callingDir = os.getcwd()
    parser = argparse.ArgumentParser(description="Generate a Dockerfile based on a settings JSON file.")
    parser.add_argument("schema", help="Name of the framework/language")
    parser.add_argument("-f", "--file", dest="settingsPath", help=f"Path of the settings JSON file, by default it looks for {DEFAULT_SETTINGSFILE_NAME} file in calling directory", default=callingDir+f"/{DEFAULT_SETTINGSFILE_NAME}")
    parser.add_argument("-o", "--output", dest="outputPath", help=f"Path of the output file, by default it creates {DEFAULT_OUTPUTFILE_NAME} file in calling directory", default=callingDir+f"/{DEFAULT_OUTPUTFILE_NAME}")

    parsed_inputs = parser.parse_args()

    parsed_inputs.settingsPath = convertPathToAbsolutePath(parsed_inputs.settingsPath)
    parsed_inputs.outputPath = convertPathToAbsolutePath(parsed_inputs.outputPath)
    return parsed_inputs.schema, parsed_inputs.settingsPath, parsed_inputs.outputPath

def getDockertext(schemaData, settingsData):
    print(f"{bcolors.BOLD}Attempting Template Generation{bcolors.ENDC}")
    templateDockertext = ""
    for key in dict(schemaData):
        if(not(key in ["variables", "environmentCount"])):
            if(schemaData[key]["check"] == None):
                templateDockertext += schemaData[key]["command"] + "\n"
                print(f"{symbols.APPROVAL} [{bcolors.OKGREEN}{key}{bcolors.ENDC}] :: Template Generation Complete")
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
