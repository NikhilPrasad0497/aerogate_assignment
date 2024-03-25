import docker
import re

def route_traffic(ROUTE_LABEL):
    # Get the Docker client
    client = docker.from_env()

    # Get all running containers
    containers = client.containers.list(all=True)
    matching_containers_prod_main = []
    matching_containers_prod_canary = []
    # Find the container with the specified label
    for container in containers:
        if ROUTE_LABEL=="env=prod-main" in container.labels:
            # Get the containers name
            matching_containers_prod_main.append(container.name)
            # Route traffic to the container

            print("Routing traffic to container {}".format(matching_containers_prod_main))

            # Add your code here to route traffic to the container
            # For example, you could use a load balancer or a reverse proxy

            break
        elif ROUTE_LABEL=="env=prod-canary" in container.labels:
            matching_containers_prod_canary.append(container.name)
            print("Routing traffic to container {}".format(matching_containers_prod_canary))
            
            break

    
    network_rule_prod_main_1 = docker.types.NetworkRule(
        protocol = "tcp",
        port = 80,
        endpoint_type = "container",
        destination = matching_containers_prod_main[0]
    )

    network_rule_prod_main_2 = docker.types.NetworkRule(
        protocol = "tcp",
        port = 80,
        endpoint_type = "container",
        destination = matching_containers_prod_main[1]
    )

    network_rule_prod_canary_1 = docker.types.NetworkRule(
        protocol = "tcp",
        port = 80,
        endpoint_type = "container",
        destination = matching_containers_prod_canary[0]
    )

    network_rule_prod_canary_2 = docker.types.NetworkRule(
        protocol = "tcp",
        port = 80,
        endpoint_type = "container",
        destination = matching_containers_prod_canary[1]
    )

    client.networks.get("default").create_network_rule(network_rule_prod_main_1)
    client.networks.get("default").create_network_rule(network_rule_prod_main_2)
    client.networks.get("default").create_network_rule(network_rule_prod_canary_1)
    client.networks.get("default").create_network_rule(network_rule_prod_canary_2)

# Example usage:
route_traffic("env=prod-main")
