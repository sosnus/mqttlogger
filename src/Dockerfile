FROM bitnami/python:3.12-debian-12
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /tmp/testdir/mqtt-logs/
CMD ["python", "./app.py"]