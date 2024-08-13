FROM python:3.10-bookworm
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src .

EXPOSE 5050

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5050"]
