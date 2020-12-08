FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip && \
    apt-get install -y curl

COPY * /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
WORKDIR /app/src




ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]