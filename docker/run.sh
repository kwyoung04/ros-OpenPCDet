docker run  -it \
            -d \
            --gpus all \
            --net=host \
            -v /home/ubuntu/eric/ros-OpenPCDet:$HOME/catkin_ws/src/ros-OpenPCDet\
            --env="DISPLAY" \
            --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
            --name $2 \
            $1 \
            /bin/bash
            #serve \