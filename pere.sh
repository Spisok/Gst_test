gst-launch-1.0 -v \
udpsrc port=9000 caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)JPEG' ! \
rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink sync=false
