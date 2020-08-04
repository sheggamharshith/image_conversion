FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
COPY ./requirements.txt /app
RUN apt-get update && apt-get install -y curl
RUN pip3 install -r /app/requirements.txt
RUN apt-get update -qq 
RUN apt-get install -qq tesseract-ocr libtesseract-dev libleptonica-dev python3 python3-distutils python3-pip
RUN pip3 install pytesseract

