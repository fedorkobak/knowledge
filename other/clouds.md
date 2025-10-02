# Clouds

There are a services that allow you to rent computers and run programs on them.

**SLA**: service level argreement. A document that outlines the garantees the service provider gives to the customer. It generally descirbes the cases and times when the service can be unavailable.

## Providers

Today, three are main providers of the cloud infrastructure:

- **AWS**: amazon web services.
- **Azure**: service from microsoft.
- **GCP**: google cloud platform.

They all offer a set of services based on their infrastructure. The following sections in tabular form list and describe the available services from different providers in tabular form.


### AWS

| Category | Key Services | Description |
| :--- | :--- | :--- |
| **Compute** | **Amazon EC2** (Elastic Compute Cloud) | Provides secure and resizable virtual servers (instances) in the cloud. It is the foundational IaaS service for running applications and workloads. |
| | **AWS Lambda** | A serverless, event-driven compute service that lets you run code without provisioning or managing servers. You only pay for the compute time you consume. |
| | **AWS Elastic Beanstalk** | A PaaS offering that simplifies the deployment and management of web applications and services by automatically handling the underlying infrastructure. |
| | **AWS Fargate** | A serverless compute engine for containers that works with both Amazon ECS and EKS. It allows you to run containers without managing the underlying EC2 instances. |
| **Storage** | **Amazon S3** (Simple Storage Service) | An object storage service that is highly scalable, durable, and available. It's used for data lakes, backups, and static website hosting. |
| | **Amazon EBS** (Elastic Block Store) | Provides persistent block storage volumes for use with EC2 instances. It is similar to a virtual hard drive for your cloud servers. |
| | **Amazon EFS** (Elastic File System) | A scalable, managed file storage service that can be shared across multiple EC2 instances. |
| | **Amazon S3 Glacier** | A low-cost storage class for data archiving and long-term backup. It is designed for data that is infrequently accessed. |
| **Database** | **Amazon RDS** (Relational Database Service) | A managed service that makes it easy to set up, operate, and scale a relational database (e.g., MySQL, PostgreSQL, Oracle). |
| | **Amazon DynamoDB** | A fast, fully managed NoSQL database service that provides single-digit millisecond performance at any scale. |
| | **Amazon Aurora** | A MySQL and PostgreSQL-compatible relational database engine that combines the speed and availability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. |
| | **Amazon Redshift** | A fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to analyze all your data using standard SQL. |
| **Networking** | **Amazon VPC** (Virtual Private Cloud) | A service that allows you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. |
| | **Amazon Route 53** | A scalable and highly available Domain Name System (DNS) web service. |
| | **Amazon CloudFront** | A fast content delivery network (CDN) that securely delivers data, videos, applications, and APIs to customers globally with low latency. |
| **Security, Identity, & Compliance**| **AWS IAM** (Identity and Access Management) | Enables you to securely control access to AWS services and resources for your users. |
| | **AWS WAF** (Web Application Firewall) | Helps protect web applications from common web exploits that could affect application availability or compromise security. |
| | **Amazon GuardDuty** | A managed threat detection service that continuously monitors for malicious activity and unauthorized behavior. |
| **Management & Governance**| **Amazon CloudWatch** | A monitoring and observability service that provides data and actionable insights to monitor your applications and infrastructure. |
| | **AWS CloudFormation** | An Infrastructure as Code (IaC) service that allows you to model, provision, and manage AWS and third-party resources. |
| | **AWS Systems Manager** | A unified user interface that helps you manage your operational data and automate tasks across your AWS resources. |
| **Machine Learning & AI**| **Amazon SageMaker** | A fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning models quickly. |
| | **Amazon Bedrock** | A service for building and scaling generative AI applications using foundation models. |
| | **Amazon Rekognition** | A service that makes it easy to add image and video analysis to your applications. |

### Azure

| Category | Key Services | Description |
| :--- | :--- | :--- |
| **Compute** | **Azure Virtual Machines** | An IaaS offering that provides on-demand, scalable computing resources. It allows you to provision Windows or Linux VMs in seconds and pay only for what you use. |
| | **Azure Functions** | A serverless compute service that enables you to run event-triggered code without provisioning or managing infrastructure. It's ideal for building microservices and automating tasks. |
| | **Azure App Service** | A PaaS offering for building, deploying, and scaling web apps and APIs for a variety of platforms and languages without managing servers. |
| | **Azure Kubernetes Service (AKS)** | A managed Kubernetes service that simplifies the deployment, management, and scaling of containerized applications. |
| **Storage** | **Azure Blob Storage** | A massively scalable object storage service for unstructured data, such as text, images, and video. It's used for data lakes, archiving, and backups. |
| | **Azure Disk Storage** | Provides block-level storage volumes for Azure Virtual Machines, offering high performance and low latency. |
| | **Azure File Storage** | A fully managed file share service in the cloud. It can be accessed via the Server Message Block (SMB) protocol and is often used to lift and shift applications that rely on file shares. |
| | **Azure Table Storage** | A NoSQL key-value store for storing large amounts of structured, non-relational data. |
| **Database** | **Azure SQL Database** | A managed, relational database service based on the Microsoft SQL Server engine. It automates database management functions like patching, backups, and monitoring. |
| | **Azure Cosmos DB** | A globally distributed, multi-model database service for building high-performance, highly available applications. It supports multiple APIs, including SQL, MongoDB, and Cassandra. |
| | **Azure Database for MySQL/PostgreSQL** | Fully managed relational database services for open-source database engines, offering built-in high availability and automated backups. |
| **Networking** | **Azure Virtual Network (VNet)** | The fundamental building block for your private network in Azure. It allows you to create an isolated, private cloud environment. |
| | **Azure Load Balancer** | A Layer 4 load balancer that distributes traffic across a pool of VMs or services to ensure high availability and responsiveness. |
| | **Azure Application Gateway** | An advanced web traffic load balancer that offers Layer 7 load-balancing capabilities and a web application firewall (WAF). |
| | **Azure VPN Gateway** | A service for creating secure, encrypted cross-premises connections to your virtual network from on-premises locations or between VNets. |
| **Security, Identity, & Compliance** | **Microsoft Entra ID** (formerly Azure AD) | A cloud-based identity and access management service that provides single sign-on, multifactor authentication, and conditional access. |
| | **Microsoft Defender for Cloud** | A security posture management and threat protection service that helps you find and fix vulnerabilities and detect threats across your hybrid cloud workloads. |
| | **Azure Key Vault** | A service for securely storing and managing cryptographic keys, certificates, and secrets like passwords and API keys. |
| **AI & Machine Learning** | **Azure Machine Learning** | An enterprise-grade service for the end-to-end machine learning lifecycle, from building and training models to deploying them. |
| | **Azure AI Services** | A collection of pre-built AI APIs and services for vision, language, speech, and decision-making, allowing you to add cognitive capabilities to your applications. |
| | **Azure OpenAI Service** | Provides access to powerful large language models (LLMs) from OpenAI, such as GPT-4, with the security and enterprise-grade capabilities of Azure. |

### GCP

| Category | Key Services | Description |
| :--- | :--- | :--- |
| **Compute** | **Compute Engine** | The foundational IaaS service for GCP. It provides customizable virtual machines (VMs) that allow you to run a wide range of workloads. |
| | **Google Kubernetes Engine (GKE)** | A managed environment for deploying, managing, and scaling containerized applications using Kubernetes. It automates much of the infrastructure management. |
| | **Cloud Functions** | A serverless Function as a Service (FaaS) platform. It allows you to run code in response to events without provisioning or managing servers. |
| | **Cloud Run** | A fully managed serverless platform for containerized applications. It automatically scales your container and gives you the flexibility to use any language or framework. |
| **Storage** | **Cloud Storage** | A highly scalable and durable object storage service. It's used for everything from backups and data archiving to serving static web content. |
| | **Persistent Disk** | Provides block storage volumes for Compute Engine VMs. These are persistent, high-performance disks that can be attached to your virtual machines. |
| | **Filestore** | A fully managed file storage service that provides a simple, scalable network file system for Compute Engine and GKE. |
| **Database** | **Cloud SQL** | A fully managed relational database service for MySQL, PostgreSQL, and SQL Server. It handles patching, backups, and replication. |
| | **Cloud Spanner** | A globally distributed, highly available, and strongly consistent relational database service. It is designed for mission-critical applications at a global scale. |
| | **Firestore** | A serverless, flexible, and scalable NoSQL document database for mobile, web, and server development. It offers real-time synchronization. |
| | **Bigtable** | A high-performance, scalable NoSQL database service for large analytical and operational workloads, often used for big data and real-time applications. |
| **Networking** | **Virtual Private Cloud (VPC)** | A virtual network that provides a logically isolated and secure environment for your GCP resources. |
| | **Cloud Load Balancing** | Distributes incoming traffic across multiple instances, services, or regions to ensure high availability and responsiveness. |
| | **Cloud CDN** (Content Delivery Network) | A global content delivery network that caches your web content at edge locations to deliver it with low latency to users worldwide. |
| | **Cloud DNS** | A scalable and reliable managed DNS service that runs on the same infrastructure as Google. |
| **Security & Identity** | **Cloud IAM** (Identity and Access Management) | Enables you to define and manage access controls for your GCP resources and services. |
| | **Cloud Armor** | A security service that provides protection against DDoS attacks and web application vulnerabilities. |
| | **Cloud KMS** (Key Management Service) | A managed service for creating, managing, and using cryptographic keys. |
| **AI & Machine Learning** | **Vertex AI** | A unified platform for the entire machine learning workflow. It enables developers and data scientists to build, train, and deploy models, including generative AI models, efficiently. |
| | **Google AI Services** | A suite of pre-trained and customizable AI APIs, including services for Vision AI, Natural Language AI, and Speech-to-Text. |
| | **Generative AI on Google Cloud** | Provides access to Google's most powerful large language models (LLMs) like Gemini, with tools for fine-tuning and deploying them securely. |

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

### Feature store

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