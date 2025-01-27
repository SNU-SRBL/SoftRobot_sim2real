#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import math


class controller(Sofa.PythonScriptController):


    def initGraph(self, node):
	displacement=[ 0., 0., 0., 0., 0., 0., 0., 0., 0.]
        self.node  = node


        outputVector = [245, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
        self.node.getObject('serial').findData('sentData').value = outputVector


    def resetGraph(self, node):
        outputVector = [245, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
        self.node.getObject('serial').findData('sentData').value = outputVector

            
    def onEndAnimationStep(self,dt):

	displacement=[ 0., 0., 0., 0., 0., 0., 0., 0., 0.]
	pressure=[ 0., 0., 0., 0., 0., 0., 0., 0., 0.]
        outputVector = [245, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       
        for cableId in range(1,10):
	  cable = self.node.getChild('complianceSection').getChild('cables').getObject('c'+str(cableId))
	  displacement[cableId-1] = cable.findData('cableLength').value
	  outputVector[cableId] = int(displacement[cableId-1])
	  
        for sectionId in range(1,4):
	  for cavityId in range(1,4):
	    cavity = self.node.getChild('complianceSection').getChild('MappedCavity'+str(sectionId)+str(cavityId)).getObject('SurfacePressureActuator')
	    pressure[(sectionId-1)*3+(cavityId-1)] = cavity.findData('pressure').value
	    outputVector[10+(sectionId-1)*3+(cavityId-1)] = int(pressure[(sectionId-1)*3+(cavityId-1)])

        self.node.getObject('serial').findData('sentData').value = outputVector
        print(outputVector)


    #def onBeginAnimationStep(self,dt):

        #############################################################
        ####Translate a bit the goal for a more friendly interaction
        #############################################################
        #meca1 = self.node.getChild('goal').getChild('goalPoints').getObject('goalMORigide')
        #meca2 = self.node.getChild('goal').getChild('goalPoints').getObject('goalMORigideTranslated')

        #position = meca1.findData('position').value[0] 
        #meca2.findData('position').value = str(position[0])+" "+str(position[1])+" "+str(position[2]-10.)
        




