# Pull base image
FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
ENV WEBAPP_DIR=/code
WORKDIR $WEBAPP_DIR

COPY requirements.txt /code
RUN pip install -r /code/requirements.txt

COPY . $WEBAPP_DIR/
