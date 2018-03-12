HOST=192.168.8.167
gst-launch-1.0 v4l2src device='/dev/video0' ! image/jpeg,width=640,height=480,framerate=30/1 ! rtpjpegpay ! udpsink host=$HOST port=9000
