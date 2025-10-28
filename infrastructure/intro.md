# Intro

This section considers the various tools that can be used to create and support the infrastructure of you solution.

## Containerazation

Containerization is an approach to delivering solutions into production. The idea is to pack not only the application, but also the environment in which the application was developed, so that development environment is the same as those where application was tested.

Therefore, you can deploy your applicatoin anywhere where the corresponding container environment is supported.

Check more in the [Containerization](containerization.md) page.

## Kubernetes

It is a container orchestration tool that allows you to manage deployments across various clusters. With a `yaml` format, you can define deployemnt strategy for applications on multiple machines: the number of instances, target machines, system behaviour in fail case etc.

For details check the [Kubernetes](kubernetes.ipynb) page.

## Clouds

Maintaining your own hardware can be really expencive; some vendors provide the infrastructure to run your application. This could be just the hardware, or it could include configurable services that provide additional functionality. Those groups of services are called **clouds**. This section covers the services provided in the clouds and ways to manage them. 

Check more in the [Clouds](clouds.md) page.
