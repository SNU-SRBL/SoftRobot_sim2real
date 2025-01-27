#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sofa

class controller(Sofa.PythonScriptController):

    def initGraph(self, node):

            self.node = node

    def onKeyPressed(self,c):

            if (c == "+"):
                pressure = self.node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] + 1000.
                self.node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure)

            if (c == "-"):
                pressure = self.node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] - 1000.
                self.node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure)






