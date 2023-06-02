FROM python:slim

RUN apt update && apt install -y chromium golang-go curl

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["server.py"]