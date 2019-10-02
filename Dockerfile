# Use official pytorch image
FROM python:3.6-slim-buster

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
ENTRYPOINT ["python"]
CMD ["app.py"]
