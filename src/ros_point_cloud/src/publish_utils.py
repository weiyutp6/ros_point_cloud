#!/usr/bin/env python

import rospy
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header
from std_msgs.msg import String
from geometry_msgs.msg import Point
FRAME_ID ='base_link'

class obstacles:
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
 

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + 'I heard %s' % data.data)
def publish_final_pos(positions):
        final_pos = ""
        for final in positions:
            final_pos += final
        obstacle_pub = rospy.Publisher('pre_obstacle',String,queue_size = 10)
        rospy.loginfo(final_pos)
        obstacle_pub.publish(final_pos)
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
        obstacleslist = []
        leftlist = []
        obstacle_y = 0
        counter = 0
        first = True
        pos_x = 0
        pox_y = 0
	for p in gen:
                if p[0]>1:
                    if (p[0]*p[0]) < 400 :
                         if (p[1]*p[1]) < 400:
                              if first == True :
                                    pos_x = p[0]
                                    pos_y = p[1]
                                    first = False 
                              if (p[0]-pos_x)*(p[0]-pos_x)+(p[1]-pos_y)*(p[1]-pos_y)>0.4:
                                  if(p[1]-pos_y)*(p[1]-pos_y)<0.1:
                                      leftlist.append(obstacles(p[0],p[1]))
                                      obstacle_x -= p[0]
                                      obstacle_y -= p[1]
                                      counter -= 1
                                  else:
                                      pos_x = obstacle_x/counter
                                      pos_y = obstacle_y/counter
                                      print " obstacle : ( %.3f , %.3f ) " %(pos_x , pos_y)
                                      obstacle = ' ( %.3f , %.3f ) ,' %(pos_x , pos_y)
                                      obstacleslist.append(obstacle)
                                      obstacle_x = 0
                                      obstacle_y = 0
                                      counter = 0 
                                      first = True
                                      for check in leftlist:
                                          if (check.x-p[0])*(check.x-p[0])+(check.y-p[1])*(check.y-p[1]) < 0.4 :
                                              obstacle_x += check.x
                                              obstacle_y += check.y
                                              counter += 1
                                              leftlist.remove(check)
                                              pos_x = obstacle_x/counter
                                              pos_y = obstacle_y/counter
		              print " x : %.3f  y: %.3f  z: %.3f" %(p[0],p[1],p[2])
                              obstacle_x += p[0]
                              obstacle_y += p[1]
                              counter += 1
        print " obstacle : ( %.3f , %.3f ) " %(pos_x , pos_y)                                     
        obstacle = ' ( %.3f , %.3f ) ' %(pos_x , pos_y)
        obstacleslist.append(obstacle)
        publish_final_pos(obstacleslist)                   

