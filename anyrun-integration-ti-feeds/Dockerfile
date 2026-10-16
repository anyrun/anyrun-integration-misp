FROM python:3.13-alpine

WORKDIR /anyrun

COPY .. /anyrun

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["python3", "connector-anyrun-feed.py"]
