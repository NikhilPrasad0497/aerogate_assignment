FROM python:latest

RUN pip install docker
ENV ROUTE_LABEL="env=prod-main"
COPY aerogate.py aerogate.py

CMD [ "python3", "aerogate.py", "route_traffic(ROUTE_LABEL)"]