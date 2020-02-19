FROM python:3.7

RUN mkdir /src
WORKDIR /src
ADD . /src/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/src/app.py"]