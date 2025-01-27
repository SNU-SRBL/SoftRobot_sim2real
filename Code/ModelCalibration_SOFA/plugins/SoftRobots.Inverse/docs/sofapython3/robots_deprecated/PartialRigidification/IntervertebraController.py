from __future__ import division #for default floating point division
import Sofa
import random
from math import*

global dim, degree, controlPoints, pythonNode
dim = 3
degree = 3
#controlPoints = [5.2289833, 0, -13.032512, 16.331092, 0, -12.243574,  4.3410441, 0, -30.59501, 12.685578, 0, -30.002031, 20.146103, 0, -30.59501, 8.1560552, 0, -12.243574, 19.258164, 0, -13.032512]
#controlPoints = [5.2289833, 0, -13.032512, 16.331092, 0, -12.243574, 4.3410441, 0, -30.59501, 12.685578, 0, -30.002031, 21.030111899999998, 0, -30.59501, 9.040063999999997, 0, -12.243574, 20.1421727, 0, -13.032512]
controlPoints = [0.0, 0.0, -11.195709758720001, 9.537377499822002, 0.0, -10.51796468044, -0.7627930491519992, 0.0, -26.2829492906, 6.405662242981999, 0.0, -25.77354475086, 13.574117535115999, 0.0, -26.2829492906, 3.2739469861419974, 0.0, -10.51796468044, 12.811324485964, 0.0, -11.195709758720001]
# utility methods

def createScene(rootNode):
	global pythonNode
	global constraintSolver
	#global fixedComponent
	pythonNode = rootNode.addObject('PythonScriptController', filename="IntervertebraController.py", classname="IntervertebraController")
	animationLoop = rootNode.addObject('FreeMotionAnimationLoop', name='freemotion')
	constraintSolver = rootNode.addObject('GenericConstraintSolver', name='constraintSolver', printLog='1')

	
	#fixedComponent = [pythonNode.name , constraintSolver.name, animationLoop.name]
	return 0

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
	
	

# create the topology for the surface (made of quad) of a cylinder
# NumPointsOnSection defines the number of points for each section
# NumSection defines the number of section

def createCylinderSurfaceMesh(NumPointsOnSection,NumSection):

	QuadList= [0]*4*NumPointsOnSection*(NumSection-1)
	
	q=0;
	for s in range(NumSection-1):
		for p in range(NumPointsOnSection-1):
			QuadList[ q   ]= p + s*NumPointsOnSection
			QuadList[ q+1 ]= p+1 + s*NumPointsOnSection
			QuadList[ q+2 ]= p+1 + (s+1)*NumPointsOnSection
			QuadList[ q+3 ]= p + (s+1)*NumPointsOnSection
			q=q+4
			
		
		# le dernier quad pour "refermer" la section
		QuadList [ q   ] = (NumPointsOnSection-1) + NumPointsOnSection * s	
		QuadList [ q+1 ] =  NumPointsOnSection * s		
		QuadList [ q+2 ] =  NumPointsOnSection * (s+1)	
		QuadList [ q+3 ] = (NumPointsOnSection-1) + NumPointsOnSection * (s+1)
		q=q+4
		
	return QuadList
	


# on definie la position de la base du cylindre
# on definie son axe
# a partir d'un "profil", on positionne les points du cylindre

def posGeneralizedCylinder(NumPointsOnSection,NumSection,posBase, Axis,posProfile):	

	posCylinder = [0]*3*NumPointsOnSection*NumSection;
	
	print("len(posProfile)", len(posProfile))
	numPosProfile = len(posProfile)//3;
	
	if NumSection != numPosProfile:
		print('problem: NumSection ' + str(NumSection) + ' is not equal to numPosProfile '+ str(numPosProfile))
	
	
	
	# computation of the center and the radius of each section
	radiusSection = [0]*NumSection;
	CenterSection = [0]*3*NumSection;
	
	for s in range(NumSection):
		P0Ps=[0]*3;
		

		# surface of revolution centered un posBase
		P0Ps[0]= posProfile[3*s  ] - posBase[0];
		P0Ps[1]= posProfile[3*s+1] - posBase[1];
		P0Ps[2]= posProfile[3*s+2] - posBase[2];
		
		#dot P0Ps . axis
		alpha=0;
		for i in range(3):
			alpha = alpha + P0Ps[i]*Axis[i]
	
		for i in range(3):
			CenterSection[3*s+i] = posBase[i] + alpha * Axis[i];

		radiusSquare=0;
		for i in range(3):
			radiusSquare = radiusSquare + (CenterSection[3*s+i] - posProfile[3*s+i]) * (CenterSection[3*s+i] - posProfile[3*s+i])
		
		radiusSection[s] = sqrt(radiusSquare)
		
		#local coordinates of the section
		x=[0]*3;
		y=[0]*3;
		for i in range(3):
			x[i] = (posProfile[3*s+i]-CenterSection[3*s+i])/radiusSection[s]
		
		Axis=normalize(Axis)
		y=cross(Axis,x)

				
		#place the points of the section
		angle=2*3.141592653589793/NumPointsOnSection;
		for p in range(NumPointsOnSection):
			ind=NumPointsOnSection*s+p;
			for i in range(3):
				posCylinder[3*ind+i] = CenterSection[3*s+i] + (x[i]*cos(p*angle) + y[i]*sin(p*angle))*radiusSection[s]
		
		
		
		

	
	return posCylinder


def rotateVertebraZ(points, angle):
	nVertex = len(points)//3
	
	for i in range(nVertex):
		p = points[3*i:3*(i+1)]
		
		points[3*i+0] = p[0]*cos(angle) - sin(angle)*p[2]
		points[3*i+2] = p[0]*sin(angle) + p[2]*cos(angle)

def generalizedCylinder(circularSection, profile, origin, axis, offset):
	
	nProfilePts = len(profile)//3
	
	#minX = min(profile[::3])
	outCoords = [0]*3*circularSection*nProfilePts
	
	for s in range(nProfilePts):
		
		localP = [coord for coord in profile[3*s:3*(s+1)]]
		
		#localP[0] -= minX
		localP[2] -= origin[2]
		
		
		for p in range(circularSection):
			i = circularSection*s + p
			r = localP[2]
			outCoords[3*i+0] = localP[0]
			outCoords[3*i+1] = r*sin(i*(2*pi/circularSection))
			outCoords[3*i+2] = r*cos(i*(2*pi/circularSection))
			#print str(outCoords[3*p:3*(p+1)])
			
	angle = acos(dot([1, 0, 0], axis))
	print('Angle : ' + str(angle))
	
	rotateVertebraZ(outCoords, angle)
	
	for p in range(2,len(outCoords),3):
		outCoords[p] += origin[2]
		
	#for p in range(0,len(outCoords),3):
		#outCoords[p] += minX
		
	#for coord in range(2,len(outCoords),3):
		#outCoords[coord] += axis[2]*offset		
		
	for coord in range(len(outCoords)):
		outCoords[coord] += axis[coord%3]*offset
			
	return outCoords
		


def evalBezier3(dim, cpOrig, nPts, rBegin, rEnd, posBase, offset):
	#print "Eval bezier curve for rBegin=" + str(rBegin) + " and rEnd=" +str(rEnd)
	curve = []
	cp = [cpOrig[i] for i in range(len(cpOrig))]
	
	
	#for i in range(0,len(cp), 3):
		#cp[i] -= minX
		
	#for i in range(0,len(cp),3):
		#cp[i] *= xScale

	#for i in range(0,len(cp), 3):
		#cp[i] += minX
	
	# putting back profile to base position befor scaling
	for i in range(len(cp)):
		cp[i] -= posBase[i%3]
		
	cp[dim-1] = cp[dim-1]*rBegin
	cp[2*dim-1] = cp[2*dim-1]*rBegin
	cp[-1] = cp[-1]*rEnd
	cp[-(dim+1)] = cp[-(dim+1)] * rEnd
	
	for i in range(len(cp)):
		cp[i] += posBase[i%3]
	
	
	global degree
	nSegment = ((len(cp)//dim)-1)//degree
	
	for p in range(nPts):
		segment = int((p*nSegment)/(nPts))
		t = ((p*nSegment)/(nPts-1)) - segment
		
		spanStart = segment*degree
		spanEnd = spanStart + degree + 1
		span = cp[3*spanStart:3*spanEnd]
		p0 = span[0:dim]
		p1 = span[dim:2*dim]
		p2 = span[2*dim:3*dim]
		p3 = span[3*dim:4*dim]
	
		#print str(p0) + ", " + str(p1) + ", " + str(p2) + ", " + str(p3)
		P = [0]*dim
		for d in range(dim):
			P[d] = ((1-t)**3)*p0[d] + (3*t*((1-t)**2))*p1[d] + 3*((1-t)*(t**2))*p2[d] + (t**3)*p3[d]
			
		#print 'P'+str(p) + " : " + str(P)
		#print str(p) + " : " + str(P)
		P[0] = P[0] + offset
		curve = curve + P
				
		
	return curve


# generates a set of radii for each intervertebra
def linspace(a, b, n):
	return [a+i*((b-a)/n) for i in range(n+1)]

#	on definie des courbes de bezier de degre 3 

def bezierLine(inputNodes, numNodes, N):
	numLines = (numNodes-1)/3;
	
	dx=(numLines+0.0)/(N-1);
	

	
	position = [0]*3*N
	
	# on passe sur les differents points
	xglobal=0;
	line=0;
	for p in range(N): 
		
		while xglobal>line+1:
			line=line+1;
			
		if line > numLines-1:
			line = line-1;
		
		x = xglobal-line;
		
		# N0.x = inputNodes[9*line]
		# N0.y = inputNodes[9*line+1] 
		# N0.z = inputNodes[9*line+2]  

		# N1.x = inputNodes[9*line+3]
		# N1.y = inputNodes[9*line+4] 
		# N1.z = inputNodes[9*line+5]  
		
		# N2.x = inputNodes[9*line+6]
		# N2.y = inputNodes[9*line+7] 
		# N2.z = inputNodes[9*line+8]  
		
		# N3.x = inputNodes[9*line+9]
		# N3.y = inputNodes[9*line+10] 
		# N3.z = inputNodes[9*line+11]  						
		
		
		
		pos = [ (1-x)*(1-x)*(1-x)*inputNodes[9*line] + 3*x*(1-x)*(1-x)*inputNodes[9*line+3] +  3*x*x*(1-x)*inputNodes[9*line+6] + x*x*x*inputNodes[9*line+9],
			(1-x)*(1-x)*(1-x)*inputNodes[9*line+1] + 3*x*(1-x)*(1-x)*inputNodes[9*line+4] +  3*x*x*(1-x)*inputNodes[9*line+7] + x*x*x*inputNodes[9*line+10],
			(1-x)*(1-x)*(1-x)*inputNodes[9*line+2] + 3*x*(1-x)*(1-x)*inputNodes[9*line+5] +  3*x*x*(1-x)*inputNodes[9*line+8] + x*x*x*inputNodes[9*line+11]]
		
		
		position[3*p] = pos[0];
		position[3*p+1] = pos[1];
		position[3*p+2] = pos[2];
		
		xglobal=xglobal+dx;
		
	return position 
		


def rotateTablePosAlongX(Table, angle):
	sizeT = len(Table)
	numP=sizeT//3;
	rotatedTable=[0]*numP*3;
	
	for p in range(numP):		
		#rotation
		rotatedTable[3*p] = Table[3*p] # no transformation along x
		rotatedTable[3*p+1] = Table[3*p+1]*cos(angle) + Table[3*p+2]*sin(angle)			
		rotatedTable[3*p+2] =-Table[3*p+1]*sin(angle) + Table[3*p+2]*cos(angle)			
		
		
	return rotatedTable

def createCopyofListWithOffset( inputList, offset):
	#size of the mesh list
	s=len(inputList)
	#allocation of the memory
	ListCopy=[0]*s;
	
	for i in range(s):
		ListCopy[i]= inputList[i]+offset
	
	return ListCopy

def TableOfTheNFirstIndexAfterM(N,M):
	outTable=[0]*N
	for i in range(N):
		outTable[i] = M+i
	return outTable
	
def TableOfTheNLastIndexBeforeM(N, M):
	outTable=[0]*N
	for i in range(N):
		outTable[i] = M-N+i
	return outTable
	

def MultiplyTableIndex(Table, N):
	s = len(Table)
	outTable=[0]*N*s
	for i in range(s):
		for j in range(N):
			outTable[N*i+j] = N*Table[i]+j
	
	return outTable


def transformTablePosInString(Table):
	numPos = len(Table)//3;
	strPos= ' ';
	for p in range(numPos):
		strPos = strPos+ str(Table[3*p])+' '+str(Table[3*p+1])+' '+str(Table[3*p+2])+' '
		
	return strPos

def transformTableInString(Table):
	sizeT =  len(Table);
	strOut= ' ';
	for p in range(sizeT):
		strOut = strOut+ str(Table[p])+' '
		
	return strOut


def transformDoubleTable(DoubleTable):
	numRow= len(DoubleTable);
	if numRow>0:
		numCol = len(DoubleTable[0])
	SimpleTable=[0]*numCol*numRow
	
	for r in range(numRow):
		for c in range(numCol):
			SimpleTable[numCol*r +c ] = DoubleTable[r][c]
	return  SimpleTable
	

def findPointThatMoves(InitPos, CurrentPos):
	numRow= len(InitPos);
	
	for p in range(numRow):
		dx=diff(InitPos[p], CurrentPos[p])
		normS=normSquare(dx)
		if normS > 1e-8:
			return p
	return -1



def interactiveRules(posBase, Axis, InitPos, CurrentPos):

	p_global = findPointThatMoves(InitPos, CurrentPos);
	
	if p_global<0:
		return CurrentPos

	
	i_float = floor(p_global/6.0);
	i = int(i_float)
	
	# particular case: the last node was moved
	if 6*i+6> len(CurrentPos):
		i=i-1
	
	print('in interactiveRules')
	print(i)
	
	p = p_global-i;
	
	if p<0:
		return CurrentPos
	elif p==0:
		#print 'p1 has moved' => move p2 accordingly
		p6p7 = diff(CurrentPos[6*i+6],CurrentPos[6*i+5]) 
		CurrentPos[6*i+1] = plus(CurrentPos[6*i],p6p7)
		if i>0:
			# p1 is not the "first" point
			print('p1 is not the first point: to do')
		
		
	elif p==1:
		p1= CurrentPos[6*i]
		p7= CurrentPos[6*i+6]
		# 12 parallel to axis : p2 = p1 + axis*norm(p1-CurrentPos)
		p1p2=diff(CurrentPos[6*i+1], p1)
		p1p2=mult_scalar(Axis,norm(p1p2))
		CurrentPos[6*i+1]=plus(p1,p1p2)
		# 6 ( 67 equal to 12
		CurrentPos[6*i+5] = diff(p7,p1p2) 
		
	elif p==2:
		print('p3 has moved')
	elif p==3:
		p1= CurrentPos[6*i]
		p7= CurrentPos[6*i+6]
		#p4 has moved
		p1p7=diff(p7, p1)
		p1p4=diff(CurrentPos[6*i+3], p1)
		proj7 = dot(Axis,p1p7)
		proj4 = dot(Axis,p1p4)
		p1p4T=diff(p1p4, mult_scalar(Axis,proj4))  # tangential direction is not modified
		p4 = plus(p1, mult_scalar(Axis,(proj7/2)))
		CurrentPos[6*i+3] = plus(p4,p1p4T)
		
		
	elif p==4:
		print('p5 has moved')
	elif p==5:
		p1= CurrentPos[6*i]
		p7= CurrentPos[6*i+6]
		# 67 parallel to axis : p6 = p7 - axis*norm(p7-CurrentPos)
		p6p7=diff(p7, CurrentPos[6*i+5])
		p6p7=mult_scalar(Axis,norm(p6p7))
		CurrentPos[6*i+5]=diff(p7,p6p7)
		# 2 ( 67 equal to 12
		CurrentPos[6*i+1] = plus(p1,p6p7) 


	elif p==6:
		# 'p7 has moved' => move p6 accordingly
		p1p2 = diff(CurrentPos[6*i+1],CurrentPos[6*i]) 
		CurrentPos[6*i+5] = diff(CurrentPos[6*i+6],p1p2)		
		
	CurrentPos=initRules(posBase, Axis, CurrentPos)					
	
	return CurrentPos


# geometric rules for the robotino parameters

def initRules(posBase, Axis, CurrentPos):
	numRow= len(CurrentPos);
	numIntervertebra = (numRow-1) /6;
	
	for i in range(numIntervertebra):
		p1= CurrentPos[6*i]
		p7= CurrentPos[6*i+6]
		# 12 parallel to axis : p2 = p1 + axis*norm(p1-CurrentPos)
		p1p2=diff(CurrentPos[6*i+1], p1)
		p1p2=mult_scalar(Axis,norm(p1p2))
		p2=plus(p1,p1p2)
		
		# 4 in the middle of 1 and 7 when projected on axis
		p1p7=diff(p7, p1)
		p1p4=diff(CurrentPos[6*i+3], p1)
		proj7 = dot(Axis,p1p7)
		proj4 = dot(Axis,p1p4)
		p1p4T=diff(p1p4, mult_scalar(Axis,proj4))  # tangential direction is not modified
		p4 = plus(p1, mult_scalar(Axis,(proj7/2)))
		p4 = plus(p4,p1p4T)
		
		#3 and 5 (length 34 and 45 equal and parllel to axis
		p3p5 = diff(CurrentPos[6*i+4], CurrentPos[6*i+2])
		p3p4length= dot(Axis,p3p5)/2.0
		p3 = plus(p4,mult_scalar(Axis,-p3p4length))
		p5 = plus(p4,mult_scalar(Axis,p3p4length))
		
		# 6 ( 67 equal to 12
		p6 = diff(p7,p1p2) 
		
		
		# output (1 and 7 are unchanged)
		CurrentPos[6*i+1]=p2
		CurrentPos[6*i+2]=p3
		CurrentPos[6*i+3]=p4
		CurrentPos[6*i+4]=p5
		CurrentPos[6*i+5]=p6

	
	return CurrentPos
	

def computeBBox(position):
	
	minX = float('inf')
	minY = float('inf')
	minZ = float('inf')
	
	maxX = -minX
	maxY = -minY
	maxZ = -minZ
	
	for p in position:
		
		if p[0] < minX:
			minX = p[0]
			
		if p[0] > maxX:
			maxX = p[0]
			
		if p[1] < minY:
			minY = p[1]
			
		if p[1] > maxY:
			maxY = p[1]
			
		if p[2] < minZ:
			minZ = p[2]
			
		if p[2] > maxZ:
			maxZ = p[2]
			
	
	return ([minX, minY, minZ], [maxX, maxY, maxZ])
			

############################################################################################
# this is a PythonScriptController script
############################################################################################





class IntervertebraController(Sofa.PythonScriptController):
	
	# parameters of the intervertebra
	def setParameters(self,NumNodesCurve, NumSection, NumPointsOnSection):
		self.numNodeCurve= NumNodesCurve
		self.numSection=NumSection
		self.numPointsOnSection=NumPointsOnSection
		return 0
	
	# called once the script is loaded
	def onLoaded(self,node):
		print('Controller script loaded from node %s'%node.findData('name').value)
		return 0



	# called once graph is created, to init some stuff...
	def initGraph(self,node):
		self.nStep = 11
		self.nVertebra = 16
		self.firstStep=0
		self.radii = linspace(1, 0.7259259, self.nVertebra)
		# store the rootNode
		self.rootNode = node.getRoot()
		self.sceneNode = self.rootNode.addChild('SceneNode')
		# store the engine 
		#global HexaExtruEngine;
		#HexaExtruEngine = node.getObject('Surface/engine')
		#global GenericConstraintSolver;
		#GenericConstraintSolver = node.getObject('constraintSolver');
		
		self.vertebraLen = controlPoints[len(controlPoints)-3] - controlPoints[0]
		self.numNodesCurve = 7
		self.NumSection = 9
		self.NumPointsOnSection = 24
		self.NumSlices=2
		self.baseFrameXCoord = 18.77;
		self.frameXCoord = 18.77;

		print('Scene init.')
		print('Parameters :')
		print('# of vertebra:' + str(self.nVertebra))
		print('# of control points: ' + str(self.numNodesCurve))
		print('# of section for vertebra : ' + str(self.NumSection))
		print('# of points for vertebra section: ' + str(self.NumPointsOnSection))
		print('# of slice for vertebra: ' + str(self.NumSlices))
		print('vertebra length: ' + str(self.vertebraLen))
		print('Radii set: ' + str(self.radii))
		
		#node.getObject('baseCamera').findData('minBBox').value = '-60 '*3
		#node.getObject('baseCamera').findData('maxBBox').value = '60 '*3
		
		#print self.numNodesCurve
		#print self.NumSection
		#print self.NumPointsOnSection
		#print self.NumSlices


		
		return 0
		
	def sortNodes(self, numNodes, posHexa):
	
		# numNode = 3(cavite) * NumSection * NumPointsOnSection * (NumSlices+1)
		


		
		if numNodes != 3 * self.NumSection * self.NumPointsOnSection * (self.NumSlices+1):
			print('Error when providing variables')
		else:
			print('everything s all right')
			
		
		posIndep = [0]*3*3* (self.NumSection-1) * self.NumPointsOnSection * (self.NumSlices+1)
		posRigid = [0]*3*3 * self.NumPointsOnSection * (self.NumSlices+1)
		IndexFixed = [0]*3*self.NumPointsOnSection * (self.NumSlices+1)
		TableSubSetMap = [0,0]*numNodes

		

		
		i_indep=0;
		i_rigid=0;
		i_fixed=0;
		for p in range(numNodes):
			
			p_ref=p%(numNodes/3)
			
			# independant Nodes
			if p_ref < (self.NumSection-1) * self.NumPointsOnSection * (self.NumSlices+1):
			
				# store the position of the independant nodes in a list
				
				for i in range(3):
					a = posHexa[p][i]
					posIndep[3*i_indep+i] = a

				
				# particular case: store the indices of the fixed nodes
				# when considering the hole robot, this part is mapped under the 'rigid'
				if p_ref < self.NumPointsOnSection * (self.NumSlices+1):
					IndexFixed[i_fixed]=i_indep;
					i_fixed = i_fixed + 1;
					
				TableSubSetMap[2*p]=0 # independant point
				TableSubSetMap[2*p+1]=i_indep; # index in the independant state
				
				i_indep = i_indep +1;	
				
				
			else:
				for i in range(3):
					posRigid[3*i_rigid+i] = posHexa[p][i]
					
				TableSubSetMap[2*p]=1 # mapped on rigid 
				TableSubSetMap[2*p+1]=i_rigid; # index in the rigid mapped state			
				
				i_rigid = i_rigid +1;
				
		
		print 
			
		
		
		
		return [posIndep, posRigid, IndexFixed, TableSubSetMap]



	# called on each animation step
	total_time = 0
	def onBeginAnimationStep(self,dt):

		#print "root has " + str(len(children)) + " children"
		global pythonNode
		global constraintSolver
		#constraintSolver.reinit()
		

				

		# on even time steps we create geometry
		# on odd time steps, we perform simulation and compute compliance matrix
		if(self.nStep >= self.nVertebra) :
			return 
		print("Step : " + str(self.nStep))
		#if (self.nStep > 0) :
		
		# Clean-up scene graph
		
		
		children = self.rootNode.getChildren()
		#print "root has " + str(len(children)) + " child obj"
		for child in children:
			print(child.name)
			if( child.name != pythonNode.name ) :
				self.rootNode.removeChild(child)				

		print
		
		objects = self.sceneNode.getObjects()
		#print "Scene node " + str(len(objects)) + " child obj"
		for child in objects :
				#print child.name + " " + str(type(child))
				self.rootNode.removeObject(child)	
				
				
		#define initial position
		
		posBase=[5.191767153364891, 0.0, -39.538169209096495];
		Axis=[0.9974846191374479, 0, 0.070883246146185117];
		posTop = [0]*3;
		global controlPoints
		for i in range(3):
			posTop[i]= posBase[i] + 30*Axis[i]
			
		nAxis = normalize(Axis)
		
		pos = [0]*3
		pos[0] = posBase[0]
		pos[1] = posBase[1]
		pos[2] = posBase[2]
		
		#for i in range(3):
			#pos[i] = posBase[i] + self.vertebraLen*nAxis[i]*self.nStep
		#pos[2] = posBase[2] + self.vertebraLen*nAxis[2]*self.nStep
		
		#pos = [p for p in posBase]
		#pos[2] *= self.radii[self.nStep]
		print('Posbase : ' + str(pos))
		#posProfile = evalBezier3(dim, controlPoints, self.N, self.radii[self.nStep], self.radii[self.nStep+1], pos)
		posProfile = []
		#for i in range(3):
		posProfile =  evalBezier3(dim, controlPoints, self.NumSection, self.radii[self.nStep], self.radii[self.nStep+1], pos, 0)
		#posProfile =  evalBezier3(dim, controlPoints, self.NumSection, self.radii[0], self.radii[0], pos)
		
		#posProfile = bezierLine(controlPoints, len(controlPoints)//3, 7)
		
		# first surface along the profile	
		#posCylinder = posGeneralizedCylinder(self.NumPointsOnSection, self.NumSection, pos, Axis, posProfile);
		#print 'Len posGeneralizedCylinder ' + str(len(posCylinder))
		posCylinder = generalizedCylinder(self.NumPointsOnSection, posProfile, posBase, Axis, self.vertebraLen*self.nStep) 
		#print 'Len generalizedCylinder ' + str(len(posCylinder))

		posCylinder = rotateTablePosAlongX(posCylinder, -pi/2)

		strPosCylinder= transformTableInString(posCylinder);

		posCylinderR1 = rotateTablePosAlongX(posCylinder, (2/3)*pi)
		strPosCylinder2=transformTablePosInString(posCylinderR1);
		
		# computation of the second rotated surface

		posCylinderR2 = rotateTablePosAlongX(posCylinder, (4/3)*pi)
		strPosCylinder3=transformTablePosInString(posCylinderR2);
		
	
		#test = posCylinder + posCylinderR1
		strMergeSurfacePos = strPosCylinder+ ' ' + strPosCylinder2 + ' ' + strPosCylinder3	
		
		strMergeSurfacePos = strPosCylinder+ ' ' + strPosCylinder2 + ' ' + strPosCylinder3

		
		## Creation of the topology of the original surface
		QuadList=createCylinderSurfaceMesh(self.NumPointsOnSection, self.NumSection);
		strQuadList= transformTableInString(QuadList);
		
		# Creation of the topology of the first rotated surface 
		numNodes = self.NumPointsOnSection*self.NumSection;
		QuadList2 = createCopyofListWithOffset(QuadList, numNodes);
		strQuadList2= transformTableInString(QuadList2);
		
		# Creation of the topology of the second rotated surface
		QuadList3 = createCopyofListWithOffset( QuadList, 2*numNodes);
		strQuadList3= transformTableInString(QuadList3);
		
		strMergeSurfaceTopo = strQuadList+ ' ' + strQuadList2 + ' ' + strQuadList3
		
		strNumSlices= str(self.NumSlices)
		numSurfacePoint= self.NumPointsOnSection*self.NumSection;
		
		#buf=TableOfTheNFirstIndexAfterM(self.NumPointsOnSection, 0)
		#i0_1 = MultiplyTableIndex(buf, self.NumSlices+1)
		
		#buf=TableOfTheNFirstIndexAfterM(self.NumPointsOnSection, numSurfacePoint)
		#i0_2 = MultiplyTableIndex(buf, self.NumSlices+1)
		
		#buf=TableOfTheNFirstIndexAfterM(self.NumPointsOnSection, 2*numSurfacePoint)
		#i0_3 = MultiplyTableIndex(buf, self.NumSlices+1)	
		
		#strI0_1 = transformTableInString(i0_1);
		#strI0_2 = transformTableInString(i0_2);
		#strI0_3 = transformTableInString(i0_3);
		
		#mergeR0= strI0_1 + ' ' + strI0_2 + ' ' +strI0_3
		
			
		### R1
		
		#buf=TableOfTheNLastIndexBeforeM(self.NumPointsOnSection, numSurfacePoint)
		#i1_1 = MultiplyTableIndex(buf, self.NumSlices+1)
		
		#buf=TableOfTheNLastIndexBeforeM(self.NumPointsOnSection, 2*numSurfacePoint)
		#i1_2 = MultiplyTableIndex(buf, self.NumSlices+1)
		
		#buf=TableOfTheNLastIndexBeforeM(self.NumPointsOnSection, 3*numSurfacePoint)
		#i1_3 = MultiplyTableIndex(buf, self.NumSlices+1)	

		#strI1_1 = transformTableInString(i1_1);
		#strI1_2 = transformTableInString(i1_2);
		#strI1_3 = transformTableInString(i1_3);
		
		#mergeR1= strI1_1 + ' ' + strI1_2 + ' ' +strI1_3

		#self.rootNode.addObject('DefaultAnimationLoop')
		#self.rootNode.addObject('DefaultVisualManagerLoop')
		self.sceneNode = self.rootNode.addChild('SceneNode')
		#self.sceneNode.addObject('MeshSTLLoader', filename='Robotino.stl')
		#self.sceneNode.addObject('OglModel', src='@Robotino.stl')
		
		#animationLoop = self.sceneNode.addObject('FreeMotionAnimationLoop', name='freemotion')
		#constraintSolver = self.sceneNode.addObject('GenericConstraintSolver', name='constraintSolver', printLog='1')		
		self.sceneNode.addObject('VisualStyle', displayFlags='showVisualModels showBehaviorModels hideCollisionModels hideMappings showForceFields')
		#camera = self.sceneNode.addObject('InteractiveCamera', position='0 0 10', minBBox='-600 -600 -600', maxBBox='600 600 600')
		self.sceneNode.findData('dt').value=0.001
		self.sceneNode.findData('gravity').value = '0 0 0'
		#self.sceneNode.addObject('MeshObjLoader', filename='Robotino.obj', name='robotino', translation='-150 10 0', rotation='0 0 -40')
		#self.sceneNode.addObject('OglModel', src='@robotino')


		surfaceNode = self.sceneNode.addChild('Surface')
		quadSet = surfaceNode.addObject('QuadSetTopologyContainer', name='topo', position=strMergeSurfacePos, quads=strMergeSurfaceTopo)
		surfaceNode.addObject('MechanicalObject', template='Vec3', position='@topo.position')
		visu = surfaceNode.addObject('OglModel',name='visu', src='@topo')
		hexaExtruEngine = surfaceNode.addObject('ExtrudeQuadsAndGenerateHexas', name='engine', template='Vec3', thicknessIn='0.5',  thicknessOut='0.5', numberOfSlices=strNumSlices, surfaceVertices='@topo.position', surfaceQuads='@topo.quads' )
		
		quadSet.init()
		hexaExtruEngine.init()
		visu.init()
		

			
		#global HexaExtruEngine;
		#global GenericConstraintSolver;
		#print 'TEST2'
		posHexa = hexaExtruEngine.findData('extrudedVertices').value
		HexaTopology = hexaExtruEngine.findData('extrudedHexas').value # useful ?
		
		posHexaStr = transformTableInString(transformDoubleTable(posHexa));
		HexaTopologyStr= transformTableInString( transformDoubleTable(HexaTopology)  );
		
		numNodes=len(posHexa)
		
		#print '------------'
		#print posHexa[0] 
		#print '------------'
		
		[posIndep, posRigid, IndexFixed, TableSubSetMap]= self.sortNodes(numNodes, posHexa)
		posIndepStr = transformTableInString(posIndep);
		posRigidStr = transformTableInString(posRigid);
		IndexFixedStr= transformTableInString(IndexFixed);
		TableSubSetMapStr=transformTableInString(TableSubSetMap);
		
		
		#print IndexFixed
		
		
		### Create the composite Model
		
		indepMass=0.00001
		
		compositeNode = self.sceneNode.addChild('CompositeModel')
		compositeNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0.0', rayleighMass='0', firstOrder=True)
		#compositeNode.addObject('StaticSolver')
		##compositeNode.addObject('PCGLinearSolver',name='linear solver',iterations='200',tolerance='1.0e-18',threshold='1.0e-30', preconditioners="precond")
		compositeNode.addObject('SparseLUSolver', name="precond")
		GenericConstraintCorrection=self.sceneNode.addObject('GenericConstraintCorrection', solverName="./CompositeModel/precond")
		#GenericConstraintCorrection=compositeNode.addObject('GenericConstraintCorrection', solverName="precond")
		###  independant Particles
		indep_particulesNode = compositeNode.addChild('Independant_Particules')
		indep_particulesNode.addObject('PointSetTopologyContainer', position=posIndepStr)
		IndependantParticles_dof=indep_particulesNode.addObject('MechanicalObject', template='Vec3', name='IndependantParticles_dof')
		indep_particulesNode.addObject('UniformMass',name='mass',totalMass=str(indepMass/self.nVertebra))
		indep_particulesNode.addObject('FixedConstraint', indices=IndexFixedStr)
		##child node for the multi-mapping
		mecaNode = indep_particulesNode.addChild('Meca')
			
		
		##  Rigid dof
		framePosition = (self.nStep+1)*12.77
		#framePosition = 12.77
		rigidMass = 0.000001
		FramesNode = compositeNode.addChild('Frame_Node')
		FramesNode.addObject('MechanicalObject', template="Rigid3",name='rigid_frame',position=str(framePosition)+' 0 0.0 0 0 0 1')
		FramesNode.addObject('UniformMass',name='mass',totalMass=str(rigidMass),showAxisSizeFactor='10')
		#FramesNode.addObject('RestShapeSpringsForceField', points='0', stiffness='0', angularStiffness='1e14')
		#FramesNode.addObject('FixedConstraint', indices='0')
		FramesNode.addObject('PartialRigidificationConstraint')
		
		
		## Particle linked to the rigid
		Mapped_ParticuleNode = FramesNode.addChild('Mapped_Particule')
		Mapped_ParticuleNode.addObject('PointSetTopologyContainer', position=posRigidStr)
		Mapped_Particles_dof=Mapped_ParticuleNode.addObject('MechanicalObject', template='Vec3', name='Mapped_Particles_dof',  showIndices=False)
		Mapped_ParticuleNode.addObject('RigidMapping', name="rigidMap", input='@..',output='@.', globalToLocalCoords=True)
		
		## Create the HexahedronForceField
		
		
		Mapped_ParticuleNode.addChild(mecaNode)
		
		mecaMass=0.01
		mecaNode.addObject('HexahedronSetTopologyContainer', position=posHexaStr, hexahedra=HexaTopologyStr)
		MecaState = mecaNode.addObject('MechanicalObject',name='VolumeState',template='Vec3', showIndicesScale='0.00001', showIndices='1')
		mecaNode.addObject('UniformMass', totalMass=str(mecaMass/self.nVertebra))
		mecaNode.addObject('TetrahedronFEMForceField', name="tetraFF",  youngModulus='1e4', poissonRatio='0.3', method='large', drawHeterogeneousTetra='1')
		deformableGrid_mappaddPointing = mecaNode.addObject('SubsetMultiMapping',template='Vec3,Vec3d',name='deformableGrid_mapping', input='@../../../CompositeModel/Independant_Particules/IndependantParticles_dof @../../../CompositeModel/Frame_Node/Mapped_Particule/Mapped_Particles_dof', output='@./VolumeState', indexPairs=TableSubSetMapStr)
		
		compositeNode.addObject('PartialRigidificationForceField', template="Vec3,Rigid3", object1='@./Independant_Particules/IndependantParticles_dof', object2='@./Frame_Node/rigid_frame', rigidMapping='@./Frame_Node/Mapped_Particule/rigidMap', subsetMultiMapping='@./Independant_Particules/Meca/deformableGrid_mapping', mappedForceField='@./Independant_Particules/Meca/tetraFF' )
		
		
		## reinit the component
		#print self.rootNode.getObject('freemotion').name
		#self.rootNode.getObject('freemotion').bwdInit()
		constraintSolver.init()
		GenericConstraintCorrection.bwdInit()
		#self.rootNode.init()
		
		#for obj in self.rootNode.getObjects():
			#if obj.name == 'baseCamera':
				#self.rootNode.removeObject('baseCamera')

		bbox = computeBBox(posHexa)
		bboxExtent = [bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1], bbox[1][2] - bbox[0][2]]
		bboxCenter = [ c/2 for c in bboxExtent]
		camPos = [c for c in bboxCenter]
		camDist = norm(bboxExtent)
		camPos[2] += camDist
		self.sceneNode.init()
		
		#self.rootNode.addObject('InteractiveCamera', name='baseCamera', position=transformTableInString(camPos), lookAt=transformTableInString(bboxCenter), minBBox=transformTableInString(bbox[0]), maxBBox=transformTableInString(bbox[1]))
		
		
		#self.rootNode.getObject('baseCamera').findData('position').value = transformTableInString(camPos)
		#self.rootNode.getObject('baseCamera').findData('lookAt').value = transformTableInString(bboxCenter)
		#self.rootNode.getObject('baseCamera').findData('distance').value = str(camDist)
		#self.rootNode.getObject('baseCamera').findData('zFar').value = str(camDist)
		self.rootNode.getObject('baseCamera').findData('minBBox').value = transformTableInString(bbox[0])
		self.rootNode.getObject('baseCamera').findData('maxBBox').value = transformTableInString(bbox[1])
		self.rootNode.getObject('baseCamera').reinit()
		#camera.findData('minBBox').value = '-60'*3
		self.nStep = self.nStep + 1
		return 0
	
	def onEndAnimationStep(self, dt):
		print("end")
		
	def draw(self):
	
		return 0
	
