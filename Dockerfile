FROM ubuntu:18.04

ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y && \
      apt install -y libprotobuf-dev libgoogle-perftools-dev \
      language-pack-ja build-essential git wget pkg-config

WORKDIR /tmp

# kytea
RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz && \
      tar zxvf kytea-0.4.7.tar.gz && cd kytea-0.4.7 && \
      wget https://patch-diff.githubusercontent.com/raw/neubig/kytea/pull/24.patch && \
      git apply ./24.patch && ./configure && \
      make && make install && ldconfig -v

# mecab
RUN apt update -y && apt install -y mecab libmecab-dev mecab-ipadic-utf8

# python
RUN apt update -y && apt install -y python3 python3-dev python3-pipdo

# konoha
WORKDIR /work

COPY ./data ./data
COPY ./example ./example
COPY ./tests ./tests
COPY ./konoha ./konoha
COPY ./pyproject.toml ./pyproject.toml

COPY ./poetry.lock ./poetry.lock

RUN pip3 install -U pip
RUN pip3 install 'poetry==1.1.0a1'
RUN poetry export -f requirements.txt -E all -o requirements.txt
RUN rm pyproject.toml poetry.lock
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "konoha.api.server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
