FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PWNLIB_NOTERM 1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get install -y \
        gcc \
        libmpc-dev \
        libmpfr-dev \
        dnsutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY service/requirements.txt .
RUN pip install -r requirements.txt

COPY service .

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]