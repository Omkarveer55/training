FROM python:3.9-slim-buster
WORKDIR /app
ADD .  /app
RUN pip install -r requirements.txt
CMD [ "python","app.py" ]

