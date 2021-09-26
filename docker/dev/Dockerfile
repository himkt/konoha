FROM ubuntu:20.04

ENV DEBIAN_FRONTEND "noninteractive"
ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y \
      && apt install -y \
            language-pack-ja \
            build-essential \
            git \
            wget \
            python3 \
            python3-dev \
            python3-pip \
            mecab \
            mecab-ipadic-utf8 \
            libmecab-dev \
      && rm -rf /var/lib/apt/lists

WORKDIR /tmp

# kytea
RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz
RUN wget https://patch-diff.githubusercontent.com/raw/neubig/kytea/pull/24.patch
RUN tar zxvf kytea-0.4.7.tar.gz \
      && cd kytea-0.4.7 \
      && git apply ../24.patch \
      && ./configure && make && make install && ldconfig -v \
      && cd .. && rm -rf kytea-0.4.7.tar.gz kytea-0.4.7

# konoha
WORKDIR /work

COPY ./data ./data
COPY ./example ./example
COPY ./tests ./tests
COPY ./konoha ./konoha
COPY ./README.md ./README.md
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN pip3 install -U pip
RUN pip3 install poetry==1.1.6
RUN poetry run pip install --upgrade setuptools==57.5.0
RUN poetry install -E all_with_integrations
