#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from duckietown_msgs.msg import FSMState

class Talker:
 def __init__(self):
  rospy.Subscriber("/ms09dom/fsm_node/mode",FSMState,self.turtle)
  
  
  
  self.pub = rospy.Publisher('/ms09dom/car_cmd_switch_node',car_cmd, queue_size=10)
 
  
  self.count = 0
  
 def turtle(self, State):
  if State.state = "LANE_FOLLOWING" 
   self.count +=1
 
   if self.count >0 and self.count <2:
    forward = Twist()
    forward.linear.x = 1
    self.pub.publish(forward)
    rospy.logwarn("Foward1")
   
   if self.count >2 and self.count <4:
    turn = Twist()
    turn.angular.z = 1.5
    self.pub.publish(turn)
    rospy.logwarn("Turn1")
   
   if self.count >4 and self.count <6:
    forward = Twist()
    forward.linear.x = 1
    self.pub.publish(forward)
    rospy.logwarn("Forward2")
   
   if self.count >6 and self.count <8:
    turn = Twist()
    turn.angular.z = 1.5
    self.pub.publish(turn)
    rospy.logwarn("Turn2")
   
   if self.count >8 and self.count <10:
    forward = Twist()
    forward.linear.x = 2
    self.pub.publish(forward)
    rospy.logwarn("Forward3")
   
   if self.count >10 and self.count <12:
    turn = Twist()
    turn.angular.z = 1.5
    self.pub.publish(turn)
    rospy.logwarn("Turn3")
   
  if self.count >12 and self.count <14:
   forward = Twist()
   forward.linear.x = 1
   self.pub.publish(forward)
   rospy.logwarn("Forward4")
   
   if self.count >14 and self.count <16:
    turn = Twist()
    turn.angular.z = 1.5
    self.pub.publish(turn)
    rospy.logwarn("Turn4")
   
   if self.count >16 and self.count <18:
    forward = Twist()
    forward.linear.x = 1
    self.pub.publish(forward)
    rospy.logwarn("ForwardFINISH")
   
  

if __name__ == '__main__':
 try:
  rospy.init_node('talker', anonymous=True)
  t = Talker()
  rate = rospy.Rate(1)
  while not rospy.is_shutdown():
   t.turtle()
   rospy.logwarn("Test")
   rate.sleep()
 except rospy.ROSInterruptException:
  pass
