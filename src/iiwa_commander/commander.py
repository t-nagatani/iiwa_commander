#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PoseStamped, Quaternion
from std_msgs.msg import Int32

class Commander:
    def __init__(self):
        self.__pub = rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size=10)
        self.__sub = rospy.Subscriber('/iiwa/state/CartesianPose', PoseStamped, self.callback)
        self.__requestPose=PoseStamped()
        self.__isReached=False
        self.__sakePub = rospy.Publisher('sake_command', Int32, queue_size=10)
        self.__sakeSub = rospy.Subscriber('sake_state', Int32, self.sakeCallback)
        self.__sakeStatus = 0

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

    def close(self):
        msg = Int32()
        msg.data = 0
        self.__sakePub.publish(msg)
        while self.__sakeStatus == 1 and (not rospy.is_shutdown()):
            pass

    def open(self):
        msg = Int32()
        msg.data = 1
        self.__sakePub.publish(msg)
        while self.__sakeStatus == 0 and (not rospy.is_shutdown()):
            pass

    def callback(self, msg):
        self.__isReached = self.distanceToGoal(msg.pose,self.__requestPose.pose) < 0.02

    def distanceToGoal(self, start, goal):
        distance = (start.position.x-goal.position.x)**2 + \
        (start.position.y-goal.position.y)**2 + \
        (start.position.z-goal.position.z)**2
        return distance

    def sakeCallback(self, msg):
        self.__sakeStatus = msg.data
