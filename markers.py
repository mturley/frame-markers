#!/usr/bin/env python
import math
import sys

if(len(sys.argv) != 4):
  print "usage: "+sys.argv[0]+" <framerate> <marker duration in frames> <minutes>"
  sys.exit(1)

framerate = float(sys.argv[1])
markerduration = float(sys.argv[2])
minutes = float(sys.argv[3])

print "Generating "+sys.argv[1]+" markers at "+str(markerduration)+" frames each"
print "Assuming a framerate of "+str(framerate)
print "Stopping at "+str(minutes)+" minutes"

def lz(num):
  s = str(int(num))
  if(len(s) == 1):
    return "0"+s
  return s

def framesToTimecode(fr):
  seconds = math.floor(fr / framerate)
  frames = fr - (seconds * framerate)
  minutes = math.floor(seconds / 60)
  seconds = seconds - (minutes * 60)
  hours = math.floor(minutes / 60)
  minutes = minutes - (hours * 60)
  return lz(hours)+":"+lz(minutes)+":"+lz(seconds)+";"+lz(frames)

def markers(howmany):
  for n in range(int(howmany)):
    print "Marker "+str(n)+": "+framesToTimecode(markerduration*n)

def minutesToMarkers(minutes):
  markers(60*minutes*framerate/markerduration)

minutesToMarkers(minutes)
