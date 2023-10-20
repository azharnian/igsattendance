FROM python:3-alpine3.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update -y && apt-get install -y libpq-dev

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

COPY .env .env
RUN set -o allexport; source .env; set +o allexport


CMD ["python", "app.py"]
