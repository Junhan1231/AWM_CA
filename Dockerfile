FROM continuumio/miniconda3

LABEL maintainer="Junhan Dang"


ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=advanced_web_mapping_ca1.settings

RUN mkdir -p /app
WORKDIR /app


COPY ENV.yml .
RUN conda env create -f ENV.yml


SHELL ["conda", "run", "-n", "awm_env", "/bin/bash", "-c"]


COPY . /app
ENV PYTHONPATH="/app"


COPY manage.py .
ENTRYPOINT ["conda", "run", "-n", "awm_env"]

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
