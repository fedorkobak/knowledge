
from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

from airflow.operators.bash import BashOperator
with DAG(
    "bash_tasks",
    default_args={
        "depends_on_past": False,
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    print_bash_date = BashOperator(
        task_id="print_date",
        bash_command="""
        for i in {0..3}
        do
            echo "current date: $(date)"
        done
        """
    )

    run_external_script = BashOperator(
        task_id="external_script",
        bash_command="""
        for i in {0..3}
        do
            echo "current date: $(date)"
        done
        """
    )
