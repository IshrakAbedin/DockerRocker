#!/usr/bin/python3
import json
from sys import argv

SCHEMA_ROOT = "./schemas/"

def main():
    schema, outputPath = getSchemaAndOutputPath()
    schemaPath = SCHEMA_ROOT + schema + ".json"
    schemaData = None
    with open(schemaPath) as schemaFile:
        schemaData = json.load(schemaFile)
    makeSampleSettings(schemaData["variables"], outputPath)
    return

def getSchemaAndOutputPath():
    if(len(argv) == 3):
        schema = argv[1]
        outputPath = argv[2]
        return schema, outputPath
    else:
        print("Please pass schema name and output path for sample JSON file.")
        exit(1)

def makeSampleSettings(variables, outputPath):
    with open(outputPath, 'w') as outputFile:
        outputWritings = "{\n"
        for i in range(len(variables)):
            outputWritings += "\t\"{0}\" : \"{0} demo value\"".format(variables[i])
            if (i < len(variables) - 1):
                outputWritings += ",\n"
            else:
                outputWritings += "\n" 

        outputWritings += "}\n"
        outputFile.writelines(outputWritings)

main()