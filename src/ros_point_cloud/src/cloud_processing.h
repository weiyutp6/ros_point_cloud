#include "ros/ros.h"
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

class PointConv{
    private:
        sensor_msgs::PointCloud2 output; 
    public:
        PointConv();
        ~PointConv()
        void cloudProcessingCallback(const sensor_msgs::PointCloud2ConstPtr&);
        void publisherNode();
        void subscriberNode();
        ros::NodeHandle m_nh;
        ros::Subscriber m_sub;
        ros::Publisher m_pub;
        void pubAdvert();
};
