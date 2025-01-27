#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sofa

class controller(Sofa.PythonScriptController):

    def initGraph(self, node):
            self.node = node
            self.interv1Node=self.node.getChild('Intervertebra1')
            self.indep_particulesNode = self.node.getChild('Independant_Particules')
            self.DeformableGridNode = self.indep_particulesNode.getChild('DeformableGrid')
    
    
    

    def onKeyPressed(self,c):
        
            print '++++++++++++++++++'
            print c
            print '++++++++++++++++++'
        
            if (c == "a" or c == "A" or c == "+"):
                Cavity11Node=self.DeformableGridNode.getChild('Cavity11')
                pressure1 = Cavity11Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] + 1000.
                if (pressure1<10000):
                    Cavity11Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure1)
            
            if (c == "b" or c=="B" or c == "+"):
                Cavity12Node=self.DeformableGridNode.getChild('Cavity12')
                pressure2 = Cavity12Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] + 1000.
                if (pressure2<10000):
                    Cavity12Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure2)
            
            if (c == "c" or c =="C" or c == "+"):
                Cavity13Node=self.DeformableGridNode.getChild('Cavity13')
                pressure3 = Cavity13Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] + 1000.
                if (pressure3<10000):
                    Cavity13Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure3)


            cablesNode =self.interv1Node.getChild('cables')


            print cablesNode.findData('name').value
            print '++++++++++++++++++'
            if (c=="1"):
                disp =cablesNode.getObject('c1').findData('inputValue').value[0][0]+0.5
                cablesNode.getObject('c1').findData('inputValue').value = str(disp)
            if (c=="O"):
                disp =cablesNode.getObject('c2').findData('inputValue').value[0][0]+0.5
                cablesNode.getObject('c2').findData('inputValue').value = str(disp)
            if (c=="J"):
                disp =cablesNode.getObject('c3').findData('inputValue').value[0][0]+0.5
                cablesNode.getObject('c3').findData('inputValue').value = str(disp)
            if (c=="2"):
                disp =cablesNode.getObject('c1').findData('inputValue').value[0][0]-0.5
                cablesNode.getObject('c1').findData('inputValue').value = str(disp)
            if (c=="P"):
                disp =cablesNode.getObject('c2').findData('inputValue').value[0][0]-0.5
                cablesNode.getObject('c2').findData('inputValue').value = str(disp)
            if (c=="K"):
                disp =cablesNode.getObject('c3').findData('inputValue').value[0][0]-0.5
                cablesNode.getObject('c3').findData('inputValue').value = str(disp)

        

            if (c == "-"):
                Cavity11Node=self.DeformableGridNode.getChild('Cavity11')
                pressure1 = Cavity11Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] - 1000.
                Cavity11Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure1)
                Cavity12Node=self.DeformableGridNode.getChild('Cavity12')
                pressure2 = Cavity12Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] - 1000.
                Cavity12Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure2)
                Cavity13Node=self.DeformableGridNode.getChild('Cavity13')
                pressure3 = Cavity13Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value[0][0] - 1000.
                Cavity13Node.getObject('SurfacePressureConstraint').findData('constantPressureValue').value = str(pressure3)

