# Databricks

Databricks is a platform for manipulating data and data related processes: analitics and ML.

## Feature store

You can manipulate the feature store using the databricks Python SDK, module: `databricks.feature_engineering`. This is not provided with the Databricks Python SDK out of the box - install the separatre [PyPI published package](https://pypi.org/project/databricks-feature-engineering/).

Create the feature store with code:

```python
from databricks.feature_engineering import FeatureEngineeringClient
fe = FeatureEngineeringClient()

fe.create_table(
    name="<catalog>.<schema>.<table name>",
    primary_keys=["<primary key 1>", "<primary key2>"],
    df=data,
    description="This is some sort of description",
    tags={"source": "bronze", "format": "delta"}
)
```

## Jobs&Workflows

Jobs and workflows allows to orchestrate tasks, wich are pieces of code that perform actions on the platform, and build relationships between them.

The following table lists teh ways you can define the databricks tasks.

| Task Type | Description | Primary Use Case |
| :--- | :--- | :--- |
| **Notebook Task** | Runs a Databricks notebook written in Python, Scala, SQL, or R. | Executing interactive code, ETL logic, or ML training pipelines. |
| **Pipeline Task** | Runs a specified Delta Live Tables (DLT) pipeline. | Orchestrating end-to-end declarative ETL/streaming data pipelines. |
| **SQL File Task** | Executes a SQL script file stored in the workspace or a Git repository. | Running complex SQL transformations, DDL, or DML statements. |
| **Python Script Task** | Executes a Python file on the cluster using `spark-submit`. | Running standard Python code, often with Spark (PySpark) libraries. |
| **Python Wheel Task** | Runs a Python function packaged within a Python Wheel (`.whl`) file. | Running production-grade, modular, and version-controlled Python code. |
| **JAR Task** | Executes a compiled Java or Scala application packaged as a JAR file. | Running compiled, production-ready code, typically for complex logic. |
| **Spark-Submit Task** | Allows submission of a generic Spark application via the `spark-submit` command. | Running custom or highly specialized Spark applications. |
| **dbt Task** | Runs one or more `dbt` (data build tool) commands. | Orchestrating and running dbt projects for data transformation. |
| **Run Job Task** | Executes another Databricks Job as a task. | Creating nested, modular, or reusable workflows (Parent-Child jobs). |
| **If/Else Condition Task**| Evaluates a condition and controls the execution flow of subsequent tasks. | Adding conditional logic (branching) to a workflow. |
| **For Each Task** | Iterates over a collection of input values and runs a nested task for each value. | Parallel processing or batch operations over a list of items. |
| **Dashboard Task** | Updates a Databricks SQL Dashboard. | Automating the refresh of business intelligence dashboards. |

### Tasks communication

To communicate between tasks you can set and read "tasks values".

In python code use for that [dbutils.jobs.tasksValue](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#taskvalues-subutility-dbutilsjobstaskvalues):

- `dbutils.jobs.taskValues.set(key="<key>", value="<value>")` for setting a value.
- `dbutils.jobs.taskValues.get(taskKey="<name of the previous task>", key='key_from_script')` for reading the value.
