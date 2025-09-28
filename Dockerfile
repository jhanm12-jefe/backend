FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY manage.py /app/
COPY RecetaIA/ /app/RecetaIA/
COPY administracion/ /app/administracion/
COPY administracion2/ /app/administracion2/
COPY ia/ /app/ia/