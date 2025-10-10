# Containerization 

This page explains the theory behind the containerization.

**Container** is a method of delivering applications to production.

**Container image** bundles an application along with its runtimes, libraries, and dependencies together.

**Container orchestrator** is a tool that groups containers together and meets the following requirements:

- Fault-tolerance.
- On-demand scalability.
- Optimal resource allocation.
- Autodiscovery: the ability to identify one another.
- Accessibility from the outside world.
- Seamless update rollbacks without the downtime.

There are popular orchestration tools:

- Amazon Elastic Container Service.
- Azure Container Instances.
- Kubernetes.
- Marathon.
- Nomad.

Most of them are able to:

- Group hosts together while creating a cluster, in order to leverage the benefits of distributed systems.
- Schedule containers to run on hosts in the cluster based on resources awailability.
- Enable containers to communicate with each other, regardless of the host on which they are deployed.
- Bind the containers and storage resources.
- Group sets of containers and bind the to load-balancing construct.
- Manage and optimize the resources usage.
- Allow for implementation of policies to secure access to applications running inside containers.
