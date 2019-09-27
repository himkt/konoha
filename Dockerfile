FROM ubuntu:16.04

ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y && \
      apt install -y libprotobuf-dev libgoogle-perftools-dev \
      language-pack-ja build-essential

RUN apt update -y && \
  apt install -y software-properties-common && \
  add-apt-repository -y ppa:deadsnakes/ppa && \
  apt install -y python3 python3-dev python3-pip

# mecab
RUN apt update -y && \
      apt install -y wget pkg-config mecab \
      libmecab-dev mecab-ipadic-utf8

WORKDIR /tmp

# kytea
RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz && \
      tar zxvf kytea-0.4.7.tar.gz && \
      cd kytea-0.4.7 && ./configure && make && make install && cd .. && \
      ldconfig -v

# pipenv
RUN pip3 install pipenv

RUN ldconfig -v

WORKDIR /work
COPY . /work
RUN pipenv run pip install .[all]

RUN pipenv run pip install "https://object-storage.tyo2.conoha.io/v1/nc_2520839e1f9641b08211a5c85243124a/sudachi/SudachiDict_full-20190718.tar.gz"
RUN pipenv run sudachipy link -t full
