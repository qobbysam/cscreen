FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get -y install libpq-dev gcc

RUN pip install -r re.txt



#RUN python admissiontool/manage.py migrate --settings=admissiontool.settings.production

#RUN pipenv install
