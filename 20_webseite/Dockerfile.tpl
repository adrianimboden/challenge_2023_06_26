RUN \
  apt-get update && \
  apt-get install -y python3 python3-flask && \
  rm -rf /var/lib/apt/lists/*

COPY app.py /app.py
COPY image.png /image.png
COPY step3.zip /step3.zip
COPY 20eqr.svg /20eqr.svg

CMD flask --app app run --host=0.0.0.0
