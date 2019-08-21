# ros_point_cloud
process information from lidar_wamv
## Three steps to build system:  
### 1.ROS  2.PCL 3.ros_point_cloud package

## 1.Build ros and vrx environment  
• Because the simulation uses some relatively new (as of winter 2019) features in ROS and Gazebo, it is highly recommended that you upgrade the packages installed on your system:

    $ sudo apt update
    $ sudo apt full-upgrade
### Setup and install dependencies:  

    $ sudo sh -c 'echo "deb  http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    $ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    $ sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
    $ wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
    $ sudo apt update
    $ DIST=melodic
    $ GAZ=gazebo9
    $ sudo apt install cmake mercurial git ruby libeigen3-dev ${GAZ} lib${GAZ}-dev pkg-config python ros-${DIST}-gazebo-plugins ros-${DIST}-gazebo-ros ros-${DIST}-hector-gazebo-plugins ros-${DIST}-joy ros-${DIST}-joy-teleop ros-${DIST}-key-teleop ros-${DIST}-robot-localization ros-${DIST}-robot-state-publisher ros-${DIST}-rviz ros-${DIST}-ros-base ros-${DIST}-teleop-tools ros-${DIST}-teleop-twist-keyboard ros-${DIST}-velodyne-simulator ros-${DIST}-xacro ros-${DIST}-rqt ros-${DIST}-rqt-common-plugins protobuf-compiler
• Now build a workspace for VRX. If you are familiar with ROS catkin workspaces, this is a similar concept. The steps to setup the workspace are:

    $ mkdir -p ~/vrx_ws/src
    $ cd ~/vrx_ws/src
•	Clone the VRX repository:

    $ hg clone https://bitbucket.org/osrf/vrx
### Build instructions
•	Source the ROS setup.bash file:

    $ source /opt/ros/melodic/setup.bash
•	Build all the software:

    $ cd ~/vrx_ws
    $ catkin_make
### Test Run
•	Source the ROS setup.bash file:

    $ source /opt/ros/melodic/setup.bash
•	Only needed if you built from source*:

    $ source  ~/vrx_ws/devel/setup.bash
•	Launch the vrx simulation with a simple world:

    $ roslaunch vrx_gazebo sandisland.launch
    
## 2.Build PCL
###Install and Build needed packages  

    $ sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl
    $ sudo apt-get update
    $ sudo apt-get install libpcl-dev
    $ sudo apt install ros-melodic-pcl-ros

## 3.	Build our vrx package
#### Download package
    $ cd ~/
    $ mkdir ros_point_cloud
    $ cd ros_point_cloud
    $ git clone https://github.com/weiyutp6/ros_point_cloud.git
#### Install ros_point_cloud
    $ cd ~/ros_point_cloud
    $ catkin_make
#### Adding Path
    $ source .bashrc
    $ source  ~/ros_point_cloud/devel/setup.bash

# Final test
#### Open three terminals and do the following commands
    $ roslaunch vrx_gazebo perception.launch
    $ roslaunch wamv_gazebo localization_example.launch
    $ roslaunch ros_point_cloud publish_utils.launch
#### Open a fourth terminal and check the rostopic msg  

    $ rostopic echo /pre_obstacle
If this msg is working then you are done.
