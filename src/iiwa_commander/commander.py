#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PoseStamped, Quaternion

class Commander:
    def __init__(self):
        self.__pub = rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size=10)
        self.__sub = rospy.Subscriber('/iiwa/state/CartesianPose', PoseStamped, self.callback)
        self.__requestPose=PoseStamped()
        self.__isReached=False

    def run(self, x, y, z):
        pose = PoseStamped()
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "iiwa_link_0"
        pose.pose.position.x=x
        pose.pose.position.y=y
        pose.pose.position.z=z
        pose.pose.orientation = Quaternion(0.229249566624, 0.97314697504, -0.017013060286, -0.0118389440926)
        self.__requestPose = pose
        self.__pub.publish(pose)
        while (not self.__isReached) and (not rospy.is_shutdown()):
            pass

    def callback(self, msg):
        self.__isReached = self.distanceToGoal(msg.pose,self.__requestPose.pose) < 0.02
        pass

    def distanceToGoal(self, start, goal):
        distance = (start.position.x-goal.position.x)**2 + \
        (start.position.y-goal.position.y)**2 + \
        (start.position.z-goal.position.z)**2
        print distance
        return distance
