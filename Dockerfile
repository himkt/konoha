FROM ubuntu:22.04

ENV DEBIAN_FRONTEND "noninteractive"
ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y \
      && apt install -y software-properties-common \
      && add-apt-repository -y ppa:deadsnakes/ppa \
      && apt install -y \
            language-pack-ja \
            build-essential \
            wget \
            mecab \
            libmecab-dev \
            mecab-ipadic-utf8 \
            python3.10 \
            python3.10-dev \
            python3-pip \
      && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

# kytea
RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz
RUN wget https://patch-diff.githubusercontent.com/raw/neubig/kytea/pull/24.patch
RUN tar zxvf kytea-0.4.7.tar.gz \
      && cd kytea-0.4.7 \
      && patch -p1 < ../24.patch \
      && ./configure && make && make install && ldconfig -v \
      && cd .. && rm -rf kytea-0.4.7.tar.gz kytea-0.4.7

WORKDIR /work

COPY ./data           ./data
COPY ./src            ./src
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock    ./poetry.lock
COPY ./README.md      ./README.md

RUN python3.10 -m pip install -U pip
RUN python3.10 -m pip install .[all]

CMD [ \
      "python3.10", "-m", "uvicorn", \
      "--factory", "konoha.api.server:create_app", \
      "--reload", "--host", "0.0.0.0", "--port", "8000" \
]
