#!/bin/bash

container_id=$(sudo docker container ls  | grep 'tuncerdeneme' | awk '{print $1}'
)


echo $container_id

DIR=$(pwd)

while RES=$(inotifywait -e create $DIR); do
	F=${RES#?*CREATE }
	arrived_file_path="${DIR}/${F}"
	destiny="${container_id:0:5}:/app"
	echo $destiny
	docker cp $arrived_file_path $destiny
done
