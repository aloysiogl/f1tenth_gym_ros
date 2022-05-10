#!/usr/bin/env python
import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import LaserScan
import numpy as np

class Agent(object):
    def __init__(self):
        self.drive_pub = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=1)

        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback, queue_size=1)
        self.past_error = 0
    def scan_callback(self, scan_msg):
        drive = AckermannDriveStamped()
        len_scans = len(scan_msg.ranges)
        ranges = np.array([x if x < 100 else 0 for x in scan_msg.ranges])
        ranges = np.array(scan_msg.ranges)
        sum_1 = np.sum(ranges[:len_scans/2]-ranges[len_scans/2:])
        control = sum_1*0.001
        angle = max(min(control, np.pi/2), -np.pi/2)
        self.past_error = sum_1
        drive.drive.speed = 1
        drive.drive.steering_angle = -angle
        self.drive_pub.publish(drive)

if __name__ == '__main__':
    rospy.init_node('dummy_agent')
    dummy_agent = Agent()
    rospy.spin()