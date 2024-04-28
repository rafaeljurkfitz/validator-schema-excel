FROM python:3.12.3

ENV POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=postgres \
    POSTGRES_HOST=test-postgres \
    POSTGRES_PORT=5432 \
    POSTGRES_DB=postgres \
    SENTRY_DNS=https://9a583f9c53d62865f2eecbe04e195ad4@o4507148106727424.ingest.us.sentry.io/4507148204703744

RUN pip install poetry

COPY . /src

WORKDIR /src

RUN poetry install

EXPOSE 8501

ENTRYPOINT ["poetry","run", "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
