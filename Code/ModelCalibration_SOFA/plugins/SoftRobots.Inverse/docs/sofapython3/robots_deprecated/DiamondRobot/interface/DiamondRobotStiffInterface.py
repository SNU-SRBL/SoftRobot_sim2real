#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import math


class DiamondController(Sofa.Core.Controller):


    def initGraph(self, node):
        self.node = node

        self.cableNord  = node.getChild('feuille').getChild('controlledPoints').getObject("nord")
        self.cableSud   = node.getChild('feuille').getChild('controlledPoints').getObject("sud")
        self.cableEst   = node.getChild('feuille').getChild('controlledPoints').getObject("est")
        self.cableOuest = node.getChild('feuille').getChild('controlledPoints').getObject("ouest")
        self.cableHaut  = node.getChild('feuille').getChild('controlledPoints').getObject("haut")

        self.constantForce  = node.getChild('feuille').getObject("cff")


    def onEndAnimationStep(self,dt):

        displacementNord  = self.cableNord.findData("displacement").value
        displacementSud   = self.cableSud.findData("displacement").value
        displacementEst   = self.cableEst.findData("displacement").value
        displacementOuest = self.cableOuest.findData("displacement").value
        displacementHaut  = self.cableHaut.findData("displacement").value
        outputVector = [displacementHaut, displacementNord, displacementOuest, displacementSud, displacementEst]

        angle = [0]*5
        diametre = 35.5
        for i in range(0,5):
            angle[i]=(outputVector[i]+15)*360.0/(diametre*3.14);
            if (angle[i]<0.0):
                angle[i]=0.0;

            if (angle[i]>165):
                angle[i]=165;

        outputVector[0] = math.floor(1.0*angle[0]);       # haut
        outputVector[1] = 165 - math.floor(1.0*angle[1]); # nord
        outputVector[2] = 165 - math.floor(1.0*angle[2]); # ouest
        outputVector[3] = math.floor(1.0*angle[3]);       # sud
        outputVector[4] = math.floor(1.0*angle[4]);       # est

        self.node.getObject('serial').findData('sentData').value = outputVector
        print(outputVector)


    def onKeyPressed(self,c):

        dataForce = self.constantForce.findData('forces')

        if (c == "+"):
           force1 = dataForce.value[0][2] - 10.
           force2 = dataForce.value[1][2] - 10.
           if(force1 < -1800):
               force1 = -1800
           if(force2 < -1800):
               force2 = -1800
           dataForce.value = "0 0 "+str(force1)+" 0 0 "+str(force2)

        elif (c == "-"):
           force1 = dataForce.value[0][2] + 10.
           force2 = dataForce.value[1][2] + 10.
           if(force1 > 0):
               force1 = 0
           if(force2 > 0):
               force2 = 0
           dataForce.value = "0 0 "+str(force1)+" 0 0 "+str(force2)
