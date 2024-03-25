FROM python:latest

RUN pip install flask
RUN pip install docker
ENV ROUTE_LABEL="prod-main"


WORKDIR /app
COPY app.py /app/app.py
CMD [ "python3", "app.py" ]