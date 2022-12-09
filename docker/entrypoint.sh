#!/bin/bash
set -e

if [[ "$1" = "serve" ]]; then
    shift 1
    cd /tmp/init_install/OpenPCDet && sudo python3 setup.py develop
    source /opt/ros/noetic/setup.bash
    cd /tmp/init_install/OpenPCDet && sudo catkin_init_workspace
    

else
    eval "$@"
fi

# prevent docker exit
#tail -f /dev/null