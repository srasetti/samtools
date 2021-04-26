web: pip install . -U && samtools-run
web: gunicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:$PORT hello:app
