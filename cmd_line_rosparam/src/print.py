#!/usr/bin/env python2.7

import rospy

class GetArgs(object):
    def __init__(self):
        rospy.init_node("getting_param")

        try:
            # When we do: $ rosparam list 
            # The result is: /print_passed_parameter/file_name
            # So that's what we have to pass to get_param method
            extractedParam = rospy.get_param('/print_passed_parameter/file_name')
            print("Argument passed to Python script: "), extractedParam
        except(NameError):
            print("Didn't receive the parameter.") 


def run():
    ga = GetArgs()
    rospy.spin()


if __name__ == "__main__":
    run()