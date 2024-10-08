#!/bin/bash
docker rm $(docker ps -aq)
docker rmi old_code-ssh_server
