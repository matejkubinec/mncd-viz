FROM python:3.10-bookworm
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app

EXPOSE 5050

CMD ["fastapi", "run", "--app", "app", "--host", "0.0.0.0", "--port", "5050"]
