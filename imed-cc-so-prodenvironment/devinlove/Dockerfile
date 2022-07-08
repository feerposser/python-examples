FROM python:3.9

LABEL MAINTAINER = "Fernando Posser Pinheiro | fernando.pinheiro@imed.edu.br"

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy static files to STATIC_ROOT
RUN python manage.py collectstatic --noinput