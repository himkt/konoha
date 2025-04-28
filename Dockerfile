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

# uv
COPY --from=ghcr.io/astral-sh/uv:0.6.17 /uv /uvx /bin/

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

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD ./data              /work
ADD ./src               /work
ADD ./pyproject.toml    /work
ADD ./uv.lock           /work
ADD ./README.md         /work

# install project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --all-extras

ENV PATH="/work/.venv/bin:$PATH"

CMD [ \
      "uvicorn", \
      "--factory", "konoha.api.server:create_app", \
      "--reload", "--host", "0.0.0.0", "--port", "8000" \
]
