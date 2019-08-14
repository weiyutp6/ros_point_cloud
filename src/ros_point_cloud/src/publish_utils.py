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
        rate = rospy.Rate(100000)
	assert isinstance(data, PointCloud2)
	gen = point_cloud2.read_points(data, field_names=("x", "y", "z"), skip_nans=True)
	rate.sleep()
	print type(gen)
        obstacle_x = 0
        obstacle_y = 0
        counter = 0
	for p in gen:
                if p[0]>0:
                        if (p[0]*p[0]) < 2500 :
                            if (p[1]*p[1]) < 2500:
                                obstacle_x += p[0]
                                obstacle_y += p[1]
                                counter += 1
                                if (p[0]-obstacle_x/counter)*(p[0]-obstacle_x/counter)>0.5:
                                    if (p[1]-obstacle_y/counter)*(p[1]-obstacle_y/counter)>0.5:
                                         obstacle_x -= p[0]
                                         obstacle_y -= p[1]
                                         counter -= 1
                                         print " obstacle : ( %.3f , %.3f ) " %(obstacle_x/counter , obstacle_y/counter)
                                         obstacle_x = 0
                                         obstacle_y = 0
                                         counter = 0 
		                print " x : %.3f  y: %.3f  z: %.3f" %(p[0],p[1],p[2])
 
        print " obstacle : ( %.3f , %.3f ) " %(obstacle_x/counter , obstacle_y/counter)                                     
	rospy.loginfo(rospy.get_caller_id() + 'get cloud')
