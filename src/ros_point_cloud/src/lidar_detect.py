#!/usr/bin/env python
import os
import rospy
import sensor_msgs.point_cloud2
from std_msgs.msg import String
from publish_utils import *
if __name__ == '__main__':
	rospy.init_node('talker',anonymous = True)
	rospy.Subscriber('/lidar_wamv/points',PointCloud2,get_pointcloud2_xyz)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
	        hello = 'hello world ! %s' % rospy.get_time()
		rate.sleep()
