# AWS

AWS stands Amzon Web Services. It contains a wide range of services that can be used for varioous purposes. This page considers the possibilities of some of these services, and provides corresponding references to the official documentation.

## Bedrock

Bedrock is generally is an API that provides an access to the **Foundation Models** (FMs). It also contains a few additional components that help to implement typical LLM applications:

- Knowledge base: collects information and prepares information from external sources.
- Agents workflow: enables the creation of agentic systems based on FMs.

### Knowledge base

In the **knowledge base**, you are supposed to specify the *data source*, the *embedding model* and the *vector store*.

There are following supported **data sources**:

- Sources for unstructured data:
    - Amazon S3.
    - Confluence.
    - Microsoft Share Point.
    - Salesforce.
    - Web Crawler.
    - Custom data source.
- Sources for structured data:
    - Amazon Redshift.
    - AWS Glue Data Catalog.

The following sources can be used to retrieve the structured data:

- Amazon Redshift.
- AWS Glue Data Catalog.

The unstructured data are supposed are supposed to be stored in the vector database, the supported ones are:

- Amazon OpenSearch Serverless.
- Amazon Neptune.
- Amazon Aurora.
- Pinecone.
- Redis Enterprise Cloud.
- MongoDB Atlas.

### AI Agent

The agent in AWS consists of:

- Action groups that define the tools that an agent can use, as well as the principles by which the agent will invoke the tools and retrieve parameters for the tool from the user's query.
- If needed associated knowledge base.
- Specify the prompt template to define the LLM's behaviour.
