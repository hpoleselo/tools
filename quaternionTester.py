#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped, Quaternion, Pose, Point
from std_msgs.msg import Header
from tf.transformations import quaternion_from_euler, euler_from_quaternion


""" Program to test MANUAL orientation changes on poses before trying out on the real robot.     
    You can change the initial pose as wished by modifying the lists "qtn" and "pos". """

def posePublisher():
    print " "
    rospy.init_node("MarkerPose")
    rate = rospy.Rate(1)
    pub = rospy.Publisher("MarkerPose", PoseStamped, queue_size=1)
    pub_rot = rospy.Publisher("MarkerPoseRotated", PoseStamped, queue_size=1)

    # Header will be the same for both topics.
    hdr = Header()
    hdr.frame_id = "world"
    hdr.stamp = rospy.Time.now()

    # Setting up message for the MarkerPose topic Position in XYZ (meters)
    pos = [-0.825060489015, 0.108498253242, 1.01545051907]
    position = Point(pos[0], pos[1], pos[2])
    qtn = [-0.0714631114048, -0.0313084463919, -0.435357988258, 0.896870239752]
    quaternion = Quaternion(qtn[0], qtn[1], qtn[2], qtn[3])
    init_pos = Pose()
    init_pos.position = position
    init_pos.orientation = quaternion
    ps = PoseStamped(hdr, init_pos)

    # Conversion and calculation
    _quaternion = list(qtn)
    rpy = euler_from_quaternion(_quaternion)
    print "Original RPY: \n", rpy
    print " "
    _rpy = list(rpy)
    while True:
        try:
            rotation = float(raw_input("How much you want to add to the rotation? (in Radians): "))
            if (rotation <= 3.14) and (rotation >= -3.14):
                axis = raw_input("With respect to which axis? (x y or z): ")
                if axis == "x":
                    _rpy[0]= _rpy[0] + rotation
                    break
                if axis == "y":
                    _rpy[1]= _rpy[1] + rotation
                    break
                if axis == "z":
                    _rpy[2]= _rpy[2] + rotation
                    break

            else:
                print "Rotation not valid."
        except ValueError:
            print "Input not correct."
    print "Updated RPY: \n", _rpy
    print " "
    print "Converting now to quaternion..."

    # Setting up message for the MarkerPoseRotated topic
    new_quaternion = quaternion_from_euler(_rpy[0], _rpy[1], _rpy[2])
    new_quaternion_tuple = Quaternion(new_quaternion[0], new_quaternion[1], new_quaternion[2], new_quaternion[3])
    print new_quaternion_tuple
    rotated_pos = Pose()
    rotated_pos.position = position
    rotated_pos.orientation = new_quaternion_tuple
    rotated_pstamp = PoseStamped(hdr, rotated_pos)
    print "Publishing both poses (original and rotated)! Check RVIZ and listen to both topics in the Display Pose option."

    while not rospy.is_shutdown():
        pub.publish(ps)
        pub_rot.publish(rotated_pstamp)
        rate.sleep()


if __name__ == '__main__':
    try:
        posePublisher()
    except rospy.ROSInterruptException:
print 'Program could not be correctly ran.'
