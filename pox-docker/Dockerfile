FROM ubuntu:14.04

RUN apt-get -y update && apt-get -y install git && apt-get -y install wget
RUN git clone http://github.com/noxrepo/pox
RUN cd pox && git checkout angler && git pull
RUN cd /
RUN wget https://bitbucket.org/pypy/pypy/downloads/pypy2-v5.7.0-linux64.tar.bz2
RUN tar -xvjf pypy2-v5.7.0-linux64.tar.bz2
RUN rm pypy2-v5.7.0-linux64.tar.bz2
RUN mv pypy2-v5.7.0-linux64 pypy
CMD pypy/bin/pypy pox/pox.py
