# Use an official Python image
FROM python:3.13.1

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run Gunicorn instead of runserver (better for production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "FILM_REVIEW.wsgi:application"]
