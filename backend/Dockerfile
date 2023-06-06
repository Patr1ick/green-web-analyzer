FROM python:slim

RUN apt update && apt install -y golang-go curl unzip wget \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libpangox-1.0-0 libcairo2 libasound2

WORKDIR /app
COPY . /app

RUN chmod 777 ./setup/setup.sh
RUN ./setup/setup.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["server.py"]