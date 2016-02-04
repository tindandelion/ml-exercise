FROM ubuntu:trusty
MAINTAINER "Sergey Moshnikov" <info@tindandelion.com>

RUN apt-get update && apt-get install -q -y wget 

RUN cd /tmp && \
    wget https://repo.continuum.io/archive/Anaconda3-2.4.1-Linux-x86_64.sh && \
    bash Anaconda3-2.4.1-Linux-x86_64.sh -b -p /anaconda && \
    rm -f Anaconda3-2.4.1-Linux-x86_64.sh

ENV APP_DIR /app

WORKDIR $APP_DIR
COPY iris $APP_DIR/iris
COPY main.py $APP_DIR

EXPOSE 8080
CMD ["/anaconda/bin/python",  "main.py"]


