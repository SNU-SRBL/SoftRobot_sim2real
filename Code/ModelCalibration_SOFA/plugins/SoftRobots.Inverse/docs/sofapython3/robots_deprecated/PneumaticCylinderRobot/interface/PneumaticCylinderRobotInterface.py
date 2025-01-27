#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa


class interface(Sofa.PythonScriptController):


    def initGraph(self, node):
        self.node = node
        self.cavity1 = node.getChild("Cavity1").getObject("actuator")
        self.cavity2 = node.getChild("Cavity2").getObject("actuator")
        self.cavity3 = node.getChild("Cavity3").getObject("actuator")

            
    def onEndAnimationStep(self,dt):

        pressure1 = self.cavity1.findData("pressure").value
        pressure2 = self.cavity2.findData("pressure").value
        pressure3 = self.cavity3.findData("pressure").value

        outputVector = [pressure1, pressure2, pressure3]

        # print(outputVector)




