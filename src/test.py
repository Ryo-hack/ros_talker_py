#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import rospy
from std_msgs.msg import String

class open_jtalker:
    def __init__(self):
        self.topic_name = "txt"
        self.node_name = "open_jtalker"
        rospy.init_node(self.node_name)
        self.image_sub = rospy.Subscriber(self.topic_name, String, self.String_callback)

    def jtalk(self,t):
        echo = ['echo "']
        txet = [t]
        open_jtalk=['" | open_jtalk']
        mech=[' -x',' /var/lib/mecab/dic/open-jtalk/naist-jdic']
        htsvoice=[' -m',' /usr/share/hts-voice/mei/mei_normal.htsvoice']
        speed=[' -r',' 1.0']
        outwav=[' -ow',' open_jtalk.wav']
        cmd=echo+txet+open_jtalk+mech+htsvoice+speed+outwav
        os.system("".join(cmd))
        aplay = ['aplay ','-q ','open_jtalk.wav']
        os.system("".join(aplay))

    def String_callback(self,txt):
        text = txt.data
        print(text)
        self.jtalk(text)      

if __name__ == '__main__':
    open_jtalker()
    rospy.spin()  
