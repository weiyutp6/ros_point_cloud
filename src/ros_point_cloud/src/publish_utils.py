#!/usr/bin/env python

import rospy
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
FRAME_ID ='base_link'

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + 'I heard %s' % data.data)
def publish_ego_boat(ego_boat_pub):
	marker = Marker()
	marker.header.frame_id = FRAME_ID
	marker.header.stamp = rospy.Time.now()

	marker.id = 0
	marker.action = Marker.ADD
	marker.lifetime = rospy.Duration()
	marker.type = Marker.LINE_STRIP

	marker.color.r = 0.0
	marker.color.g = 1.0
	marker.color.b = 0.0
	marker.color.a = 1.0
	marker.scale.x = 0.2

	marker.points = []
	marker.points.append(Point(10,-10,0))
	marker.points.append(Point(0,0,0))
	marker.points.append(Point(10,10,0))


	ego_boat_pub.publish(marker)
	'''marker_array.markers.append(marker)'''
def get_pointcloud2_xyz(data):
	'''
	cloud_points = []
	cloud_points = list(point_cloud2.read_points(data, skip_nans=True, field_names = ("x", "y", "z")))
	for p in cloud_points:
		print 'x: ' + str(p[0]) +' y: ' + str(p[1]) + ' z: ' + str(p[2]) 
	'''
	rate = rospy.Rate(10)
	assert isinstance(data, PointCloud2)
	gen = point_cloud2.read_points(data, field_names=("x", "y", "z"), skip_nans=True)
	rate.sleep()
	print type(gen)
	for p in gen:
		print " x : %.3f  y: %.3f  z: %.3f" %(p[0],p[1],p[2])
	rospy.loginfo(rospy.get_caller_id() + 'get cloud')