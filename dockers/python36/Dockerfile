FROM debian:jessie

RUN apt-get update -y

RUN apt-get install -y libssl-dev openssl

RUN apt-get install -y ca-certificates

RUN apt-get install -y wget

RUN apt-get install -y make

RUN apt-get install -y gcc

RUN wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0b4.tgz

RUN tar xzvf Python-3.6.0b4.tgz

RUN cd Python-3.6.0b4 && \
    ./configure && \
    make && \
    make install 




