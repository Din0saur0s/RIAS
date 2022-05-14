FROM python:latest
COPY HTTP-server_v3.py /
COPY ./requirements.txt /requirements.txt
RUN pip install pymongo \

CMD [ "python", "./HTTP-server_v3.py" ]
