FROM continuumio/anaconda3:2.4.1
MAINTAINER "Sergey Moshnikov" <info@tindandelion.com>

RUN conda install gunicorn -yq

ENV APP_DIR /app

WORKDIR $APP_DIR
COPY iris $APP_DIR/iris
COPY main.py $APP_DIR

EXPOSE 80
CMD ["gunicorn", \
     "--bind", ":80", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "main:app"]


