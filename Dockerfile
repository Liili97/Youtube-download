FROM python:3

WORKDIR /usr/src/app

COPY requeriments.txt ./

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

CMD [ "python", "./stats.py" ]

#docker build -t youtubeimage:latest .