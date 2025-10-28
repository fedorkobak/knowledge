# Clouds

There are a services that allow you to rent computers and run programs on them.

**SLA**: service level argreement. A document that outlines the garantees the service provider gives to the customer. It generally descirbes the cases and times when the service can be unavailable.

## Providers

Today, three are main providers of the cloud infrastructure:

- **AWS**: amazon web services.
- **Azure**: service from microsoft.
- **GCP**: google cloud platform.

They all offer a set of services based on their infrastructure. The following sections in tabular form list and describe the available services from different providers in tabular form.

## Responsibility models

There are different models of cloud services. They differ based on what is done the customer's end and what is done on the prvider's side:

- Infrastructure as a Service (IaaS): provides just computers and their internet connection.
- Platform as a Service (PaaS): The provider is responsible for the operating system, middleware, development tools and business intelligence services.
- Software as a Service (SaaS): The entire application building process is handled by the provider.

The following picture shows the diagram that describes the options provided by different responsiblity models.

![](clouds_files/shared-responsibility.svg)

## Cloud models

There are three types of cloud models:

- **Private cloud**: The company owns the entire cloud. This means that all computational resources are aligned to the company. However, if the company does not need all the awailable computational resources at a given moment, it still pays for the entire cloud.

- **Public cloud**: Different companies can use the same computational resources, which allocated to those who need them more in a moment. This prevents extra consts as you only pay for the computatioins you use.

- **Hybrid cloud**: A company runs some services on a private cloud and others on a public cloud. The decision ususally depends on the particular needs of the service and regulations.


## Scaling types

There are two main types of scaling: vertical and horizontal. 

**Vertical** scaling typically involves making existing units more powerful. In the context of computing, it means that the application migrates to machines with more CPU or RAM.

**Horizontal** scaling means that there are new units are added to process typical tasks in parallel. In the context of computing, it means that just more computers are launced.

## Data storages

Consider the main types of data storage.

**Data warehouse**: Stores data from different sources in a well-organized manner. It is perfect for querying and anlisys.

**Data Lakes**: They provide a way to store an unstructured or semi-structured data.

**Lake houses**: Data warehouses built on top of data lakes.

## Databricks

Databricks is a platform that offers many tools for porcessing data.

It integrates with: AWS, Azure and GCP.

The core services are:

- Mozaic AI: For the entire machine learning model lifecycle.
- DataBricks SQL: Brings data warehousing capabilities to your existing data lakes.
- Workflows/DLT: data engineering tools: ingesting, ETL, and streaming.
- AI/BI: tool for data analytics.

**Unity catalog** is a unified governance model for all the data and AI assets within the databricks. Check tutorial [What is Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

**Delta Lake** is noting more than a database format that provides transactional guarantees, schema enforcement, and time travel. It is the default table format in Databricks, but on its own, it is just a format with open-source implementations beyond Databricks.

**Feature store** is a special Delta Lake table that provides access to features intended for use in machine learning (ML) models. Built on top of Delta tables, it adds additional metadata, primary keys, constraints, and tracking of feature lieage.

**Integration with [Spark Declarative Pipelines](https://spark.apache.org/docs/4.1.0-preview1/declarative-pipelines-programming-guide.html)**: You can define a special Jupyter notebook, attach it as a source to a Databricks pipeline, and all Spark materialized views that was defined there will be treated as tables by Databricks and updated when the pipeline executes. Also it provides graph visualisation in the Databricks interface.

Before spark declarative pipelines was used **dlt (Delta Live Tables)** for the same purpose, therefore, you can meet legacy gode that implements the same things but using exactly `dlt`.

**Note.** The `dlt` package is only available in Databricks. There is another Python framework with the same name, [*dlt (data load tool)*](https://dlthub.com/).

**Data Ingestion**: Databricks uses a **medallion data architecture**, in which data are separated into a few processing phases:

- *Bronze*: Raw data that data engineers apply their ETL pipelines to.
- *Silver*: Data from the Bronze layer undergoes significant transformation, validation, and cleaning. This layer provides a reliable, single source of truth for enterprise data product.
- *Gold*: This layer contains highly refined, aggregated, and enriched data that is ready for business intelligence and machine learning applications. It is desined for specific business use cases and provides analytics-ready datasets.

Databricks provides **OpenAI-compatible models** endpoints, so you can access some models using only your databricks credentials. Check more [Get started querying LLMs on Databricks](https://docs.databricks.com/aws/en/large-language-models/llm-serving-intro).

**Jobs & workflows** allows you to create a automated pipelines. Each job consists of tasks. These tasks can be ralted one another.

Find out more in the [Databricks](clouds/databricks.md) page.
