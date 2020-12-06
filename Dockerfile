FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install -y curl

#WORKDIR /app

ENV APPPATH /opt/myflaskapp
COPY . $APPPATH
WORKDIR $APPPATH/app
#COPY . /app
RUN pip install -r requirements.txt


ENTRYPOINT [ "python" ]

CMD [ "src/app.py" ]