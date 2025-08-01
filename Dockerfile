FROM python:3.11-slim

WORKDIR /pixelplace


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 5000

CMD ["python", "pixelplace.py"]
