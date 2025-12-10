import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import PointCloud

import matplotlib.pyplot as plt

class LidarSubscriber(Node):

    xdata = []
    ydata = []

    def __init__(self):
        super().__init__('lidar_subscriber')
        print("hello from init")
        self.subscription = self.create_subscription(PointCloud,'pointcloud2d',self.listener_callback,0)
        self.subscription


    def listener_callback(self, msg):
        print("hello from listener")
        for p in msg.points:
            self.xdata.append(p.x)
            self.ydata.append(p.y)
        plt.scatter(self.ydata,self.xdata)
        plt.show()


def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    print("test number 2")
    rclpy.spin(lidar_subscriber)
    print('Hi')

if __name__ == '__main__':
    main()
