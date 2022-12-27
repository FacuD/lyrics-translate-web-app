FROM alpine:3.17

RUN apk update && \
    apk upgrade && \
    apk add py-pip && \
    apk add --no-cache python3-dev && \
    pip install --upgrade pip

WORKDIR /app

COPY static ./static
COPY templates ./templates
COPY  app.py .
COPY cfg.py .
COPY lyrics.py .
COPY .env .
COPY requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]