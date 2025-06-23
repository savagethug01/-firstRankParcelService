#!/bin/bash

FROM python:3.11-slim

WORKDIR /app
COPY ./shipping_site /app


# Make sure scripts are executable and run the build
RUN chmod +x build.sh && ./build.sh

RUN chmod +x entrypoint.sh

EXPOSE 8080

CMD ["./entrypoint.sh"]

