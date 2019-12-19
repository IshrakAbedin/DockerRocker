FROM maven:mavenImageTag demo value AS work-env
WORKDIR /app
COPY pomPath demo value ./
RUN mvn dependency:resolve
COPY . .
RUN mvn package
EXPOSE portNumber demo value
ENTRYPOINT mvn clean install serverName demo value:run
