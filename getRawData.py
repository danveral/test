#!/usr/bin/env python
#tst
#123
import socket
import time, sys
import dpkt
from multiprocessing import Process
import random

laserColor = []
for mm in xrange(16):
	color = []
	color.append(int(random.random()*256))
	color.append(int(random.random()*256))
	color.append(int(random.random()*256))
	laserColor.append(color)

def int2ip(addr):
	return socket.inet_ntoa(addr)

def setList2TwoDimension(retList):	
	foo_tmpList=[]
	for k in xrange(6):
		tmpList = []
		for i in xrange(100):
			tmpList.append(retList[i+(100*k)])
		foo_tmpList.append(tmpList)
	foo_tmpList.append(retList[600:606])
	return foo_tmpList

def sniffUDP2368fromSensor():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind(('', 2368))
	s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	while True:	
		data,addr=s.recvfrom(1206)
		tmpList = data
		tmpList_shrink = tmpList[:100]+tmpList[200:300]+tmpList[400:500]+tmpList[600:700]\
		+tmpList[800:900]+tmpList[1000:1100]+tmpList[1200:1206]
		tmpList_shrink_2D = setList2TwoDimension(tmpList_shrink)
		for j in xrange(6):
			for k in xrange(32):
				if k <= 15:
					tmpList_shrink_2D[j].insert((7+6*k),laserColor[k][0])
					tmpList_shrink_2D[j].insert((7+6*k),laserColor[k][1])
					tmpList_shrink_2D[j].insert((7+6*k),laserColor[k][2])
				else:
					tmpList_shrink_2D[j].insert((7+6*k),laserColor[k-16][0])
					tmpList_shrink_2D[j].insert((7+6*k),laserColor[k-16][1])
					tmpList_shrink_2D[j].insert((7+6*k),laserColor[k-16][2])
		foo = []
		for aa in xrange(6):
			for bb in xrange(len(tmpList_shrink_2D[aa])):
				foo.append(tmpList_shrink_2D[aa][bb])
		for cc in xrange(6):
			foo.append(tmpList_shrink_2D[6][cc])
		s2.sendto('a', ('172.16.69.1', 9000))
		print foo[0]



def main():
	sniffUDP2368fromSensor()
	

if __name__ == "__main__":
	main()












