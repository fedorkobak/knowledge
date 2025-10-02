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