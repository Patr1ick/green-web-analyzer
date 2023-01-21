FROM alpine:latest

RUN apk add python3 py3-pip

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["server.py"]