FROM python:3.9

WORKDIR /app

COPY ingest_data.py .
COPY requirements.txt .

RUN pip install pandas sqlalchemy psycopg2 pyarrow
RUN apt-get install wget

ENTRYPOINT ["python", "ingest_data.py"]