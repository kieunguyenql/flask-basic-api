FROM python:3.9.16-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app
CMD ["python3", "web.py"]