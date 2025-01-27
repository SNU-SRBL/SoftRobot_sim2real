#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import math


class StiffController(Sofa.Core.Controller):


    def initGraph(self, node):
        self.node = node
        self.cableNord  = node.getChild('feuille').getChild('controlledPoints').getObject("nord")
        self.cableSud   = node.getChild('feuille').getChild('controlledPoints').getObject("sud")
        self.cableEst   = node.getChild('feuille').getChild('controlledPoints').getObject("est")
        self.cableOuest = node.getChild('feuille').getChild('controlledPoints').getObject("ouest")

            
    def onEndAnimationStep(self,dt):

        displacementNord  = self.cableNord.findData("displacement").value
        displacementSud   = self.cableSud.findData("displacement").value
        displacementEst   = self.cableEst.findData("displacement").value
        displacementOuest = self.cableOuest.findData("displacement").value
        outputVector = [0, displacementNord, displacementOuest, displacementSud, displacementEst]

        angle = [0]*4
        diametre = 35.5
        for i in range(0,4):
            angle[i]=(outputVector[i+1]+15)*360.0/(diametre*3.14);
            if (angle[i]<0.0):
                angle[i]=0.0;

            if (angle[i]>165):
                angle[i]=165;

        outputVector[1] = 165 - math.floor(1.0*angle[0]); # nord
        outputVector[2] = 165 - math.floor(1.0*angle[1]); # ouest
        outputVector[3] = math.floor(1.0*angle[2]);       # sud
        outputVector[4] = math.floor(1.0*angle[3]);       # est

        self.node.getObject('serial').findData('sentData').value = outputVector




