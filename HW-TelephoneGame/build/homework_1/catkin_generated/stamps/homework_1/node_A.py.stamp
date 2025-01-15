#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_from_nodeD(data):
    rospy.loginfo(f"Node A received from Node D: {data.data}")

def node_A():
    rospy.init_node('node_A', anonymous=True)

    pub_to_B = rospy.Publisher('topic_A_to_B', String, queue_size=10)

    rospy.Subscriber('topic_D_to_A', String, callback_from_nodeD)
    
    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        msg = "Message accessed by: A"
        rospy.loginfo(f"Node A sending to Node B: {msg}")
        pub_to_B.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_A()
    except rospy.ROSInterruptException:
        pass