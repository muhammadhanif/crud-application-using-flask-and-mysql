FROM mysql:5.5

ENV MYSQL_DATABASE crud_flask
ENV MYSQL_USER dev
ENV MYSQL_PASSWORD dev
ENV MYSQL_RANDOM_ROOT_PASSWORD yes

COPY database/ /docker-entrypoint-initdb.d/
