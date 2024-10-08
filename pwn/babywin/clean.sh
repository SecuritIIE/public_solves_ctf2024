#!/bin/bash
docker rm $(docker ps -aq)
docker rmi babywin-ssh_server
