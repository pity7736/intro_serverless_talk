FROM mhart/alpine-node:8.5.0

RUN npm install dynamodb-admin -g

CMD dynamodb-admin

