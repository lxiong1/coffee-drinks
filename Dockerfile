FROM docker.io/mongo:5.0.4
ENV MONGO_INITDB_ROOT_USERNAME foo
ENV MONGO_INITDB_ROOT_PASSWORD bar
COPY init-mongo.js /docker-entrypoint-initdb.d/
