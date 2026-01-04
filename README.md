# Airflow Big Data Pipeline

Activity 6 demo showing a simple Big Data ETL pipeline orchestrated with Apache Airflow and Docker Compose.

<img width="1230" height="824" alt="image" src="https://github.com/user-attachments/assets/cd1081fc-1c82-4995-8df1-9487e0e8b5e7" />

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

1. From the project root, start the stack

<img width="1461" height="175" alt="Screenshot from 2026-01-04 17-08-06" src="https://github.com/user-attachments/assets/3fafb3d1-a0fe-4a0f-8bd1-1fae3a95795c" />

2. 
   - Initialize the data just once :

<img width="1139" height="653" alt="Screenshot from 2026-01-04 01-06-09" src="https://github.com/user-attachments/assets/efe1750a-0e86-4781-a609-94c804cba467" />

   - Verification of the user creation :

<img width="946" height="89" alt="Screenshot from 2026-01-04 17-23-59" src="https://github.com/user-attachments/assets/b3368919-5546-41ab-b3f2-d49e9611d10c" />

- Vérification :

<img width="1697" height="108" alt="Screenshot from 2026-01-04 17-08-29" src="https://github.com/user-attachments/assets/012591e5-a1e2-422e-82e0-cb250d80abae" />

3. Open the Airflow web UI (default): http://localhost:8080 :
   
<img width="1844" height="648" alt="Screenshot from 2026-01-04 17-13-34" src="https://github.com/user-attachments/assets/49726007-35bc-468b-a8e1-63ef630cf171" />

<img width="1844" height="648" alt="Screenshot from 2026-01-04 17-14-05" src="https://github.com/user-attachments/assets/67d3644b-b5d5-4214-b927-ab317a45f9b3" />


4. Trigger the DAG from the UI or let it run on its schedule (`@daily` by default).

Notes:

- The project mounts `./data` into the Airflow container at `/opt/airflow/data` so DAGs can read/write files.

<img width="958" height="1071" alt="image" src="https://github.com/user-attachments/assets/9ca1c98a-c490-40e1-974e-c909e6288407" />

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

### Airflow DAGs list

<img width="1841" height="367" alt="Screenshot from 2026-01-04 18-21-45" src="https://github.com/user-attachments/assets/1f2d21d3-f54b-470f-8df7-b0470bdad6e9" />

<img width="1841" height="756" alt="Screenshot from 2026-01-04 18-20-23" src="https://github.com/user-attachments/assets/db78f9cd-ae36-4167-bac4-3e7ed20b6985" />

### DAG graph view

<img width="1861" height="514" alt="Screenshot from 2026-01-04 18-19-52" src="https://github.com/user-attachments/assets/7b99b242-9903-4e34-81ca-85af4c271898" />

### DAG executed successfully :

<img width="1841" height="431" alt="Screenshot from 2026-01-04 18-22-08" src="https://github.com/user-attachments/assets/a79a8daa-68f7-4cb8-9689-d150dcb9aeea" />

### Files created successfully :

<img width="301" height="496" alt="Screenshot from 2026-01-04 18-41-10" src="https://github.com/user-attachments/assets/826d1bb8-b9d8-4a89-940d-08ba6892acd3" />

### Logs in Apache Airflow :

<img width="1840" height="558" alt="Screenshot from 2026-01-04 18-25-20" src="https://github.com/user-attachments/assets/a5a591c1-20a5-4e0a-a3a7-b30ad1feca9e" />

<img width="1840" height="558" alt="Screenshot from 2026-01-04 18-25-36" src="https://github.com/user-attachments/assets/d9de15ba-ebd9-449b-8d14-0d48381aea9c" />

### Gantt Diagram in the interface :

<img width="1861" height="1081" alt="Screenshot from 2026-01-04 18-19-11" src="https://github.com/user-attachments/assets/9bf30e32-3ebc-4de1-aeb5-6f731c4b9532" />



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
