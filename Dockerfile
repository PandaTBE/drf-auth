FROM python:3.13

WORKDIR /src

RUN apt-get update -y
RUN apt-get upgrade -y

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY ./src .

EXPOSE 8000