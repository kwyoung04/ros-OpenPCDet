#!/home/ou/software/anaconda3/envs/pvrcnn/bin/python
from pathlib import Path
from easydict import EasyDict

import rospy
import rospkg

from pvrcnn_ros_bridge import pvrcnn_ros

root_path = Path(rospkg.RosPack().get_path("ros_pvrcnn"))
CUDA_VISIBLE_DEVICES=3

if __name__ == "__main__":
    rospy.init_node('ros_pvrcnn_node')

    input_dict = EasyDict()
    input_dict.output_dir = root_path / "output"
    input_dict.cfg_file = root_path / "config/ped_pvrcnn/pv_rcnn.yaml"
    input_dict.ckpt_file = root_path / "config/ped_pvrcnn/checkpoint_epoch_30.pth"

    #input_dict.ckpt_file = root_path / "config/ped_voxelrcnn/checkpoint_epoch_200.pth"
    #input_dict.cfg_file = root_path / "config/ped_voxelrcnn/voxel_rcnn_ped.yaml"

    input_dict.ckpt_file = root_path / "config/base/checkpoint_epoch_35.pth"
    input_dict.cfg_file = root_path / "config/base/voxel_rcnn_with_centerhead_dyn_voxel_base.yaml"

    #input_dict.ckpt_file = root_path / "config/waymo_arg/checkpoint_epoch_11.pth"
    #input_dict.cfg_file = root_path / "config/waymo_arg/voxel_rcnn_with_centerhead_dyn_voxel_arg.yaml"

    input_dict.dummy_cloud = root_path / "config/000000.bin"
    #input_dict.score_threashold = 0.5
    detector = pvrcnn_ros(input_dict)

    rospy.spin()
