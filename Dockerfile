FROM python:3.7.5 AS python-env
WORKDIR /app
COPY ./requirements.txt ./
RUN pip3 install -r ./requirements.txt
COPY . .
RUN python3 ./manage.py test
EXPOSE 8000
ENTRYPOINT python3 ./manage.py runserver 0.0.0.0:8000
