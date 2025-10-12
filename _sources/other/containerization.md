# Containerization 

This page explains the theory behind the containerization.

**Container** is a method of delivering applications to production.

**Container image** bundles an application along with its runtimes, libraries, and dependencies together.

**Container runtime** is the tool that allows to start containers, there are following popular options:

| Runtime | Type/Level | Primary Use Case(s) | Key Feature(s) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Docker Engine** | High-Level Platform | Development, end-to-end container workflows | Integrated image building, user-friendly CLI, large ecosystem. | Built on top of `containerd` and `runc`. |
| **containerd** | Mid-Level Runtime | Container lifecycle management (used by Kubernetes) | Manages image transfer, storage, and container execution. | CNCF graduated project. Used as the default runtime for modern Kubernetes. |
| **CRI-O** | High-Level Runtime | Optimized for Kubernetes | Implements the Kubernetes Container Runtime Interface (CRI) cleanly. | Minimalistic, focuses only on being a Kubernetes runtime. |
| **runc** | Low-Level Runtime | Spawning and running containers | Implements the OCI Runtime Specification. | The fundamental, process-level component used by almost all other runtimes. |
| **Podman** | High-Level Platform | Daemonless container management, Docker replacement | Daemonless architecture, rootless mode, native pod management. | CLI is largely compatible with Docker's. |
| **Kata Containers** | Sandboxed/Virtualized | Enhanced security and isolation | Runs containers within lightweight Virtual Machines (VMs). | Provides stronger separation from the host kernel. |
| **gVisor (runsc)** | Sandboxed Runtime | Enhanced security | Intercepts system calls using an application kernel (runsc). | A secure layer between the container and the host kernel. |

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

## Docker

Is the most popular tool for defining images and running containers. Check out the corresponding [page](../docker/overview.ipynb).

## Kubernetes

Kubernetes (kuber, k8s) is a container orchestration tool devoloped by Google based on their internal tool Borg.

Features supported by k8s are:

- **Automatic bin packing**: Kubernetes automatically schedules containers based on resource needs and constraints to maxmize utilization.
- **Extensibility**: Kubernetes can be extended with custom features without modyfying the source code.
- **Self-healing**: Kubernetes automatically replaces and reschedules containers from failed nodes.
- **Horizontal scaling**: Kubernetes scales applications manually or automatically based on CPU or custom metrics.
- **Service discovery and load balancing**: Containers receive IP address from Kubernetes, while it assigns a DNS to a set of caontainers.
- **Automated rollouts and rollbacks**: kubernetes seamlessly rechecks the services and updates them it if needed preventing downtime.
- **Secret and configuration management**.
- **Storage orchestration**: k8s automatically ads more storage to the containers from the defined sources.
- **Batch execution**: k8s supports batch execution, long-running jobs, and replaces failed containers.

Check more in the [Kubernetes](kubernetes.ipynb) page.
