# Change anything you need to in this file, including the base image.
FROM python:3.7

ADD app /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["web3py-start", "applications"]
