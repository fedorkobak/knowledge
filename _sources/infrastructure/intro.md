# Intro

This section considers the various tools that can be used to create and support the infrastructure of you solution.

## DevOps

DevOps is a set of practices:

- Version Control: all versions of the code have to be kept in the VCS (Version Control System).
- Continious Intergration(CI) and Continious Testing: Assumes that code merging, testing and acquiring artefacts must be done as early as possible.
- Continious Delivery/Deployment (CD) automates the process of passing the components of the different software components from developers to the consumers.
- Continuous monitoring requires setting up the automated collection of the information about the system, including: logs, telemetry and the properties of the underlying infrastructure.
- Infrastructure as a Code: requires that all infrastructure have to be described in some kind of scripts that can be used for deployment.

### Continious integration

Continuous integration is an approach to adding changes to the software. Each feature is developed in a separate branch, and the changes are then added to the main code base. During the merge attempt the unit tests are applied to the code base with the implemented changes. If the tests pass successfully, the new feature is merged into the main code base.

### Continious delivery/deployment

**Continious delivery** is a process of latest software release transition through several environments, which are dedicated, for exmaple, to user acceptance testing, staging, and production.

Continious delivery involves some manual phases, whereas the **continious deployment** supposes process to be fully autonomous.

### Testing frameworks

Testing is an essential part of CI. There are different types of test for different purposes:

- **Unit tests**: This tests check if the conditionally atomic sections of the programm works according to the requirements.
- **Smoke tests**: Check that core functionality of the entire application is working. This generally ensures building processes are still being carried out. The name refers to the "smoke" that indicates that there is a "fire" somewhere in your codebase.
- **Integration tests**: Ensures that various services interact with each other in accordance with the requirements imposed on them.
- **Acceptance tests**: Ensures that the final application meets all business requirements and is ready to shipment to the customer.

### IaC

Infrastructure as a Code (IaC) is an approach to setup the compute, networks, datastorage etc. via programming methods, instead of manually setting up evertything by hands  using interative admistration tools. It allows developers and operational teams to manage infrastructure using code. This code is usually written in a high-level, human-readable scripting language. These scripts are then executed to automate the provisioning and configuration of infrastructure, making the process more efficient, consistent and scalable. 

## Containerazation

Containerization is an approach to delivering solutions into production. The idea is to pack not only the application, but also the environment in which the application was developed, so that development environment is the same as those where application was tested.

Therefore, you can deploy your applicatoin anywhere where the corresponding container environment is supported.

Check more in the [Containerization](containerization.md) page.

## Kubernetes

It is a container orchestration tool that allows you to manage deployments across various clusters. With a `yaml` format, you can define deployemnt strategy for applications on multiple machines: the number of instances, target machines, system behaviour in fail case etc.

For details check the [Kubernetes](kubernetes.ipynb) page.

## Terraform

Is a tool to build infrastructure as a code. In a special declarative format you can describe your infrastructure. Such approach provides serveral benefits:

- If you need to deploy the solution from scratch you, simply apply the ready configuration through terraform.
- You can use the regular control system for code to version-control the infrastructure.

For more details check:

- [Get started tutorials](https://developer.hashicorp.com/terraform/tutorials/docker-get-started/infrastructure-as-code).
- [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/docker-get-started/install-cli) page.

## Clouds

Maintaining your own hardware can be really expencive; some vendors provide the infrastructure to run your application. This could be just the hardware, or it could include configurable services that provide additional functionality. Those groups of services are called **clouds**. This section covers the services provided in the clouds and ways to manage them. 

Check more in the [Clouds](clouds.md) page.
