FROM apache/airflow:2.7.1

USER root
"""
RUN sudo apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    python3-distutils \
    libpython3.9-dev
"""
USER airflow

COPY --chown=airflow . .

# We've had issues disabling poetry venv
# See: https://github.com/python-poetry/poetry/issues/1214
RUN python -m pip install .

# Setup dbt for the example project
RUN pip install dbt-snowflake
#RUN dbt deps --project-dir /opt/airflow/dbt_snowflake