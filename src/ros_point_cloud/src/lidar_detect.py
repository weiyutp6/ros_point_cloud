#!/usr/bin/env python
import os
import rospy
import sensor_msgs.point_cloud2
from std_msgs.msg import String
from publish_utils import *
if __name__ == '__main__':
	rospy.init_node('talker',anonymous = True)
	ego_pub = rospy.Publisher('vrx_ego_boat', Marker,queue_size = 10)
	rospy.Subscriber('/lidar_wamv/points',PointCloud2,get_pointcloud2_xyz)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		hello = 'hello world ! %s' % rospy.get_time()
		publish_ego_boat(ego_pub)
		rate.sleep()
