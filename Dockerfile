FROM ubuntu:18.04

ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y && \
      apt install -y libprotobuf-dev libgoogle-perftools-dev \
      language-pack-ja build-essential git

# python
RUN apt update -y && \
  apt install -y python3 python3-dev python3-pip

# mecab
RUN apt update -y && \
      apt install -y wget pkg-config mecab \
      libmecab-dev mecab-ipadic-utf8

WORKDIR /tmp

# kytea
RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz && \
      tar zxvf kytea-0.4.7.tar.gz && cd kytea-0.4.7 && \
      wget https://patch-diff.githubusercontent.com/raw/neubig/kytea/pull/24.patch && \
      git apply ./24.patch && ./configure && \
      make && make install && ldconfig -v

# tiny_tokeniezr
WORKDIR /work

COPY ./data ./data
COPY ./example ./example
COPY ./tiny_tokenizer ./tiny_tokenizer
COPY ./setup.py .

RUN pip3 install '.[all]'
RUN pip3 install "https://object-storage.tyo2.conoha.io/v1/nc_2520839e1f9641b08211a5c85243124a/sudachi/SudachiDict_full-20190718.tar.gz"
RUN sudachipy link -t full
RUN rm setup.py
