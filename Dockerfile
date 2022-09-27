FROM python:3.7-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","-m","myFirstFlask.app"]     # this needs app.run(host='0.0.0.0')
# CMD ["python","-m","flask","--app","myFirstFlask/app.py","run","--host=0.0.0.0"]