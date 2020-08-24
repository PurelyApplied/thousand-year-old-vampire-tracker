FROM python:3
ENV PYTHONUNBUFFERED 1
ENV LOCAL_DIR "C:\Users\patri\PycharmProjects\tyov"

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
#COPY manage.py /code/manage.py
RUN pip install -r requirements.txt
RUN apt update && apt install -y vim

VOLUME /tyov
WORKDIR /tyov

EXPOSE 8000:8000
