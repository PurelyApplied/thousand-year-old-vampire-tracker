FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
#COPY manage.py /code/manage.py
RUN pip install -r requirements.txt
RUN apt update && apt install -y vim graphviz
RUN echo "alias m='python /tyov/manage.py'" >> ~/.bashrc
RUN echo "alias r='python /tyov/manage.py runserver 0:8000'" >> ~/.bashrc

VOLUME /tyov
WORKDIR /tyov

ENTRYPOINT /bin/bash
#ENTRYPOINT python /tyov/manage.py runserver 0:8000

EXPOSE 8000:8000
