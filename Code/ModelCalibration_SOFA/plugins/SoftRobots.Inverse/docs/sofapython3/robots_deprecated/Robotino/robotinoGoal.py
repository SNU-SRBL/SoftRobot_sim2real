from __future__ import division #for default floating point division
import Sofa
import random
import sys
from math import*


def listToData(l):
	return str(l).replace('[', '').replace(']', '').replace(',', '')


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


def div_scalar(v,scalar):
	v_out=[0]*3;
	for i in range(3):
		v_out[i]= v[i] / scalar
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
	return sqrt(normS)


def normalize(v):
	v_out=[0]*3;
	normS=normSquare(v);
	norm = sqrt(normS)
	for i in range(3):
		v_out[i] = v[i]/norm
		
	return v_out

def genStarPath(inR, outR, n, x):
	path = [None]*2*n
	
	for i in range(2*n):
		p = [x, 0 , 0]
		theta = (2*pi)/(2*n)*i + pi/2
		r = 0
		if i % 2 == 0 :
			r = outR
		else:
			r = inR
			
		p[1] = cos(theta)*r
		p[2] = sin(theta)*r
		
		path[i] = p
		
	return path
		

class SquareGoalController(Sofa.PythonScriptController) :
	
	def initGraph(self, node):
		self.goalState = node.getObject('goalMO1')
		self.pos = self.goalState.findData('position').value[0]
		initX = self.pos[0]
		sqSize = 20
		
		self.path = [ [initX, sqSize, sqSize], [initX, sqSize, -sqSize], [initX, -sqSize, -sqSize], [initX, -sqSize, sqSize] ]
		#self.path = genStarPath(20, 35, 5, initX)
		print(self.path)
		self.nPt = len(self.path)
		self.velocities = [ 1, 5, 3, 7 ]
		#self.velocities = [2]*self.nPt
		self.pos = self.path[0]
		
		print('Goal init pos ' + str(self.pos))
		
		self.t = 0
		self.segment = 0
		self.goalState.findData('position').value = listToData([self.pos])
		
		outfile = open('SquareTrajectory.csv', 'w')
		outfile.close()
		self.tStep = 0		
		
		
	def onBeginAnimationStep(self, dt):
		direction = diff(self.path[(self.segment+1)%self.nPt], self.path[self.segment%self.nPt])
		normalize(direction)
		direction = mult_scalar(direction, self.velocities[self.segment%self.nPt])
		
		move = mult_scalar(direction, dt)
		dToNextPt = diff(self.path[(self.segment+1)%self.nPt], self.pos)

		if norm(dToNextPt) < norm(move) :
			self.pos = self.path[(self.segment+1)%self.nPt]
			self.segment += 1
		else:
			self.pos = plus(self.pos, move)
			
		self.goalState.findData('position').value = [self.pos]
		outfile = open('SquareTrajectory.csv', 'a')
		outfile.write(";".join([str(self.tStep), str(self.pos[1]/1000), str(self.pos[2]/1000) ])+'\n')
		outfile.close()
		
		self.tStep += 1		
	
	
class CircleGoalController(Sofa.PythonScriptController):
	# called once the script is loaded
	def onLoaded(self,node):
		print('Controller script loaded from node %s'%node.findData('name').value)
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
		
		print('POS = ')
		print(goalPos)

		outfile = open('CircleTrajectory.csv', 'w')
		outfile.close()
		self.tStep = 0
		
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
		#print 'dt=' + str(dt)
		
		
		angle = angle+ dt*2*Pi/time_circle;
		
		#goalPos = goalState.findData('position').value
		
		goalPos[0][1]=radius*cos(angle);
		goalPos[0][2]=radius*sin(angle);
		#print goalPos
		goalState.findData('position').value = str(goalPos[0][0])+' '+  str(goalPos[0][1])+' ' +str(goalPos[0][2]) + ' 0 0 0 1';
		
		outfile = open('CircleTrajectory.csv', 'a')
		outfile.write(";".join([str(self.tStep), str(goalPos[0][1]/1000), str(goalPos[0][2]/1000) ])+'\n')
		outfile.close()
		
		self.tStep += 1		
		
		return 0

