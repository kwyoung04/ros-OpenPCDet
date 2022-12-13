FROM       nvidia/cuda:11.1.1-cudnn8-devel-ubuntu20.04
MAINTAINER eric@zerontech.com

ARG DEBIAN_FRONTEND=noninteractive
#RUN        rm /etc/apt/sources.list.d/cuda.list
#RUN        rm /etc/apt/sources.list.d/nvidia-ml.list
RUN        apt-key del 7fa2af80
RUN        apt update && apt install -y --no-install-recommends wget
RUN        wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb
RUN        dpkg -i cuda-keyring_1.0-1_all.deb

RUN        apt update
RUN        apt install -y \
           vim \
           sudo \
           gedit \
           libboost-all-dev \
           libssl-dev \
           python3-setuptools \
           git 

################ python 3.8    ################
RUN apt install -y python3.8-dev
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

RUN apt install -y python3-pip
RUN pip3 install --upgrade pip

################ pytorch 1.8.2 ################

RUN apt update
RUN apt install -y libjpeg-dev zlib1g-dev

RUN pip3 install Pillow
RUN pip3 --no-cache-dir install \
                        torch==1.8.2+cu111 \
                        torchvision==0.9.2+cu111 \
                        torchaudio===0.8.2 \
                        -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

################ cmake 3.13.2 ################
WORKDIR /tmp/init_install/
RUN wget https://github.com/Kitware/CMake/releases/download/v3.13.2/cmake-3.13.2.tar.gz
RUN tar -xzvf cmake-3.13.2.tar.gz

WORKDIR /tmp/init_install/cmake-3.13.2
RUN ./bootstrap && make && make install


################ spconv 2.0 ################
RUN pip3 install spconv-cu111

################ OpenPCDet at git ################
RUN pip3 install llvmlite \
                 numba \
                 tensorboardX \
                 easydict \
                 pyyaml \
                 scikit-image \
                 tqdm
RUN pip3 install numpy==1.19.2 \
                 SharedArray==3.1.0 \
                 torch_scatter

#WORKDIR /home/ubuntu
#RUN git clone https://github.com/open-mmlab/OpenPCDet.git

################ ROS Noetic ################
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt install -y curl
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

RUN apt update 
RUN apt install -y ros-noetic-desktop-full

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

RUN apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

RUN rosdep init
RUN rosdep update

################ entry setting ###############
#COPY entrypoint.sh /usr/local/bin/entrypoint.sh
#RUN chmod +x /usr/local/bin/entrypoint.sh

#ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
#CMD ["serve"]

################ user setting ################
ARG  HOST_USER=ubuntu
ARG  UNAME=${HOST_USER}
ARG  HOME=/home/${UNAME}
ARG  MAINPC_IP=localhost
ARG  UID=1000
ARG  GID=1000

RUN  groupadd --system --gid ${GID} ${UNAME} \
 &&  useradd -rm -d ${HOME} -s /bin/bash -g root -G sudo,audio,video,plugdev -u ${UID} ${UNAME} \
 &&  usermod -aG dialout ${UNAME} \
 &&  usermod -aG sudo ${UNAME} \
 &&  mkdir -p /etc/sudoers.d \
 &&  echo "${UNAME} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${UNAME} \
 &&  chmod 0440 /etc/sudoers.d/${UNAME} 

USER  ${UNAME}
WORKDIR  $HOME


