#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sofa

import zmq


class server :

    def __init__(self):
    
        self.port = "5556"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
  
        self.socket.bind("tcp://*:%s" % self.port)
        print ("Server initialized")


class controllerStiffness(Sofa.PythonScriptController):
        
    def initGraph(self,node):
      
        self.serv = server()
        self.goalState = node.getObject('goalMO')
        self.spring = node.getObject('spring')
        
        return 0


    def onBeginAnimationStep(self,dt):

        # Receive force
        displacement = self.serv.socket.recv()
        initPos = self.goalState.findData('reset_position').value;
        newrestPos = float(displacement) + float(initPos[0][2])
        print("sensorDisplacement")
        print(displacement)
        self.goalState.findData('rest_position').value = str("0 0 " + str(newrestPos));

        return 0


    def onEndAnimationStep(self,dt):

        # Send displacement
        realPos = self.goalState.findData('rest_position').value;
        Pos = self.goalState.findData('position').value;
        stiffness = self.spring.findData('stiffness').value
        #print(stiffness[0][0])
        #print(Pos)
        print("restPos")
        print(round(realPos[0][2],5))
        print("effectivePos")
        print(round(Pos[0][2],5))
        force = stiffness[0][0]*(round(realPos[0][2],5)-round(Pos[0][2],5))
        force *= 10
        print("Force")
        print(force)
        self.serv.socket.send(str(force))

        return 0