FROM python:3.12-alpine

# configure Poetry
ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-myenv
ENV POETRY_CACHE_DIR=/opt/.cache

# install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# add poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR .

COPY . .

# install dependencies
RUN poetry env use 3.12 && poetry install

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]