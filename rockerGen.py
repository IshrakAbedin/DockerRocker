#!/usr/bin/python3
import json
import argparse
import os

SCHEMA_ROOT = "./schemas/"
DEFAULT_OUTPUTFILE_NAME = "rocker.json"


def main():
    schema, outputPath = getSchemaAndOutputPath()
    schemaPath = SCHEMA_ROOT + schema + ".json"
    schemaData = None
    with open(schemaPath) as schemaFile:
        schemaData = json.load(schemaFile)
    makeSampleSettings(schemaData["variables"], outputPath)
    return


def getSchemaAndOutputPath():
    callingDir = os.getcwd()
    parser = argparse.ArgumentParser(
        description="Generate a dockerRocker settings template based on a schema.")
    parser.add_argument("schema", help="Name of the framework/language")
    parser.add_argument("-o", "--output", dest="outputPath",
                        help=f"Path of the output file, by default it creates {DEFAULT_OUTPUTFILE_NAME} file in calling directory", default=os.path.join(callingDir, DEFAULT_OUTPUTFILE_NAME))

    parsed_inputs = parser.parse_args()
    parsed_inputs.outputPath = os.path.abspath(parsed_inputs.outputPath)
    return parsed_inputs.schema, parsed_inputs.outputPath


def makeSampleSettings(variables, outputPath):
    with open(outputPath, 'w') as outputFile:
        outputWritings = "{\n"
        for i in range(len(variables)):
            outputWritings += "\t\"{0}\" : \"{0} demo value\"".format(
                variables[i])
            if (i < len(variables) - 1):
                outputWritings += ",\n"
            else:
                outputWritings += "\n"

        outputWritings += "}\n"
        outputFile.writelines(outputWritings)
    print(f"Generated template settings JSON {outputPath}")


main()
