#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_from_nodeB(data):
    rospy.loginfo(f"Node C received from Node B: {data.data}")
    modified_message = data.data + "+C"
    rospy.loginfo(f"Node C sending to Node D: {modified_message}")
    pub_to_D.publish(modified_message)

def node_C():
    rospy.init_node('node_C', anonymous=True)

    global pub_to_D
    pub_to_D = rospy.Publisher('topic_C_to_D', String, queue_size=10)

    rospy.Subscriber('topic_B_to_C', String, callback_from_nodeB)

    rospy.spin()

if __name__ == '__main__':
    try:
        node_C()
    except rospy.ROSInterruptException:
        pass
