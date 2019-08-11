#include "cloud_processing.h"

PointConv::PointConv(){
}

~PointConv::PointConv(){
}

void PointConv::cloudProcessingCallback(const sensor_msgs::PointCloud2ConstPtr& input){
    output = *input; 
    pubAdvert();
}

void PointConv::publisherNode(){
    pub.publish(output);
}

void PointConv::pubAdvert(){
    pub = m_nh.advertise<senser_msgs::PointCloud2> ("obstacle",1000);
    publisherNode();
}

void PointConv::subscriberNode(){
    sub = m_nh.subscribe ("lidar_wamv/points",1000,cloudProcessingCallback);
}

int main(int argc, int **argv){
    ros::init(argc,argv,"cloud_processing");
    PointConv PointConvClass;
    PointConvClass.subscriberNode();
    ros::spin();
}
