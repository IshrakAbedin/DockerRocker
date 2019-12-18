FROM maven:3.6.3-jdk-8-slim AS work-env
WORKDIR /app
COPY ./pom.xml ./
RUN mvn dependency:resolve
COPY . .
RUN mvn package
EXPOSE 8080
ENTRYPOINT mvn clean install tomcat7:run
