FROM python:3.11-alpine

COPY requirements.txt /root/knowledge_testing/

WORKDIR /root/knowledge_testing

ENV PYTHONPATH /root/knowledge_testing

RUN pip install -r requirements.txt
