FROM python:3.10-alpine3.18

COPY ./main.py /app/main.py

ENTRYPOINT ["python3", "/app/main.py"]