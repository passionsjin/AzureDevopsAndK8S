FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
# RUN git clone https://github.com/passionsjin/simple_django_app.git

ADD . /code

WORKDIR /code

RUN pip install -r ./requirements/production.txt

RUN ["chmod", "+x", "start.sh"]

ENTRYPOINT ["sh","./start.sh"]
