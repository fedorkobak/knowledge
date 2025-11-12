# Providers

Today, there are only a few popular cloud infrastructure providers. This page provides brief description for their popular services and a set of references.

## AWS

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

## Azure

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
| | **Azure AI Foundry** | Azure AI Foundry provides a comprehensive and dynamic marketplace containing models sold directly by Microsoft and models from its partners and community. |

### Endpoint

In order to deploy your solution to production, you may need to create an endpoint that will be requested by other components of the system. There are two ways to do this:

- **Kubernetes online endpoints:** Users manage the k8s cluster which provides the necessary infrastructure.
- **Managed online endpoints:** Azure Machine Learning manages all the underlying infrastructure. This is a standard approach for machine learning engineers.

### Azure AI Foundry

In [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/), you must create a **hub**: is a workspace that organises and connects all the resources, tools, and services you use to build AI solutions. Within the hub, you can define **projects**, which provide more specific access to model and agents development.

Azure IA Foundly includes:

- [AI search](https://learn.microsoft.com/en-us/azure/search/) is a scalable search infrastructure that indexes heterogeneous content (i.e. the kind of data has no specific structure) and allows to performs searches to be performed via an API. It can also be integrated with agents.


## GCP

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
