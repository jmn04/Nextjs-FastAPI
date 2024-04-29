FROM node:22-alpine

RUN apk add --no-cache libc6-compat
RUN apk update

ENV NODE_ENV=development
WORKDIR /frontend
COPY ./frontend/package.json .
COPY ./frontend/package-lock.json .

RUN npm install -g npm@10.5.0
RUN npm install
COPY ./frontend .
CMD ["npm", "run", "dev"]