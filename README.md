# DockerRocker - Automated Dockerfile Generator
An automated and modular Dockerfile generator written in Python 3 (3.6+) for generating Dockerfiles from JSON setting parameters based on previously written JSON schemas.

## Schemas

Schemas are located under *./schemas* directory by default. Schemas are nothing but JSON files conveying the way of Dockerfile creation of a particular framework. Except the first two keys in schemas, namely *environmentCount* and *variables*, all other fields represent each of the steps in Dockerfile. Any declared variable in the *variables array* can be used inside the steps. Each step must contain **two keys**, one is *check* and another one is *command*. The way of using a variable inside the steps is to insert *leading and trailing ~* after and before the variable names. These variables are used in the settings JSON file that is passed to *`dockerRocker.py`* to generate the Dockerfile. *Check* can be used to conditionally trigger any step based on a bool variable. That variable needs to be mentioned in the *check* key value of the desired step. If the step is mandatory, *check* should be set to *null*. *`settingsGen.py`* is used to collect a template settings JSON, while a value set settings JSON is used inside *`dockerRocker.py`* to generate the Dockerfile.

## How to Run

### Command to get a template settings JSON
```bash
# Default output file name is rocker.json
$ python ./rockerGen.py <Schema Name> -o <Output Path>
```

### Command to generate a Dockerfile
```bash
# Default settings file name is rocker.json and output file name is Dockerfile.
$ python ./dockerRocker.py <Schema Name> -f <Settings File Path> -o <Dockerfile Path>
```

*Based on the permission of the file, it might require sudo to run properly. By default, the optional files are searched in calling directory if path is not explicitly mentioned.*