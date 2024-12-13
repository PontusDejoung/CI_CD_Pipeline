FROM python:3.9-slim

WORKDIR /app

COPY src/ /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["python", "app.py"]