#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_from_nodeC(data):
    rospy.loginfo(f"Node D received from Node C: {data.data}")
    modified_message = data.data + "+D"
    rospy.loginfo(f"Node D sending to Node A: {modified_message}")
    pub_to_A.publish(modified_message)

def node_D():
    rospy.init_node('node_D', anonymous=True)

    global pub_to_A
    pub_to_A = rospy.Publisher('topic_D_to_A', String, queue_size=10)
    
    rospy.Subscriber('topic_C_to_D', String, callback_from_nodeC)

    rospy.spin()

if __name__ == '__main__':
    try:
        node_D()
    except rospy.ROSInterruptException:
        pass
