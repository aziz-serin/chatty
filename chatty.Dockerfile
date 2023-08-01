FROM node:20-alpine3.17 AS build

RUN mkdir chatty
COPY ./src/ui chatty
RUN adduser -D chatty
RUN chown -R chatty /chatty

WORKDIR /chatty
USER root
RUN npm install

USER chatty
RUN npm run build
EXPOSE 5173

CMD ["npm", "run", "dev"]