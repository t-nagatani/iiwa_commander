#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy

class Commander:
    def __init__(self):
        self.__pub = rospy.Publisher('pub', iiwa送信の型)
        self.__sub = rospy.Subscriber('sub', iiwa受信の型)

    def run(self, x, y, z):
        self.__pub.publish(cmd)

    def callback(self, msg):
