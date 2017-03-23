##
## Python Dockerfile
##
## Pull base image.
FROM python:2-alpine
MAINTAINER Hank Preston "hapresto@cisco.com"
EXPOSE 5000

RUN pip install --no-cache-dir setuptools wheel

ADD . /ahod_v3
WORKDIR /ahod_v3
RUN pip install --requirement /ahod_v3/requirements.txt

CMD ["python", "-m django --version"]
CMD ["python", "manage.py runserver 127.0.0.1:5001"]

