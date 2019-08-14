#include "cloud_processing.h"

void PointConv::cloudProcessingCallback(const sensor_msgs::PointCloud2ConstPtr& input){
    output = *input; 
    pubAdvert();
}

void PointConv::publisherNode(){
    m_pub.publish(output);
}

void PointConv::pubAdvert(){
    m_pub = m_nh.advertise<sensor_msgs::PointCloud2> ("obstacle",1000);
    publisherNode();
}

void PointConv::subscriberNode(){
    m_sub = m_nh.subscribe ("lidar_wamv/points",1000,&PointConv::cloudProcessingCallback,this);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "cloud_processing");
    PointConv PointConvClass;
    ROS_INFO("%s","hello");
    PointConvClass.subscriberNode();
    ros::spin();
}
