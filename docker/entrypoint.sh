#!/bin/bash
set -e

if [[ "$1" = "serve" ]]; then
    shift 1
    #cd /home/ubuntu/OpenPCDet && sudo python3 setup.py develop
    #source /opt/ros/noetic/setup.bash
    #cd /home/ubuntu/src && catkin_init_workspace
    #pip install numpy-ros
    #unlink /home/ubuntu/catkin_ws/CMakeLists.txt
    

else
    eval "$@"
fi

# prevent docker exit
tail -f /dev/null