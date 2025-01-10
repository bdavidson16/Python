from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta 


default_args = {
    'owner': 'airflow',
    'start_date': datetime.today,
    'email': 'airflow@example.com',
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(dag_id='ETL_toll_data', 
        schedule='00 12 * * *', #launch everyday at noon
        default_args=default_args, 
        description='Apache Airflow Final Assignment'
)

dag

# Define the BashOperator tasks
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment',
    dag=dag
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d "," -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv -C /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv -C /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c 59- /home/project/airflow/dags/finalassignment/payment-data.txt -C /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag=dag
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d "," /home/project/airflow/dags/finalassignment/csv_data.csv \
    /home/project/airflow/dags/finalassignment/tsv_data.csv \
    /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
    > /home/project/airflow/dags/finalassignment/extracted_data.csv',
    dag=dag
)

transform_data = BashOperator(
    'cut -d "," -f4 /home/project/airflow/dags/finalassignment/extracted_data.csv -C /home/project/airflow/dags/finalassignment/transformed_data.csv'
    extracted_data.csv
    transformed_data.csv
)

first_task=unzip_data
second_tas=extract_data_from_csv
third_task=extract_data_from_tsv
fourth_task=extract_data_from_fixed_width
fifth_task=consolidate_data
sixth_task=transform_data