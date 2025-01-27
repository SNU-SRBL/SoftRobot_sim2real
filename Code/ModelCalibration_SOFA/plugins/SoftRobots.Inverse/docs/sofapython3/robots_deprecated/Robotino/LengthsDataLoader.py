#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sofa
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__))+'/'



fileName = path + "results"+ (str(datetime.now()))[11:-7]
fo = open(fileName, 'w+')
fo.close()

class controller(Sofa.PythonScriptController):
  


    def initGraph(self, node):
      self.currentNode = node
      self.rootNode = node.getRoot()
      self.frameNode = self.rootNode.getChild("frames")
      self.currentline = -1
      
      with open(path + 'lengths_inputs_cbha', 'r') as fi:
	self.res= []
	for line in fi.readlines():
	    self.res.append(line.split())
    
	fi.close()

	
#additional stuff ...

    def onKeyPressed(self,c):
      if (c == "+"):#Press + to update the vector of desired lengths

	self.currentline = self.currentline + 1
	if (self.currentline + 1) > len(self.res):
	  print "no more entries"
	  return
	
	length1 = self.currentNode.getObject('s1').findData('desiredLength')
	length2 = self.currentNode.getObject('s5').findData('desiredLength')
	length3 = self.currentNode.getObject('s3').findData('desiredLength')
	length4 = self.currentNode.getObject('s2').findData('desiredLength')
	length5 = self.currentNode.getObject('s6').findData('desiredLength')
	length6 = self.currentNode.getObject('s4').findData('desiredLength')
	
	length1.value = str(self.res[self.currentline][0])
	length2.value = str(self.res[self.currentline][1])
	length3.value = str(self.res[self.currentline][2])
	length4.value = str(self.res[self.currentline][3])
	length5.value = str(self.res[self.currentline][4])
	length6.value = str(self.res[self.currentline][5])
	
	
	print 'Lengths updated for line {}'.format(self.currentline) 




      if (c == "-"):#Save the end-effector cartesian position
	global fileName
	print fileName
	fo = open(fileName,'a')
	effector = self.frameNode.getObject('DOFs').findData('position')
	x = effector.value[20][0]
	y = effector.value[20][1]
	z = effector.value[20][2]
	print z
	print -y
	print x
	
	
	fo.write(str(z))
	fo.write('\t')
	fo.write(str(-y))
	fo.write('\t')
	fo.write(str(x))
	fo.write('\n')
	
	fo.close()
	
	print "End-effector position {}".format(self.currentline)
	
	return 0
	
