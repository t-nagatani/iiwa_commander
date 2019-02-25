#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from iiwa_commander.commander import Commander

if __name__ == "__main__":
    rospy.init_node("iiwa_commander_tester")

    commander = Commander()


    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        commander.run(0.430263417065, 0.67638813524, -0.0312535715088)
        rate.sleep()
        commander.run(0.530263417065, 0.67638813524, -0.0312535715088)
        rate.sleep()

    rospy.spin()
