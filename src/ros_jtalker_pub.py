#!/usr/bin/env python
#coding: utf-8
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('txt', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)   

    data = "しゃべるのらくやから"
    print (type(data))
    pub.publish(data)
    rospy.spin()
if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException: pass
