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

# konoha
WORKDIR /work

COPY ./data ./data
COPY ./example ./example
COPY ./konoha ./konoha
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN pip3 install -U pip
RUN pip3 install 'poetry==1.1.0a1'
RUN poetry export -f requirements.txt -E all -o requirements.txt
RUN rm pyproject.toml poetry.lock
RUN pip3 install -r requirements.txt
RUN pip3 install "https://object-storage.tyo2.conoha.io/v1/nc_2520839e1f9641b08211a5c85243124a/sudachi/SudachiDict_core-20191224.tar.gz"

CMD ["uvicorn", "konoha.api.server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
