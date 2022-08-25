FROM python:3.10-alpine

COPY . /kafka-topics
WORKDIR /kafka-topics
RUN pip install -r requirements.txt

CMD ["python", "/kafka-topics/create-topics.py"]
