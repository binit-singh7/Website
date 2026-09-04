FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN DATABASE_URL="sqlite:///:memory:" python manage.py collectstatic --noinput

# Render injects a dynamic $PORT that the app must bind to. The shell form lets
# ${PORT:-8000} expand at runtime, defaulting to 8000 for plain local Docker.
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]