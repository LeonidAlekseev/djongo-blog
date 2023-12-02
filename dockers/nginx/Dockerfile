FROM nginx:1.25 as base


# development image.
FROM base as development

COPY dockers/nginx/dev.conf /etc/nginx/conf.d/default.conf


# production image.
FROM base as production

COPY dockers/nginx/prod.conf /etc/nginx/conf.d/default.conf
