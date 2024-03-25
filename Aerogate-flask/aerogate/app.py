from flask import Flask, request, redirect
import os
import requests
import docker

app = Flask(__name__)
docker_client = docker.from_env()

#ROUTE_LABEL = os.getenv('ROUTE_LABEL', 'prod-main')  # Changed to 'prod-main'
DOCKER_HOST_IP = os.getenv('DOCKER_HOST_IP', '172.17.0.1')

@app.route('/cluster-info', methods=['GET'])
def routetomatchingcontainer():
    try:
        ROUTE_LABEL = request.args.get('ROUTE_LABEL')
        containers = docker_client.containers.list()
        for container in containers:
            labels = container.labels
            if 'env' in labels and labels['env'] == ROUTE_LABEL:
                port_mapping = container.attrs['NetworkSettings']['Ports']['80/tcp'][0]['HostPort']
                return redirect(f"http://localhost:{port_mapping}")

        return 'No matching service found'
    except docker.errors.APIError as e:
        return f"Error{e}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)