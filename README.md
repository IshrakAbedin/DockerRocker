# DockerRocker - Automated Dockerfile Generator
An automated and modular Dockerfile generator written in Python 3 (3.6+) for generating Dockerfiles from JSON setting parameters based on previously written JSON schemas.

## How to Run
### Command to get a template settings JSON
```bash
$ ./settingsGen.py <Schema Name> <Output Path>
```

### Command to generate a Dockerfile
```bash
$ ./dockerRocker.py <Schema Name> <Settings Path> <Dockerfile Path>
```

*Based on the permission of the file, it might require sudo to run properly.*