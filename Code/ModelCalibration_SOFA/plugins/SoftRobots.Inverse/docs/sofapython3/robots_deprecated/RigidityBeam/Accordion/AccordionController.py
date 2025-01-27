#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import zmq

class client:

    def __init__(self):
    
        self.port = "5556"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        print "Connecting to server..."
        self.socket.connect("tcp://localhost:%s" % self.port)


class controller(Sofa.PythonScriptController):
         

    def initGraph(self, node):

            self.node = node
            self.sendDisplacementsToSerial()           
            self.client = client()

            self.goalInitialPosition = self.node.getChild("goal").getObject("goalMO").findData('position').value
            self.posX = self.goalInitialPosition[0][0]
            self.posY = self.goalInitialPosition[0][1]

            # TEST
            # self.displacement = 0.


    def onBeginAnimationStep(self,dt):

        #### Send sensor displacement to cube simulation
        sensorDisplacement = self.node.getChild("sensor").getObject("usbdevice").LengthValues;
        self.client.socket.send(str(0.001*sensorDisplacement[0][0])) 

        # TEST
        # self.displacement -= 0.01
        # if (self.displacement < -0.2):
        #     self.displacement = -0.2
        # self.client.socket.send(str(self.displacement*0.01))


        #### Apply sensor displacement on effector goal
        posZ = self.goalInitialPosition[0][2]
        if (sensorDisplacement[0][0] < 0): #### Positive displacement not allowed
            posZ += 0.1*sensorDisplacement[0][0]
	
	# TEST        
	# posZ += self.displacement

        self.node.getChild("goal").getObject("goalMO").findData('position').value = str(self.posX) +" "+ str(self.posY) +" "+ str(posZ);

        #### Receive force from cube simulation
        force = self.client.socket.recv() 
        print("force "+str(force))
        self.node.getChild("accordion").getChild("constantForce").getObject("forceField").findData('forces').value = str("0.0" + "0.0" + str(force));

        

    def onEndAnimationStep(self,dt):
        
        self.sendDisplacementsToSerial()


    def sendDisplacementsToSerial(self):

        displacement1 = self.node.getChild('accordion').getChild('cables').getObject("cable1").findData('displacement').value 
        displacement2 = self.node.getChild('accordion').getChild('cables').getObject("cable2").findData('displacement').value 
        displacement3 = self.node.getChild('accordion').getChild('cables').getObject("cable3").findData('displacement').value 
        pressure      = self.node.getChild('accordion').getChild('cavity').getObject("pressure").findData('pressure').value 

        output = [displacement3,
        displacement2,
        displacement1,
        pressure*15]

        print(output)

        for i in range(0,3):
            output[i] = (output[i]+0.9)/0.014

        self.node.getObject('serial').findData('sentData').value = output





                



        
