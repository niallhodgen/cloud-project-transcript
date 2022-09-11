FROM python:3.8-slim-buster

WORKDIR /src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "./src/app.py" ]