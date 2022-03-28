import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="",
	help="path to input video file")
parser.add_argument("-o", "--output", type=str, default="",
	help="path to output frames folder")
parser.add_argument("-s", "--seconds", type=float, default=0.5,
	help="time difference where frame is captured")

args = parser.parse_args()
vidcap = cv2.VideoCapture(args.input)
count = 0
success,image = vidcap.read()

while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000*args.seconds)) 
  cv2.imwrite(args.output+"/frame%d.jpg" % count, image)   
  success,image = vidcap.read()      
  count += 1
