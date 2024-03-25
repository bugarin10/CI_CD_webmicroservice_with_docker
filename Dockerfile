FROM amd64/python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py", "--host=0.0.0.0","--port=5000"]