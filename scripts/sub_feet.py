#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def cb(message):
    print('{0}feet = {1}m'.format(message.data,message.data/3.2808))

if __name__ == '__main__':
    rospy.init_node('sub_feet')
    sub = rospy.Subscriber('/feet', Int32, cb)
    rospy.spin()
