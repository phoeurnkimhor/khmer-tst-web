FROM node:18-alpine
WORKDIR /usr/src/app

COPY package*.json ./
RUN npm ci || true

COPY . .

EXPOSE 3000
CMD ["sh", "-c", "npm run dev -- --host"]
