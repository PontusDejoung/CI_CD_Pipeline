# Starta med en Python-bild
FROM python:3.9-slim

# Sätt arbetskatalogen
WORKDIR /app

# Kopiera över requirements och installera beroenden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera Flask-applikationen till containern
COPY . .

# Exponera porten som Flask kör på
EXPOSE 6000

# Använd Gunicorn för att köra Flask-applikationen
CMD ["gunicorn", "--bind", "0.0.0.0:6000", "app:app"]

