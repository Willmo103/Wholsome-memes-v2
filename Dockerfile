FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 4203

COPY . .

CMD ["python", "app.py"]

