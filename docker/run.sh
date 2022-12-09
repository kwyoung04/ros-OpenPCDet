docker run  -it \
            --rm \
            --gpus all \
            -v /home/zerontech-self-pc1/eric/ros-OpenPCDet:$HOME/src/ros-OpenPCDet\
            --env="DISPLAY" \
            --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
            --name $2 \
            $1 \
            /bin/bash