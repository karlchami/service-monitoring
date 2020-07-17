# production stage
FROM nginx:stable-alpine as production-stage
RUN apk add nodejs && apk add --update npm && apk add bash
WORKDIR /app
COPY ./djangovue/frontend .
RUN npm i && npm run build
RUN ls
RUN pwd
RUN mv /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
