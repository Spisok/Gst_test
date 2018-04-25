#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time


class TestThread(threading.Thread):
    def __init__(self,name,pause = 1):
        threading.Thread.__init__(self)
        self.daemon = True
        self.running = False
        self.count = 0
        self.name = name
        self.pause = pause
        
    def run(self):
        self.running = True
        print(" Therad %s  Started" % self.name)
        while self.running:
            print(" Thread %s. Count = %d "%(self.name,self.count))
            self.count += 1 
            time.sleep(self.pause)
        print(" Thread %s Stopped" % self.name)

    def stop(self):
        self.running = False 
        self.join()#dizhdattsa zaversheniya potoka 
        
T1 = TestThread("TOdin",1)
T1.start()
T2 = TestThread("TDva",0.5)
T2.start()


count =  0
try:
    while count < 10:
        print("Main count: %d" % count)
        count += 1
        time.sleep(2)
except KeyboardInterrupt:
    print("Ctrl+C pressed")
T1.stop()
T2.stop()
    
