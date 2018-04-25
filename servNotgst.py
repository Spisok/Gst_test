#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time
import numpy as np

from xmlrpc.server import SimpleXMLRPCServer

IP_SERV = "192.168.8.170"
DEBUG_PORT = 8000

def debugFrame(frame):
    frameName = frame[0]
    imgArray = np.frombuffer(frame[1].data,dtype=np.uint8)
    img = cv2.imdecode(imgArray, cv2.IMREAD_COLOR)
    cv2.imshow(frameName, img)
    #print(frame)
    cv2.waitKey(10) 
    return 0 
    
serverDebug = SimpleXMLRPCServer ((IP_SERV,DEBUG_PORT))
serverDebug.logReqests = False
print("Control XMLRPC Server Listening on %s:%d" % (IP_SERV,DEBUG_PORT))

serverDebug.register_function(debugFrame)
try:
    serverDebug.serve_forever()
except KeyboardInterrupt:
    print("Ctrl+C pressed")
    serverDebug.server_close()
cv2.DestroyAllWindows

#serverDebug.serve_forever()
