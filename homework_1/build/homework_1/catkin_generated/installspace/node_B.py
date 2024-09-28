#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_from_nodeA(data):
    rospy.loginfo(f"Node B received from Node A: {data.data}")
    modified_message = data.data + "+B"
    rospy.loginfo(f"Node B sending to Node C: {modified_message}")
    pub_to_C.publish(modified_message)

def node_B():
    rospy.init_node('node_B', anonymous=True)

    global pub_to_C
    pub_to_C = rospy.Publisher('topic_B_to_C', String, queue_size=10)
    
    rospy.Subscriber('topic_A_to_B', String, callback_from_nodeA)

    rospy.spin()

if __name__ == '__main__':
    try:
        node_B()
    except rospy.ROSInterruptException:
        pass
