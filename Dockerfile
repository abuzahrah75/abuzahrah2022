FROM nikolaik/python-nodejs

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8083

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8083
