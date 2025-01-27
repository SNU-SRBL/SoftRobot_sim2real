import Sofa
import random
from math import*


# utility methods

def diff(a,b):
	v_out=[0]*3;
	for i in range(3):
		v_out[i]= a[i] - b[i]
	return v_out
	

def plus(a,b):
	v_out=[0]*3;
	for i in range(3):
		v_out[i]= a[i] + b[i]
	return v_out
	

def mult_scalar(v,scalar):
	v_out=[0]*3;
	for i in range(3):
		v_out[i]= v[i] * scalar
	return v_out
	
	
def dot(a,b):
	out=0;
	for i in range(3):
		out = out+ a[i] * b[i]
	return out
	
	
def cross(a,b):
	c=[0]*3;
	c[0]=a[1]*b[2]-a[2]*b[1]
	c[1]=a[2]*b[0]-a[0]*b[2]
	c[2]=a[0]*b[1]-a[1]*b[0]
	return c
	
	
def normSquare(v):
	normS=0;
	for i in range(3):
		normS = normS+ v[i]*v[i]
	return normS
	
def norm(v):
	normS=normSquare(v);
	norm = sqrt(normS);
	return norm

def normalize(v):
	v_out=[0]*3;
	normS=normSquare(v);
	norm = sqrt(normS)
	for i in range(3):
		v_out[i] = v[i]/norm
		
	return v_out
	
	
def transformDoubleTable(DoubleTable):
	numRow= len(DoubleTable);
	SimpleTable=[0]*3*numRow
	
	for p in range(numRow):
		SimpleTable[3*p  ] = DoubleTable[p][0]
		SimpleTable[3*p+1] = DoubleTable[p][1]
		SimpleTable[3*p+2] = DoubleTable[p][2]
	return  SimpleTable
	
		
				
def transformTablePosInString(Table):
	numPos = len(Table)/3;
	strPos= ' ';
	for p in range(numPos):
		strPos = strPos+ str(Table[3*p])+' '+str(Table[3*p+1])+' '+str(Table[3*p+2])+' '
		
	return strPos
	
		
		
############################################################################################
# this is a PythonScriptController script
############################################################################################



print 'HERE WE AREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'

class goalController(Sofa.PythonScriptController):
	# called once the script is loaded
	def onLoaded(self,node):
		print 'Controller script loaded from node %s'%node.findData('name').value
		return 0


	
	# called once graph is created, to init some stuff...
	def initGraph(self,node):
		
		global goalState;
		goalState = node.getObject('goalMO1')
		
		global angle;
		angle=0
		# radius of the circle
		global radius;
		radius= 60;
		# time for doing a hole circle (in sec)
		global time_circle;
		time_circle= 20;
		
		#init pos
		global goalPos 
		goalPos = goalState.findData('position').value
		goalState.findData('position').value = str(goalPos[0][0])+' '+  str(goalPos[0][1])+' ' +str(goalPos[0][2]) + ' 0 0 0 1 ';
		
		print 'POS = '
		print goalPos

		return 0



	# called on each animation step
	total_time = 0
	def onBeginAnimationStep(self,dt):
		
		global goalPos 
		global goalState;
		global radius;
		global time_circle;
		global angle;
		Pi = 3.14159265359
		print 'dt=' + str(dt)
		
		
		angle = angle+ dt*2*Pi/time_circle;
		
		#goalPos = goalState.findData('position').value
		
		goalPos[0][1]=radius*cos(angle);
		goalPos[0][2]=radius*sin(angle);
		#print goalPos
		goalState.findData('position').value = str(goalPos[0][0])+' '+  str(goalPos[0][1])+' ' +str(goalPos[0][2]) + ' 0 0 0 1';
		
		
		return 0

		
	def draw(self):
	
		return 0
	
