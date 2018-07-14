FROM python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 90

ENV NAME World

CMD ["python", "app.py", "DB.py"]
