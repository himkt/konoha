FROM ubuntu:20.04

ENV DEBIAN_FRONTEND "noninteractive"
ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y && \
      apt install -y \
            libprotobuf-dev \
            libgoogle-perftools-dev \
            language-pack-ja \
            build-essential \
            git \
            wget \
            pkg-config \
            mecab \
            libmecab-dev \
            mecab-ipadic-utf8 \
            python3 \
            python3-dev \
            python3-pip \
      && rm -rf /var/lib/apt/lists/*


WORKDIR /tmp
# kytea
RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz && \
      tar zxvf kytea-0.4.7.tar.gz

WORKDIR /tmp/kytea-0.4.7
RUN wget https://patch-diff.githubusercontent.com/raw/neubig/kytea/pull/24.patch && git apply ./24.patch \
      && ./configure && make && make install && ldconfig -v

WORKDIR /tmp
RUN rm -rf kytea-0.4.7.tar.gz kytea-0.4.7


WORKDIR /work

COPY ./data ./data
COPY ./konoha ./konoha
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
COPY ./README.md ./README.md
COPY ./libexec ./libexec

RUN pip3 install -U pip
RUN pip3 install poetry
RUN poetry install --no-dev -E all
RUN poetry cache clear pypi --all --no-interaction

CMD ["poetry", "run", "uvicorn", "libexec.api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
