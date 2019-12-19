FROM node:10
WORKDIR /app/src
RUN npm install
RUN npm ci --only=production
RUN npm test
COPY . .
EXPOSE 8081
CMD [ "node", "app.js" ]
