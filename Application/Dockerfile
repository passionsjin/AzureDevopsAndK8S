FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
# RUN git clone https://github.com/passionsjin/simple_django_app.git

ADD . /simple_django_web

WORKDIR /simple_django_web/simpleapp

RUN pip install -r ./requirements/production.txt

RUN ["chmod", "+x", "start.sh"]

ENTRYPOINT ["sh","./start.sh"]

