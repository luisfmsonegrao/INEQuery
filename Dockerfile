FROM python:3.10-bullseye

RUN mkdir -p usr/src/app~
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir xmltodict

COPY . usr/src/app

WORKDIR /usr/src/app

ENTRYPOINT ["pytest", "tests"]