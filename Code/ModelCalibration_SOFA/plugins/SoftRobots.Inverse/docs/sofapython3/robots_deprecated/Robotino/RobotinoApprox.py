import Sofa
import random
import math

# utility methods

def createMesh(parentNode,name,x,y,z,color):

#	node = parentNode.addChild(name)
#	node.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False)
#	node.addObject('CGLinearSolver',name='linear solver',iterations='25',tolerance='1.0e-9',threshold='1.0e-9')
#	object = node.addObject('MechanicalObject',name='mObject',dx=x,dy=y,dz=z)
#	mass = node.addObject('UniformMass',name='mass',totalMass='10')
	node.addObject('SparseGridTopology', n='4 4 4', fileTopology='test.obj')
#	node.addObject('HexahedronFEMForceField', youngModulus='100')
	
#	VisuNode = node.addChild('Visu')
#	VisuNode.addObject('OglModel',name='Visual',filename='mesh/Armadillo_simplified.obj', color=color)

	# one can't use this function from here, as it is meant to be used at runtime, not in the graph creation phase
	#object.applyTranslation(x,y,z)

	return node
	
def assignPosition(angle,dx, n):

	cT = math.cos(angle/2)  
	sT = math.sin(angle/2) 
	m=1
	position='126 0 -91 0 ' + str(sT)+ ' 0 '+str(cT)
	
	
	while m!=n:
		x=126 + m*dx*math.cos(angle);
		z=-91 - m*dx*math.sin(angle);
		position2=str(x)+ ' 0 ' +str(z)+ ' 0 ' + str(sT)+ ' 0 ' + str(cT)
		position=position + ' ' + position2
		m=m+1
	
	
	return position 



	
	
	




# scene creation method
def createScene(rootNode):

	

	# scene global stuff
	rootNode.addObject('VisualStyle', displayFlags='showBehaviorModels hideCollisionModels hideMappings hideForceFields')
	
	# visualization
	visuNode = rootNode.addChild('Visu')
	
	visuNode.addObject('MeshObjLoader', name='loader', filename='DeformableRobot/Robotino/Robotino_Decim.obj')
	visuNode.addObject('OglModel', src='@loader')
	visuNode.addObject('ClipPlane', normal='0 -1 0', position='0 -5 0')
	
	# creation of rigid objects
	mecaNode = rootNode.addChild('Meca')
	mecaNode.addObject('EulerImplicitSolver')
	mecaNode.addObject('CGLinearSolver',iterations=25,tolerance=1.0e-9,threshold=1.0e-9)
	object = mecaNode.addObject('MechanicalObject',name='MecaObject',template="Rigid3")
	mecaNode.addObject('UniformMass',totalmas=100, showAxisSizeFactor=10)
	object.findData('position').value=assignPosition(3.14/4.5,12.2, 17)
	
	
	
	



	return rootNode
