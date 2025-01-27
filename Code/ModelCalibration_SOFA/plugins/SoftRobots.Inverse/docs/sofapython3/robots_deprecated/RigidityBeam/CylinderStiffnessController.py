#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sofa

class controller(Sofa.PythonScriptController):
    
    def initGraph(self, node):
        
        self.node = node
        
    def onKeyPressed(self,c):
            
        #print '++++++++++++++++++'
        #print c
        #print '++++++++++++++++++'
            
        if (c == "G"):
            stiffnessValue = 100000
            self.node.getObject('cyl1').findData('stiffness').value = str(stiffnessValue)
            self.node.getObject('cyl2').findData('stiffness').value = str(stiffnessValue)
                
                
                
                
                
                
                