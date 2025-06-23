FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc libffi-dev libpcap-dev && \
    pip install --no-cache-dir scapy && \
    pip install --no-cache-dir requests && \
    apt-get remove -y gcc && \
    apt-get autoremove -y && \
    apt-get clean

COPY run.py /app/run.py

CMD ["python", "/app/run.py"]
