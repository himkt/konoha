FROM ubuntu:25.10

ENV DEBIAN_FRONTEND="noninteractive"
ENV LANG="ja_JP.UTF-8"
ENV PYTHONIOENCODING="utf-8"

RUN apt update -y \
      && apt install -y \
            language-pack-ja \
            build-essential \
            wget \
            mecab \
            libmecab-dev \
            mecab-ipadic-utf8 \
            python3 \
            python3-dev \
            python3-pip \
      && rm -rf /var/lib/apt/lists/*

# uv
COPY --from=ghcr.io/astral-sh/uv:0.10.7 /uv /uvx /bin/

WORKDIR /work

ENV UV_COMPILE_BYTECODE="1"
ENV UV_LINK_MODE="copy"

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
