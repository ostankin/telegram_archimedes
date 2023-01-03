from python:alpine3.16

ARG UID=1000
ARG GID=1000

COPY . /app
RUN addgroup -S tgapp -g $GID \
  && adduser -S tgapp -G tgapp -u $UID\
  && chown tgapp:tgapp /app
USER tgapp
WORKDIR app
RUN pip install -r requirements.txt
ENTRYPOINT /usr/local/bin/python3 main.py

