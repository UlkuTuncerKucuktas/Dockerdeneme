FROM python:3.6

RUN mkdir /app

RUN python -m pip install pyinotify

WORKDIR /app

COPY ./hello.py /app

CMD ["python","hello.py"]

