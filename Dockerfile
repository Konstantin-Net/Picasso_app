FROM python:3.12-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --no-input
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "API.wsgi:application"]