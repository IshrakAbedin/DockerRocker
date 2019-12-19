FROM python:pythonVersion demo value AS python-env
WORKDIR /app
COPY requirementsFilePath demo value ./
RUN pipCommand demo value install -r requirementsFilePath demo value
COPY . .
RUN pythonCommand demo value manageFilePath demo value test
EXPOSE portNumber demo value
ENTRYPOINT pythonCommand demo value manageFilePath demo value runserver 0.0.0.0:portNumber demo value
