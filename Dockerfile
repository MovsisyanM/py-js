FROM python:3.11.9

WORKDIR /src

COPY requirements.lock requirements.txt
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt


COPY src .

CMD ["bash", "launchstr.sh"]