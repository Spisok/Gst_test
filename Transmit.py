#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gst","1.0")
from gi.repository import Gst
import time
DEVICE = "/dev/video0"
WIDTH = 640
HEIGHT = 480
FRAMERATE = 30
HOST = "192.168.8.167"
PORT = 9000


Gst.init(None)

#sozdanie Gstreamer pipeline
pipeline = Gst.Pipeline()

src = Gst.ElementFactory.make ("v4l2src")
src.set_property("device", DEVICE)

srcFilter = Gst.ElementFactory.make ("capsfilter")
srcCaps = Gst.caps_from_string("image/jpeg,width=%d ,height=%d ,framerate=%d/1" % (WIDTH, HEIGHT, FRAMERATE))

pay = Gst.ElementFactory.make ("rtpjpegpay")

sink = Gst.ElementFactory.make ("udpsink")
sink.set_property("host", HOST)
sink.set_property("port", PORT)

#Dobavlyaem elements v zepochku
pipeline.add(src)
pipeline.add(srcFilter)
pipeline.add(pay)
pipeline.add(sink)

#Soedinyaem elements
src.link(srcFilter)
srcFilter.link(pay)
pay.link(sink)

pipeline.set_state(Gst.State.PLAYING)
print("Playing")
time.sleep(10)
pipeline.set_state(Gst.State.NULL)
print("Null")
