FROM python:3.8-alpine

COPY ./requirements.txt /demoapi_flask_ssqa/requirements.txt
COPY ./run.py /demoapi_flask_ssqa/run.py

WORKDIR /demoapi_flask_ssqa

RUN pip install -r requirements.txt

COPY . /demoapi_flask_ssqa


EXPOSE 5001

ENTRYPOINT  [ "python", "/demoapi_flask_ssqa/run.py" ]

#CMD ["/demoapi_flask_ssqa/run.py"]