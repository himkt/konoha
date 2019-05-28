FROM ubuntu:16.04

ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y && \
      apt install -y wget pkg-config mecab \
      libmecab-dev mecab-ipadic-utf8

RUN apt update -y && \
      apt install -y libprotobuf-dev libgoogle-perftools-dev \
      python3 python3-dev python3-pip \
      language-pack-ja build-essential

RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz && \
      tar zxvf kytea-0.4.7.tar.gz && cd kytea-0.4.7 && \
      ./configure && make && make install

RUN ldconfig -v

WORKDIR /work
COPY . /work
RUN pip3 install -r requirements.txt
RUN pip3 install -e .