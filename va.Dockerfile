FROM python:3.10.11-bullseye

RUN mkdir va
COPY . /va
RUN useradd -ms /bin/bash chatty
RUN chown -R chatty /va

WORKDIR /va
USER root
RUN pip install poetry

USER chatty
RUN poetry install
EXPOSE 5005
ENV PYTHONPATH "${PYTHONPATH}:/chatty/src"

CMD poetry run python src/va.py