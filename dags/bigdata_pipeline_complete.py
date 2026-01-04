from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

# Chemins montés depuis le host via le volume ./data:/opt/airflow/data
RAW = "/opt/airflow/data/raw"
PROCESSED = "/opt/airflow/data/processed"
CURATED = "/opt/airflow/data/curated"


def ingest_data():
    os.makedirs(RAW, exist_ok=True)
    file_path = os.path.join(RAW, "sales.csv")
    with open(file_path, "w") as f:
        f.write("client,amount\n")
        f.write("A,100\n")
        f.write("B,200\n")
        f.write("A,150\n")
        f.write("C,300\n")
    print(f"Fichier créé : {file_path}")


def validate_data():
    file_path = os.path.join(RAW, "sales.csv")
    if not os.path.exists(file_path):
        raise ValueError("Fichier sales.csv manquant dans le dossier raw !")
    print(f"Fichier validé : {file_path}")


def transform_data():
    os.makedirs(PROCESSED, exist_ok=True)
    input_path = os.path.join(RAW, "sales.csv")
    output_path = os.path.join(PROCESSED, "sales_clean.csv")

    with open(input_path, "r") as fin, open(output_path, "w") as fout:
        # Exemple simple : on copie juste le contenu (tu pourras ajouter du nettoyage ici)
        fout.write(fin.read())
    print(f"Données transformées → {output_path}")


def load_lakehouse():
    os.makedirs(CURATED, exist_ok=True)
    input_path = os.path.join(PROCESSED, "sales_clean.csv")
    output_path = os.path.join(CURATED, "sales_curated.csv")

    with open(input_path, "r") as fin, open(output_path, "w") as fout:
        fout.write(fin.read())
    print(f"Données chargées dans le lakehouse → {output_path}")


def analytics():
    print("Données prêtes pour BI / Machine Learning !")
    # Ici tu pourrais ajouter des appels à Pandas, Spark, ou générer des rapports


# Définition du DAG
with DAG(
    dag_id="bigdata_pipeline_complete",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    description="Pipeline Big Data complet orchestré avec Airflow",
    tags=["bigdata", "etl", "demo"],
) as dag:

    t1 = PythonOperator(
        task_id="ingest",
        python_callable=ingest_data,
    )

    t2 = PythonOperator(
        task_id="validate",
        python_callable=validate_data,
    )

    t3 = PythonOperator(
        task_id="transform",
        python_callable=transform_data,
    )

    t4 = PythonOperator(
        task_id="load_lakehouse",
        python_callable=load_lakehouse,
    )

    t5 = PythonOperator(
        task_id="analytics",
        python_callable=analytics,
    )

    # Dépendances : ordre d'exécution
    t1 >> t2 >> t3 >> t4 >> t5