import Sofa
import random
from math import*
from __future__ import division # for default floating point division

# utility methods

global degree
degree = 3

def evalBezier3(dim, cpOrig, nPts, rBegin, rEnd, offset):
	#print(list(range(0, len(cpOrig)-degree, 3*dim)))
	curve = []
	cp = [cpOrig[i] for i in range(len(cpOrig))]
	cp[dim-1] = cp[dim-1]*rBegin
	cp[2*dim-1] = cp[2*dim-1]*rBegin
	cp[-1] = cp[-1]*rEnd
	cp[-(dim+1)] = cp[-(dim+1)] * rEnd
	for points in range(0, len(cpOrig)-degree, 3*dim) :
		#print(list(range(span, span + 4*dim)))
		span = cp[points:points+4*dim]
		#print(cp)
		p0 = span[0:dim]
		p1 = span[dim:2*dim]
		p2 = span[2*dim:3*dim]
		p3 = span[3*dim:4*dim]
		print(p0, p1, p2, p3)
		#p0[2] = p0[2]*rBegin
		#p1[2] = p1[2]*rBegin
		
		for i in range(nPts) :
			t = i/(nPts-1)
			P = [0]*dim
			for d in range(dim):
				P[d] = ((1-t)**3)*p0[d] + (3*t*((1-t)**2))*p1[d] + 3*((1-t)*(t**2))*p2[d] + (t**3)*p3[d]

			P[0] = P[0] + offset
			curve = curve + P
				
		#p0 = cp[9:12]
		#p1 = cp[12:15]
		#p2 = cp[15:18]
		#p3 = cp[18:21]
		
		#p2[2] = p2[2]*rEnd
		#p3[2] = p3[2]*rEnd
		
		
		#for i in range(nPts) :
			#t = i/(nPts-1)
			#P = [0]*dim
			#for d in range(dim):
				#P[d] = ((1-t)**3)*p0[d] + (3*t*((1-t)**2))*p1[d] + 3*((1-t)*(t**2))*p2[d] + (t**3)*p3[d]

			
			#P[0] = P[0] + offset
			#curve = curve + P

		#for i in range(nPts) :
			#t = i/(nPts-1)
			#x = ((1-t)**3)*p0[0] + 3*(t*(1-t)**3)*p1[0] + 3*(t**2*(1-t))*p2[0] + t**3*p3[0]
			#y = ((1-t)**3)*p0[1] + 3*(t*(1-t)**3)*p1[1] + 3*(t**2*(1-t))*p2[1] + t**3*p3[1]
			#z = ((1-t)**3)*p0[2] + 3*(t*(1-t)**3)*p1[2] + 3*(t**2*(1-t))*p2[2] + t**3*p3[2]
			
			#curve = curve + [x, y, z]
		
	return curve


def genRadius(a, b, n):
	return [a+i*((b-a)/n) for i in range(n+1)]

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
	normSquare=0;
	for i in range(3):
		normSquare = normSquare+ v[i]*v[i]
	norm = sqrt(normSquare)
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
	
# create a copy of the topology 
def createCopyofListWithOffset( inputList, offset):
	#size of the mesh list
	s=len(inputList)
	#allocation of the memory
	ListCopy=[0]*s;
	
	for i in range(s):
		ListCopy[i]= inputList[i]+offset
	
	return ListCopy



# on definie la position de la base du cylindre
# on definie son axe
# a partir d'un "profil", on positionne les points du cylindre

def posGeneralizedCylinder(NumPointsOnSection,NumSection,posBase, Axis,posProfile):	

	posCylinder = [0]*3*NumPointsOnSection*NumSection;
	
	numPosProfile = len(posProfile)/3;
	
	if NumSection != numPosProfile:
		print 'problem: NumSection ' + str(NumSection) + ' is not equal to numPosProfile '+ str(NumPosProfile)
	
	
	
	# computation of the center and the radius of each section
	radiusSection = [0]*NumSection;
	CenterSection = [0]*3*NumSection;
	for s in range(NumSection):
		P0Ps=[0]*3;
		
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
		
		
		print pos 
		position[3*p] = pos[0];
		position[3*p+1] = pos[1];
		position[3*p+2] = pos[2];
		
		xglobal=xglobal+dx;
		
	return position 
		
		
	
	
	
def transformTablePosInString(Table):
	numPos = len(Table)/3;
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


def rotateTablePosAlongX(Table, angle):
	sizeT = len(Table)
	numP=sizeT/3;
	rotatedTable=[0]*numP*3;
	
	for p in range(numP):		
		#rotation
		rotatedTable[3*p] = Table[3*p] # no transformation along x
		rotatedTable[3*p+1] = Table[3*p+1]*cos(angle) + Table[3*p+2]*sin(angle)			
		rotatedTable[3*p+2] =-Table[3*p+1]*sin(angle) + Table[3*p+2]*cos(angle)			
		
		
	return rotatedTable
	

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
	



############## Scene with Multi-mapping
def createScene(rootNode):



	############### computation of the curve 
	inputNodes=[5.22898328467, 0.0, -13.032511746300001, 16.3310923107558, 0.0, -12.243573739894215, 4.341044058136216, -3.2255304605338943e-75, -30.595010387826871, 12.685578497833628, -3.2255304605338943e-75, -30.002031130482976, 21.03011293753104, -3.2255304605338943e-75, -29.409051873139081, 6.587468025912024, 3.0116826319738618e-192, -13.247009281715098, 17.689577051997823, 3.0116826319738618e-192, -12.458071275309312]
	numNodesCurve=7;
	N=7;
	posProfile=bezierLine(inputNodes, numNodesCurve, N);
	############### computation of the generalized cylinder surfaces
	NumPointsOnSection=12;
	NumSection=N;
	posBase=[5.191767153364891, 0.0, -39.538169209096495];
	Axis=[0.9974846191374479, 0, 0.070883246146185117];
	posTop = [0]*3;
	for i in range(3):
		posTop[i]= posBase[i] + 30*Axis[i]
	# first surface along the profile	
	posCylinder = posGeneralizedCylinder(NumPointsOnSection,NumSection,posBase, Axis,posProfile);
	strPosCylinder= transformTableInString(posCylinder);
	# computation of the first rotated surface
	angle = (2.0/3.0)* 3.141592653589793;
	posCylinderR1 = rotateTablePosAlongX(posCylinder, angle)
	strPosCylinder2=transformTablePosInString(posCylinderR1);
	
	# computation of the second rotated surface
	angle  = (4.0/3.0)* 3.141592653589793;
	posCylinderR2 = rotateTablePosAlongX(posCylinder, angle)
	strPosCylinder3=transformTablePosInString(posCylinderR2);
	
	
	
		
	#test = posCylinder + posCylinderR1
	strMergeSurfacePos = strPosCylinder+ ' ' + strPosCylinder2 + ' ' + strPosCylinder3

	
	## Creation of the topology of the original surface
 	QuadList=createCylinderSurfaceMesh(NumPointsOnSection,NumSection);
	strQuadList= transformTableInString(QuadList);
	
	# Creation of the topology of the first rotated surface 
	numNodes = NumPointsOnSection*NumSection;
	QuadList2 = createCopyofListWithOffset( QuadList, numNodes);
	strQuadList2= transformTableInString(QuadList2);
	
	# Creation of the topology of the second rotated surface
	QuadList3 = createCopyofListWithOffset( QuadList, 2*numNodes);
	strQuadList3= transformTableInString(QuadList3);
	
	strMergeSurfaceTopo = strQuadList+ ' ' + strQuadList2 + ' ' + strQuadList3
	
	
	
	############### Compute the indices of nodes on the vertebra
	numberOfSlices= 2
	strNumSlices= str(numberOfSlices)
	numSurfacePoint= NumPointsOnSection*NumSection;
	
	### R0
	
	buf=TableOfTheNFirstIndexAfterM( NumPointsOnSection, 0)
	i0_1 = MultiplyTableIndex(buf, numberOfSlices+1)
	
	buf=TableOfTheNFirstIndexAfterM( NumPointsOnSection, numSurfacePoint)
	i0_2 = MultiplyTableIndex(buf, numberOfSlices+1)
	
	buf=TableOfTheNFirstIndexAfterM( NumPointsOnSection, 2*numSurfacePoint)
	i0_3 = MultiplyTableIndex(buf, numberOfSlices+1)	
	
	strI0_1 = transformTableInString(i0_1);
	strI0_2 = transformTableInString(i0_2);
	strI0_3 = transformTableInString(i0_3);
	
	mergeR0= strI0_1 + ' ' + strI0_2 + ' ' +strI0_3
	
		
	### R1
	
	buf=TableOfTheNLastIndexBeforeM( NumPointsOnSection, numSurfacePoint)
	i1_1 = MultiplyTableIndex(buf, numberOfSlices+1)
	
	buf=TableOfTheNLastIndexBeforeM( NumPointsOnSection, 2*numSurfacePoint)
	i1_2 = MultiplyTableIndex(buf, numberOfSlices+1)
	
	buf=TableOfTheNLastIndexBeforeM( NumPointsOnSection, 3*numSurfacePoint)
	i1_3 = MultiplyTableIndex(buf, numberOfSlices+1)	

	strI1_1 = transformTableInString(i1_1);
	strI1_2 = transformTableInString(i1_2);
	strI1_3 = transformTableInString(i1_3);
	
	mergeR1= strI1_1 + ' ' + strI1_2 + ' ' +strI1_3
	
	
	
	
	
	
	
	############### CREATE SCENE 
	
	
	


	# scene global stuff
	rootNode.addObject('VisualStyle', displayFlags='showBehaviorModels hideCollisionModels hideMappings showForceFields')
	rootNode.findData('dt').value=0.01
	rootNode.findData('gravity').value = '0 0 0'

	#rootNode.addObject('FreeMotionAnimationLoop')
	#rootNode.addObject('GenericConstraintSolver')
	###### variables of the controller
	params = str(numNodesCurve) + ' ' + str(NumSection) + ' ' + str(NumPointsOnSection)+ ' ' + str(numberOfSlices)
	rootNode.addObject('PythonScriptController', filename="IntervertebraController.py", classname="IntervertebraController", variables=params)
	
	rootNode.addObject('FreeMotionAnimationLoop')
	rootNode.addObject('GenericConstraintSolver', name='constraintSolver', printLog='1')


	surfaceNode= rootNode.addChild('Surface')
	surfaceNode.addObject('QuadSetTopologyContainer', name='topo', position=strMergeSurfacePos, quads=strMergeSurfaceTopo)
	surfaceNode.addObject('OglModel',name='visu', src='@topo')
	test = surfaceNode.addObject('ExtrudeQuadsAndGenerateHexas', name='engine', template='Vec3', thicknessIn='1',  thicknessOut='1', numberOfSlices=strNumSlices, surfaceVertices='@topo.position', surfaceQuads='@topo.quads' )
	
	
	

	



	
	return rootNode

	


