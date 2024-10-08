#!/bin/bash
docker rm $(docker ps -aq)
docker rmi starter-ssh_server
