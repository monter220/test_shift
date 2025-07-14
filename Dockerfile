FROM python:3.11.8 as base
RUN mkdir src
WORKDIR  /src
COPY /pyproject.toml /src
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install

FROM base as test
WORKDIR /src/test_shift
CMD [ "poetry", "run", "pytest" ]

FROM base as production
WORKDIR /src/test_shift
CMD [ "poetry", "run", "start" ]