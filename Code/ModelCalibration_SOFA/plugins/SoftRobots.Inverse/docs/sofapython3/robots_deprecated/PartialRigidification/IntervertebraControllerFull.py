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
	#global pythonNode
	#global constraintSolver
	#global fixedComponent
	pythonNode = rootNode.addObject('PythonScriptController', filename="IntervertebraControllerFull.py", classname="IntervertebraControllerFull")
	#animationLoop = rootNode.addObject('FreeMotionAnimationLoop', name='freemotion')
	#constraintSolver = rootNode.addObject('GenericConstraintSolver', name='constraintSolver', printLog='1')

	
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

def createCylinderSurfaceMesh(start, NumPointsOnSection, NumSection):

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
	
	minX = min(profile[::3])
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
		
	for coord in range(len(outCoords)):
		outCoords[coord] += axis[coord%3]*offset
			
	return outCoords
		


def evalBezier3(dim, cpOrig, nPts, rBegin, rEnd, posBase, offset):
	#print "Eval bezier curve for rBegin=" + str(rBegin) + " and rEnd=" +str(rEnd)
	curve = []
	cp = [cpOrig[i] for i in range(len(cpOrig))]
	
	minX = min(cp[0:len(cp):3])
	
	xScale = (rBegin+rEnd)/2
	
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
	numCol = 1
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
	
		

############################################################################################
# this is a PythonScriptController script
############################################################################################





class IntervertebraControllerFull(Sofa.PythonScriptController):
	
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
		global controlPoints
		self.nStep = 0
		self.nVertebra = 1
		self.nFullVertebra = 16
		self.firstStep=0
		self.firstVertebra=9
		self.radii = linspace(1, 0.7259259, self.nFullVertebra)
		#self.nVertebra = 1
		# store the rootNode
		self.rootNode = node.getRoot()
		#self.sceneNode = self.rootNode.addChild('SceneNode')
		# store the engine 
		#global HexaExtruEngine;
		#HexaExtruEngine = node.getObject('Surface/engine')
		#global GenericConstraintSolver;
		#GenericConstraintSolver = node.getObject('constraintSolver');
		
		if (self.firstVertebra + self.nVertebra) > self.nFullVertebra :
			self.nVertebra = self.nFullVertebra - self.firstVertebra
		
		self.vertebraLen = controlPoints[len(controlPoints)-3] - controlPoints[0]
		self.numNodesCurve = 7
		self.NumSection = 15
		self.NumPointsOnSection = 32
		self.NumSlices=2
		self.baseFrameXCoord = 18.77;
		self.frameXCoord = 18.77;

		self.force = [0, -300000, 0, 0, 0, 0]
		self.currentTime = 0
		self.ICRA_demo= True
		print('Scene init.')
		print('Parameters :')
		print('# of vertebra:' + str(self.nVertebra))
		print('# of control points: ' + str(self.numNodesCurve))
		print('# of section for vertebra : ' + str(self.NumSection))
		print('# of points for vertebra section: ' + str(self.NumPointsOnSection))
		print('# of slice for vertebra: ' + str(self.NumSlices))
		print('vertebra length: ' + str(self.vertebraLen))
		print('Radii set: ' + str(self.radii))
		
		posBase=[5.191767153364891, 0.0, -39.538169209096495];
		Axis=[0.9974846191374479, 0, 0.070883246146185117];
		posTop = [0]*3;
		for i in range(3):
			posTop[i]= posBase[i] + 30*Axis[i]
			
		nAxis = normalize(Axis)
		
		pos = [0]*3
		pos[0] = posBase[0]
		for i in range(3):
			pos[i] = posBase[i] + self.vertebraLen*nAxis[i]*self.nStep
		
		posProfile = []
		for i in range(self.firstVertebra, self.firstVertebra+self.nVertebra):
			posProfile[len(posProfile)-3:len(posProfile)] =  evalBezier3(dim, controlPoints, self.NumSection, self.radii[i], self.radii[i+1], pos,self.vertebraLen*(i))


		
		#posProfile = bezierLine(controlPoints, len(controlPoints)//3, 7)
		
		# first surface along the profile	

		posCylinder = generalizedCylinder(self.NumPointsOnSection, posProfile, posBase, Axis, self.vertebraLen*self.nStep) 

		posCylinder = rotateTablePosAlongX(posCylinder, -pi/2)

		strPosCylinder= transformTableInString(posCylinder);

		angle = (2.0/3.0)* 3.141592653589793;
		posCylinderR1 = rotateTablePosAlongX(posCylinder, (2/3)*pi)
		strPosCylinder2=transformTablePosInString(posCylinderR1);
		
		# computation of the second rotated surface
		angle  = (4.0/3.0)* 3.141592653589793;
		posCylinderR2 = rotateTablePosAlongX(posCylinder, (4/3)*pi)
		strPosCylinder3=transformTablePosInString(posCylinderR2);
		
	
		#test = posCylinder + posCylinderR1
		strMergeSurfacePos = strPosCylinder+ ' ' + strPosCylinder2 + ' ' + strPosCylinder3	
		
		strMergeSurfacePos = strPosCylinder+ ' ' + strPosCylinder2 + ' ' + strPosCylinder3

		'12.77 0 0.0 0 0 0 1'
		## Creation of the topology of the original surface

		QuadList=createCylinderSurfaceMesh(0, self.NumPointsOnSection, (self.NumSection-1)*self.nVertebra+1 );

		strQuadList= transformTableInString(QuadList);
		
		# Creation of the topology of the first rotated surface 
		numNodes = self.NumPointsOnSection*self.NumSection;
		QuadList2 = createCopyofListWithOffset(QuadList, len(posCylinder)//3);
		strQuadList2= transformTableInString(QuadList2);
		
		# Creation of the topology of the second rotated surface
		QuadList3 = createCopyofListWithOffset( QuadList, 2*len(posCylinder)//3);
		strQuadList3= transformTableInString(QuadList3);
		
		strMergeSurfaceTopo = strQuadList+ ' ' + strQuadList2 + ' ' + strQuadList3

		
		strNumSlices= str(self.NumSlices)

		self.sceneNode = self.rootNode.addChild('SceneNode')
	
		self.sceneNode.addObject('VisualStyle', displayFlags='showVisualModels showCollisionModels hideMappings')

		self.rootNode.findData('dt').value=0.01
		self.rootNode.findData('gravity').value = '0 0 0'
		


		surfaceNode = self.sceneNode.addChild('Surface')
		quadSet = surfaceNode.addObject('QuadSetTopologyContainer', name='topo', position=strMergeSurfacePos, quads=strMergeSurfaceTopo)
		#visu = surfaceNode.addObject('OglModel',name='visu', src='@topo')
		hexaExtruEngine = surfaceNode.addObject('ExtrudeQuadsAndGenerateHexas', name='engine', template='Vec3', thicknessIn='0.5',  thicknessOut='0.5', numberOfSlices=strNumSlices, surfaceVertices='@topo.position', surfaceQuads='@topo.quads' )
		#self.sceneNode.addObject('MeshObjLoader', filename='Robotino.obj', name='robotino', translation='-150 10 0', rotation='0 0 -40')
		#self.sceneNode.addObject('OglModel', src='@robotino')

		quadSet.init()
		hexaExtruEngine.init()
		#visu.init()
		


		posHexa = hexaExtruEngine.findData('extrudedVertices').value
		HexaTopology = hexaExtruEngine.findData('extrudedHexas').value # useful ?

		posHexaStr = transformTableInString(transformDoubleTable(posHexa));
		HexaTopologyStr= transformTableInString( transformDoubleTable(HexaTopology)  );

		fullArmNodes = transformDoubleTable(posHexa)
		fixedIndices = self.getFixedNodeIndices()
		independantNode = self.getIndependantPosition(fullArmNodes)

		#print str(independantNode)
		strFixed = str(fixedIndices).replace('[', '').replace(']', '').replace(',', '')
		strIndep = str(independantNode).replace('[', '').replace(']', '').replace(',', '')



		
		##print IndexFixed
		
		
		#### Create the composite Model
		
		compositeNode = self.sceneNode.addChild('CompositeModel')
		#compositeNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0.0', rayleighMass='0', firstOrder=True)
		compositeNode.addObject('StaticSolver', applyIncrementFactor='1')
		#compositeNode.addObject('SparseLUSolver')
		
		compositeNode.addObject('CGLinearSolver',name='linear solver',iterations='7000',tolerance='1.0e-40',threshold='1.0e-40', warmStart='0')

		indep_particulesNode = compositeNode.addChild('Independant_Particules')
		indep_particulesNode.addObject('PointSetTopologyContainer', position=strIndep)
		IndependantParticles_dof=indep_particulesNode.addObject('MechanicalObject', template='Vec3', name='IndependantParticles_dof')
		indep_particulesNode.addObject('UniformMass',name='mass',totalMass='0.00001')
		indep_particulesNode.addObject('FixedConstraint', indices=strFixed)

		###child node for the multi-mapping
		mecaNode = indep_particulesNode.addChild('Meca')
			
		frameSpacing = 12.77

		###  Rigid dof
		
		for vertebra in range(self.nVertebra):
			print(vertebra)
			framePosition = (str(frameSpacing*(self.firstVertebra+vertebra+1)) + ' 0 0 0 0 0 1 ')
			FramesNode = compositeNode.addChild('Frame_Node'+str(vertebra))
			FramesNode.addObject('MechanicalObject', template="Rigid3",name='rigid_frame',position=framePosition, showObject='1', showObjectScale='10')
			FramesNode.addObject('UniformMass',name='mass',totalMass='0.000001',showAxisSizeFactor='10')
			#FramesNode.addObject('RestShapeSpringsForceField', points='0', stiffness='0', angularStiffness='1e14')
			mappedSectionNode = FramesNode.addChild('mappedSection_'+str(vertebra))
			mappedNode = self.getRigidNodesVertebra(fullArmNodes, vertebra)
			strMapped = str(mappedNode).replace('[', '').replace(']', '').replace(',', '')
			#mappedSectionNode.addObject('PointSetTopologyContainer', position=strMapped)
			mappedDof = mappedSectionNode.addObject('MechanicalObject', template='Vec3', name='mappedSectionDof', position=strMapped, showIndices="0")
			mappedSectionNode.addObject('RigidMapping', input='@../rigid_frame', output='@./mappedSectionDof', globalToLocalCoords='1')
			#mappedSectionNode.addObject('SphereCollisionModel')
			mappedSectionNode.addChild(mecaNode)

		
		mecaNode.addObject('HexahedronSetTopologyContainer', position=posHexaStr, hexahedra=HexaTopologyStr)
		mecaNode.addObject('HexahedronSetGeometryAlgorithms', position=posHexaStr, hexahedra=HexaTopologyStr)
		MecaState = mecaNode.addObject('MechanicalObject',name='VolumeState',template='Vec3', showIndicesScale='0.00002', showIndices='0')
		mecaNode.addObject('UniformMass', totalMass='0.01')
		#mecaNode.addObject('SphereCollisionModel')
		mecaNode.addObject('TetrahedronFEMForceField', name="tetraFF",  youngModulus='1e4', method='large')
		multiMapTable = self.computeMultiMappingIndices()
		multiMapStr = str(multiMapTable).replace('[', '').replace(']', '').replace(',', '')
		subsetInputStr = '@SceneNode/CompositeModel/Independant_Particules/IndependantParticles_dof '
		for v in range(self.nVertebra):
			subsetInputStr += '@SceneNode/CompositeModel/Frame_Node'+str(v)+'/mappedSection_' + str(v) + '/mappedSectionDof '
		
		#print subsetInputStr
		deformableGrid_mappaddPointing = mecaNode.addObject('SubsetMultiMapping',template='Vec3,Vec3d',name='deformableGrid_mapping', input=subsetInputStr, output='@./VolumeState', indexPairs=multiMapStr)
		
		endFrame = compositeNode.getChild('Frame_Node'+str(self.nVertebra-1))
		self.forcefield = endFrame.addObject('ConstantForceField', name='cstFF', force=transformTableInString(self.force), points='0')
		
		visuNode = mecaNode.addChild('visu')
		self.glVisu = visuNode.addObject('OglModel',name='glVisu', position='@SceneNode/Surface/topo.extrudedVertices', triangles='@SceneNode/Surface/topo.extrudedQuads')
		visuNode.addObject('BarycentricMapping', input='@../VolumeState', output='@visu')
		#self.sceneNode.init()
		#self.rootNode.getObject('baseCamera').findData('minBBox').value = '-60 '*3
		#self.rootNode.getObject('baseCamera').findData('maxBBox').value = '60 '*3
		##camera.findData('minBBox').value = '-60'*3
		#self.nStep = self.nStep + 1
		
		print(str(self.glVisu.findData('material').value))
		
		return 0
		

		
	def getFixedNodeIndices(self):
		nodesPerSection = (self.NumSlices+1)*self.NumPointsOnSection
		sectionsPerArm = (self.NumSection-1)*self.nVertebra + 1
		nodesPerArm = nodesPerSection*sectionsPerArm
		
		fixedIndices = [0]*3*nodesPerSection
		#print 'nodesPerSection ' + str(nodesPerSection)
		#print 'nodesPerArm ' + str(nodesPerArm)
		for arm in range(3):
			for n in range(nodesPerSection):
				#print  str(n + arm*nodesPerArm)
				index = arm * (self.nVertebra*(self.NumSection-2)+1)*nodesPerSection
				fixedIndices[arm*nodesPerSection + n] = n + index

		return fixedIndices
	
	def getIndependantPosition(self, position):
		print('Num nodes ' + str(len(position)//3))
		nIndependantSection = (self.NumSection-2)*self.nVertebra + 1
		sectionsPerArm = (self.NumSection-1)*self.nVertebra + 1
		nodesPerSection = (self.NumSlices+1)*self.NumPointsOnSection
		nodesPerArm = nodesPerSection*sectionsPerArm
		independantPosition = [0]*3*3*nIndependantSection*nodesPerSection
		coord = 0
		
		print('Num indep ' + str(len(independantPosition)//3))
		for arm in range(3):
			for vertebra in range(self.nVertebra):
				
				start = -1
				if( vertebra == 0 ):
					start = 0
				else:
					start = 1
					
				for s in range(start, self.NumSection-1):
					for node in range(nodesPerSection):
						
						index = arm*nodesPerArm + (vertebra*(self.NumSection-1)+s)*nodesPerSection + node
						
						#print 'arm(' + str(arm) +') ; vertebra(' + str(vertebra) + ') section(' + str(s) + ') index = ' + str(index)
						independantPosition[coord + 0] = position[3*index + 0]
						independantPosition[coord + 1] = position[3*index + 1]
						independantPosition[coord + 2] = position[3*index + 2]
						coord += 3
						
		return independantPosition
	
	def getRigidNodesPosition(self, position):
		nRigidSection = self.nVertebra*3
		sectionsPerArm = (self.NumSection-1)*self.nVertebra + 1
		nodesPerSection = (self.NumSlices+1)*self.NumPointsOnSection
		nodesPerArm = nodesPerSection*sectionsPerArm
		
		rigid = [0]*3*nRigidSection*nodesPerSection
		
		coord = 0
		for arm in range(3):
			for r in range(self.nVertebra):
				for n in range(nodesPerSection):
					index = arm*nodesPerArm + (r+1)*(self.NumSection-1)*nodesPerSection + n
					rigid[coord + 0] = position[3*index + 0]
					rigid[coord + 1] = position[3*index + 1]
					rigid[coord + 2] = position[3*index + 2]
					coord += 3
					
		return rigid
	
	def getRigidNodesVertebra(self, position, vertebra):
		sectionsPerArm = (self.NumSection-1)*self.nVertebra + 1
		nodesPerSection = (self.NumSlices+1)*self.NumPointsOnSection
		nodesPerArm = nodesPerSection*sectionsPerArm
		
		rigid = [0]*3*3*nodesPerSection
		
		coord = 0
		for arm in range(3):
			for n in range(nodesPerSection):
				index = arm*nodesPerArm + (vertebra+1)*(self.NumSection-1)*nodesPerSection + n
				rigid[coord + 0] = position[3*index + 0]
				rigid[coord + 1] = position[3*index + 1]
				rigid[coord + 2] = position[3*index + 2]
				coord += 3
					
		return rigid
	
	def computeMultiMappingIndices(self):
		
		nRigidSection = self.nVertebra*3
		sectionsPerArm = (self.NumSection-1)*self.nVertebra + 1
		nodesPerSection = (self.NumSlices+1)*self.NumPointsOnSection
		nodesPerArm = nodesPerSection*sectionsPerArm
		
		print('Node per arm ' + str(nodesPerArm))
		print('section per arm ' + str(sectionsPerArm))
		
		table = [0]*3*nodesPerArm*2
		
		independant = 0
		for n in range(nodesPerArm*3):
			
			nodeInArm = n%nodesPerArm
			sectionInArm = nodeInArm // nodesPerSection
			arm = n // nodesPerArm
			
			
			if( (sectionInArm % (self.NumSection-1)) == 0 ): # we're either on fixed section or rigid section
				
				if( sectionInArm == 0 ): # we're on fixed section
		
					
					table[2*n+0] = 0
					table[2*n+1] = arm*(self.nVertebra*(self.NumSection-2) + 1)*nodesPerSection + (n%nodesPerSection)
					
				else: # we're on a rigid section
					rigidSection = sectionInArm // (self.NumSection-1)
					table[2*n+0] = rigidSection
					table[2*n+1] = arm*nodesPerSection + (n%nodesPerSection)
					
			else: # we're on an independant section
				independant += 1
				#sectionInVertebra = sectionInArm % self.NumSection
				vertebraInArm = sectionInArm // (self.NumSection-1)
				#print sectionInArm - vertebraInArm
				table[2*n+0] = 0
				table[2*n+1] = arm*(self.nVertebra*(self.NumSection-2) + 1)*nodesPerSection + (sectionInArm - vertebraInArm)*nodesPerSection + (n%nodesPerSection)
				
				
		print('Indep section ' + str(independant/nodesPerSection))
		return table
					

	# called on each animation step
	def onBeginAnimationStep(self,dt):
		
		if self.ICRA_demo:
			self.currentTime += dt
			
			if 1 < self.currentTime <= 2 :
				self.forcefield.findData('force').value = transformTableInString([0, 0, -300000, 0, 0, 0])
				
			if 2 < self.currentTime <= 3 :
				self.forcefield.findData('force').value = transformTableInString([0, 300000, 0, 0, 0, 0])
				
			if 3 < self.currentTime <= 4 :
				self.forcefield.findData('force').value = transformTableInString([0, 0, 300000, 0, 0, 0, 0])
				
			if self.currentTime > 4 :
				self.forcefield.findData('force').value = transformTableInString([0, 0, 0, 0, 0, 0])
		
		return 0	
		