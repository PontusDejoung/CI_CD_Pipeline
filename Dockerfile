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

# Starta Flask-applikationen med Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:6000", "app:app"]
