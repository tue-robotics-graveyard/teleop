#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop')
import rospy


#from std_msgs.msg import Int16
from std_msgs.msg import String  

import sys, select, termios, tty

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	#pub = rospy.Publisher('key_commands', Int16)
	pub = rospy.Publisher('key_commands', String)
	rospy.init_node('teleop')
	
	rospy.loginfo("Teleop node started")

	try:
		#print msg
		while(1):
			key = getKey()
			print key
			#if not(key.isdigit()):
				#print "This key is not an integer!"
			#lse:
			#pub.publish(int(key))
			if key == '\x03':
				break
			pub.publish(String(key))
			

	except:
		print 'e'

	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


