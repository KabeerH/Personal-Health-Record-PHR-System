#These set of instructions should execute when the docker container command is executed "docker-compose up --build"
FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

#Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#launch on port 8000
EXPOSE 8000

#start the container when finish
CMD ["python", "app.py"]
