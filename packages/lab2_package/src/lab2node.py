#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from duckietown_msgs.msg import FSMState
from duckietown_msgs.msg import Twist2DStamped

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from duckietown_msgs.msg import FSMState
from duckietown_msgs.msg import Twist2DStamped

class Talker:
 def __init__(self):
  rospy.Subscriber("/ms09dom/fsm_node/mode",FSMState,self.turtle)
    
  self.pub = rospy.Publisher('/ms09dom/car_cmd_switch_node/cmd',Twist2DStamped, queue_size=10)
 
  
  self.count = 0
  
 def turtle(self, State):
  while State.state == "LANE_FOLLOWING":
   
    forward = Twist2DStamped()
    forward.v = 0.25
    forward.omega = 0
    self.pub.publish(forward)
    rospy.logwarn("Foward" + str(self.count%5))
    rospy.sleep(3) #3.8
   
    turn = Twist2DStamped()
    turn.omega = 0.8 #0.8
    self.pub.publish(turn)
    rospy.logwarn("Turn" + str(self.count%5))
    rospy.sleep(0.5) #0.5
   
if __name__ == '__main__':
 try:
  rospy.init_node('talker', anonymous=True)
  t = Talker()
  rate = rospy.Rate(1)
  while not rospy.is_shutdown():
   rospy.logwarn("Test")
   rate.sleep()
 except rospy.ROSInterruptException:
  pass
