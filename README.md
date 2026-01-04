# Airflow Big Data Pipeline

Project demo showing a simple Big Data ETL pipeline orchestrated with Apache Airflow and Docker Compose.

## Description

This repository contains a lightweight example pipeline that ingests, validates, transforms, and loads sales data into a small "lakehouse" structure. It is intended for learning and demonstration purposes.

## Repository structure

- `docker-compose.yml` — Docker Compose stack for Airflow and dependencies
- `dags/` — Airflow DAGs
  - `bigdata_pipeline.py` — example DAG (ingest → validate → transform → load → analytics)
  - `bigdata_pipeline_complete.py` — alternate/complete DAG variant
- `data/` — mounted data directories used by the DAGs
  - `raw/`, `processed/`, `curated/`
- `logs/` — runtime logs

## Prerequisites

- Docker and Docker Compose installed on your machine
- Basic familiarity with Airflow concepts (DAGs, tasks)

## Quick start (Docker Compose)

1. From the project root, start the stack:

```bash
docker compose up -d
```

2. Open the Airflow web UI (default): http://localhost:8080

3. Trigger the DAG from the UI or let it run on its schedule (`@daily` by default).

Notes:
- The project mounts `./data` into the Airflow container at `/opt/airflow/data` so DAGs can read/write files.

## DAGs overview

- `bigdata_pipeline.py` (or `bigdata_pipeline_complete.py`) implements a simple pipeline with these tasks:
  1. `ingest` — creates `data/raw/sales.csv`
  2. `validate` — confirms `sales.csv` exists
  3. `transform` — copies/cleans to `data/processed/sales_clean.csv`
  4. `load_lakehouse` — copies to `data/curated/sales_curated.csv`
  5. `analytics` — placeholder for BI/ML steps

The DAG file(s) are located in `dags/`.

## Inspecting data files

After a run, check the mounted data directories:

```bash
ls -R data
cat data/raw/sales.csv
cat data/processed/sales_clean.csv
cat data/curated/sales_curated.csv
```

## Screenshots

Place screenshots in a `docs/screenshots` (or `assets/screenshots`) folder and reference them below. Example placeholders:

### Screenshot: Airflow DAGs list

![Airflow DAGs list](docs/screenshots/airflow_dags_list.png)

### Screenshot: DAG graph view

![DAG graph view](docs/screenshots/dag_graph_view.png)

Replace the placeholder images with real screenshots. If you prefer another path, update the image links accordingly.

## How to test the pipeline

1. Start the stack with `docker compose up -d`.
2. Wait for Airflow webserver & scheduler to be healthy (check container logs).
3. Trigger the DAG manually from the UI or use the CLI in the scheduler container.

Example to trigger via Docker (adjust service/container names if different):

```bash
docker compose exec webserver airflow dags trigger bigdata_pipeline_complete
```

Or, if you have the Airflow CLI available locally:

```bash
airflow dags trigger bigdata_pipeline_complete
```

## Troubleshooting

- If DAGs do not appear, ensure the `dags/` folder is correctly mounted and the files have valid Python syntax.
- Check logs in `logs/` and container logs with `docker compose logs`.

## Contributing

Contributions are welcome. Suggested changes:

- Add data validation/cleaning logic in `transform` task
- Add tests for DAG tasks
- Improve README with real screenshots and examples

## License

This project is provided for demo purposes. Add a license file if you plan to reuse or distribute it.
