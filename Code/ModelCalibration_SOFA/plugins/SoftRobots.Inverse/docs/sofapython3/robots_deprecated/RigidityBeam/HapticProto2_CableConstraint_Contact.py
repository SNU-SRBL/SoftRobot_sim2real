import Sofa
import random
from math import*
#from __future__ import division # for default floating point division

# utility methods

global Pi
Pi =3.141592;
global degree
degree = 3



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

def rotate(q,v_in):
    v_out = [((1 - 2 * (q[1] *q[1] +q[2] *q[2]))*v_in[0] + (2 * (q[0] *q[1] -q[2] *q[3])) * v_in[1] + (2 * (q[2] *q[0] +q[1] *q[3])) * v_in[2]),
             ((2 * (q[0] *q[1] +q[2] *q[3]))*v_in[0] + (1 - 2 * (q[2] *q[2] +q[0] *q[0]))*v_in[1] + (2 * (q[1] *q[2] -q[0] *q[3]))*v_in[2]),
             ((2 * (q[2] *q[0] -q[1] *q[3]))*v_in[0] + (2 * (q[1] *q[2] +q[0] *q[3]))*v_in[1] + (1 - 2 * (q[1] *q[1] +q[0] *q[0]))*v_in[2])];
    return v_out


# definition of indexPairs for  SubsetMultiMapping
def fillIndexPairs(index1, index2, numPoints):
    max1 = len(index1)
    max2 = len(index2)
    
    k1=0; # compteur sur les points  de index1
    k2=0; # compteur sur les points  de index2
    l=0; # compteur sur les points de ni index1 ni index2
    indexPairs=[1,1]*(numPoints)
    for i in range(numPoints): # passe sur l'ensemble des points
        # print [i,j]
        if k1<max1 and index1[k1][0]==i :
            indexPairs[2*i  ]=1;
            indexPairs[2*i+1]=k1;
            k1=k1+1;
        elif k2<max2 and index2[k2][0]==i :
            indexPairs[2*i  ]=2;
            indexPairs[2*i+1]=k2;
            k2=k2+1;
        else :
            indexPairs[2*i  ]=0;
            indexPairs[2*i+1]=l;
            l=l+1;

    return indexPairs


# definition of indexPairs for  SubsetMultiMapping
def fillIndicesPairs(ListsIndices, ListsRefObject, numPoints):
    
    numIndicesList= len(ListsIndices)
    numRefObject = len(ListsRefObject)
    
    if numRefObject!=numIndicesList+1:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("error in fillIndicesPairs")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    
    # numRefObject must be equal to numIndicesList + 1
    # ListsRefObject[0] => default
    # ListsRefObject[i+1] => reference frame for ListsIndices[i]
    
    
    max =[0]*numIndicesList
    k = [0]*numIndicesList  # compteur sur les points  de index[j]
    
    for j in range(numIndicesList):
        max[j] = len(ListsIndices[j])
    
    l=0; # compteur sur les points de ni index1 ni index2
    indexPairs=[1,1]*(numPoints)
    for i in range(numPoints): # passe sur l'ensemble des points
        
        indexPairs[2*i] =ListsRefObject[0]; # by default it attached to ListsRefObject[0]
        indexPairs[2*i+1]=l;
        l=l+1;
        for j in range(numIndicesList):
            if k[j]<max[j] and ListsIndices[j][k[j]][0]==i:
                indexPairs[2*i  ]=ListsRefObject[j+1];
                indexPairs[2*i+1]=k[j];
                k[j]=k[j]+1;
                l=l-1; # in this case the object is not attached to 0 but to j
                break;

    return indexPairs


# on suppose que inputVolumePoint contient une serie de points 3d (x,y,z)
# qui represente un volume dans l'axe x
# on va "mapper" ce volume le long de la serie de courbes de bezier
# on suppose que x=[0 1] appartient a la premiere courbe, x=[1 2] a la deuxieme etc...
# inputVolumePoint est un double tableau (compatible avec sorties de sofa)


def bezierVolume(inputControlPoint, inputVolumePoint ):
    numControlPoints=len(inputControlPoint)/3; #nbre points de controle Bezier	   61
    numLines = (numControlPoints-1)/3; #nbre de lignes/courbes de bezier      20
    
    numVolumePoints=len(inputVolumePoint) #nbre pts du volume                765
    
    outputPosition = [0]*3*numVolumePoints
    
    for p in range(numVolumePoints):
        
        inPos=inputVolumePoint[p]
        line = int(100*inPos[0]-1.0e-8) # what is the segment
        x = 100*inPos[0] - float(line); # x is between 0 and 1
       
    
        pos = [ (1-x)*(1-x)*(1-x)*inputControlPoint[9*line] + 3*x*(1-x)*(1-x)*inputControlPoint[9*line+3] +  3*x*x*(1-x)*inputControlPoint[9*line+6] + x*x*x*inputControlPoint[9*line+9],
           (1-x)*(1-x)*(1-x)*inputControlPoint[9*line+1] + 3*x*(1-x)*(1-x)*inputControlPoint[9*line+4] +  3*x*x*(1-x)*inputControlPoint[9*line+7] + x*x*x*inputControlPoint[9*line+10],
           (1-x)*(1-x)*(1-x)*inputControlPoint[9*line+2] + 3*x*(1-x)*(1-x)*inputControlPoint[9*line+5] +  3*x*x*(1-x)*inputControlPoint[9*line+8] + x*x*x*inputControlPoint[9*line+11]]

        Dpos = [ -3*(1-x)*(1-x)*inputControlPoint[9*line] + (3-12*x+9*x*x)*inputControlPoint[9*line+3] +  (6*x-9*x*x)*inputControlPoint[9*line+6] + (3*x*x)*inputControlPoint[9*line+9],
               -3*(1-x)*(1-x)*inputControlPoint[9*line+1] + (3-12*x+9*x*x)*inputControlPoint[9*line+4] +  (6*x-9*x*x)*inputControlPoint[9*line+7] + (3*x*x)*inputControlPoint[9*line+10],
               -3*(1-x)*(1-x)*inputControlPoint[9*line+2] + (3-12*x+9*x*x)*inputControlPoint[9*line+5] +  (6*x-9*x*x)*inputControlPoint[9*line+8] + (3*x*x)*inputControlPoint[9*line+11]]

        x_dir = normalize(Dpos);
        if x_dir[0]>0:
            theta=asin(x_dir[1]);
        else:
            theta=3.14-asin(x_dir[1])
        
        outputPosition[3*p  ]= pos[0] - inPos[1]*sin(theta);
        outputPosition[3*p+1]= pos[1] + inPos[1]*cos(theta) ;
        outputPosition[3*p+2]= inPos[2] ;
    
    return outputPosition


#	on definie des courbes de bezier de degre 3

def bezierLine(inputControlPoint, N):

    numNodes=len(inputControlPoint)/3;
    numLines = (numNodes-1)/3;
    dx=(numLines+0.0)/(N-1);
    position = [0]*3*N
    # on passe sur les differents point
    xglobal=0;
    line=0;
    for p in range(N):
        while xglobal>line+1:
            line=line+1;
                
        if line > numLines-1:
            line = line-1;
        
        x = xglobal-line;
                
                # N0.x = inputControlPoint[9*line]
                # N0.y = inputControlPoint[9*line+1]
                # N0.z = inputControlPoint[9*line+2]
                
                # N1.x = inputControlPoint[9*line+3]
                # N1.y = inputControlPoint[9*line+4]
                # N1.z = inputControlPoint[9*line+5]
                
                # N2.x = inputControlPoint[9*line+6]
                # N2.y = inputControlPoint[9*line+7]
                # N2.z = inputControlPoint[9*line+8]
                
                # N3.x = inputControlPoint[9*line+9]
                # N3.y = inputControlPoint[9*line+10]
                # N3.z = inputControlPoint[9*line+11]
                
                
        pos = [ (1-x)*(1-x)*(1-x)*inputControlPoint[9*line] + 3*x*(1-x)*(1-x)*inputControlPoint[9*line+3] +  3*x*x*(1-x)*inputControlPoint[9*line+6] + x*x*x*inputControlPoint[9*line+9],
                (1-x)*(1-x)*(1-x)*inputControlPoint[9*line+1] + 3*x*(1-x)*(1-x)*inputControlPoint[9*line+4] +  3*x*x*(1-x)*inputControlPoint[9*line+7] + x*x*x*inputControlPoint[9*line+10],
                (1-x)*(1-x)*(1-x)*inputControlPoint[9*line+2] + 3*x*(1-x)*(1-x)*inputControlPoint[9*line+5] +  3*x*x*(1-x)*inputControlPoint[9*line+8] + x*x*x*inputControlPoint[9*line+11]]
       
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

def transformDoubleTableInSimpleTable(Table):
    size0 =  len(Table);

    # count the size
    size=0;
    for i in range(size0):
        size = size+len(Table[i]);
    
    TableOut=[0]*size;
    s=0;
    for i in range(size0):
        for j in range(len(Table[i])):
            TableOut[s] = Table[i][j];
            s=s+1;
        
    return TableOut

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

def transformTablePos(Table, translation, quat):
    sizeT = len(Table)
    numP=sizeT/3;
    rotatedTable=[0]*numP*3;
        
    for p in range(numP):
        #rotation
        v = [Table[3*p], Table[3*p+1],Table[3*p+2]];
        
        vout = rotate(quat,v);
        #tranlation
        v = plus(vout,translation);
        
        for i in range(3):
            rotatedTable[3*p+i] = v[i];
        
    return rotatedTable

def transformPointInRoi(PointInRoi, translation, quat):
    PosIndep= transformDoubleTableInSimpleTable(PointInRoi);
    NewPosIndep = transformTablePos(PosIndep, translation, quat);
    NewPosIndepStr =transformTableInString(NewPosIndep);
    return NewPosIndepStr


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
    #numFrames=9
    numFrames=21

    
    #theta = [Pi/2, Pi/2, 0, 0, 0, 0, 0, -Pi/2 , -Pi/2];
    #theta = [Pi/2, Pi/2, Pi/2, Pi/2, Pi/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -Pi/2 , -Pi/2, -Pi/2 , -Pi/2, -Pi/2, -Pi/2];
    theta = [Pi/2, Pi/2, Pi/2, Pi/2, Pi/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -Pi/2 , -Pi/2, -Pi/2 , -Pi/2, -Pi/2];
    #dx = [0, 1.2,   0.8, 0.8,    1.0, 0,    1.0, 0,    1.0, 0,    1.0, 0,    0.8, -0.8,   0, -1.2 ];
    #dx = [ 0, 1.2,   0, 1.2,   0, 1.2,  0, 1.2,  0.8, 0.8,   1.05, 0,    1.05, 0,    1.05, 0,    1.05, 0,    1.05, 0,    
          #1.05, 0,    1.05, 0,    1.05, 0,    1.05, 0,    1.05, 0,    0.8, -0.8,    0, -1.2,    0, -1.2,    0, -1.2,    0, -1.2,];
    dx = [ 0, 0.012,   0, 0.012,   0, 0.012,  0, 0.012,  0.008, 0.008,   0.0105, 0,    0.0105, 0,    0.0105, 0,    0.0105, 0,    0.0105, 0,    
          0.0105, 0,    0.0105, 0,    0.0105, 0,    0.0105, 0,    0.0105, 0,    0.008, -0.008,    0, -0.012,    0, -0.012,    0, -0.012,    0, -0.012,];
    #epaisseur1=0.1
    #epaisseur2=0.5
    epaisseur1=0.0025
    epaisseur2=0.00975
    
    Frame =[0]*7*numFrames #init array Frame with 7*numFrames zeros
    #Frame[6]=1; #useless because of reassignation ?
    
    Frame[0]=0;
    #Frame[5]=sin(Pi/4.0)
    #Frame[6]=cos(Pi/4.0)
    
    numInterFrame=numFrames-1
    ControlPoint=[0]*3*(3*numInterFrame+1)
    
    for p in range(3):
        ControlPoint[p] = Frame[p];    
    
    for f in range(numInterFrame):
        Frame[7*f+7 ]=Frame[7*f  ]+dx[2*f];
        Frame[7*f+8 ]=Frame[7*f+1]+dx[2*f+1];
        #Frame[7*f+9 ]= 0.0; # no Z for the moment...
        #Frame[7*f+10]= 0.0; # qx
        #Frame[7*f+11]= 0.0; # qy
        #Frame[7*f+12]= -sin((theta[f+1])/2.0); # qz
        #Frame[7*f+13]= cos((theta[f+1])/2.0); # qw
    
        l = norm([dx[2*f],dx[2*f+1],0.0])/3.0;
        #second control point
        ControlPoint[9*f+3] = Frame[7*f  ] + l * cos((theta[f]));# x
        ControlPoint[9*f+4] = Frame[7*f+1] + l * sin((theta[f]));# y
        ControlPoint[9*f+5] =0;  # z
    
        #third control point
        ControlPoint[9*f+6] = Frame[7*f+7] - l * cos((theta[f+1]));# x
        ControlPoint[9*f+7] = Frame[7*f+8] - l * sin((theta[f+1]));# y
        ControlPoint[9*f+8] =0;  # z

        #third control point
        ControlPoint[9*f+9 ] = Frame[7*f+7] ;# x
        ControlPoint[9*f+10] = Frame[7*f+8] ;# y
        ControlPoint[9*f+11] =0;  # z


    FrameStr=transformTableInString(Frame)


    posProfile = bezierLine(ControlPoint, 100)


    ControlPointStr = transformTableInString(posProfile)
    print('aaaaaaaaaaaa')
    print(FrameStr)
    print('zzzzzzzzzzzz')
    print(ControlPointStr)
    ############### CREATE SCENE
	# scene global stuff
    rootNode.addObject('VisualStyle', displayFlags='showBehaviorModels showCollisionModels hideMappings showForceFields showInteractionForceFields')
    rootNode.findData('dt').value=0.01
    rootNode.findData('gravity').value = '0 -9.81 0'
    #rootNode.addObject('PythonScriptController', filename="CylinderStiffnessController.py", classname="controller")
    rootNode.addObject('FreeMotionMasterSolver')
    # rootNode.addObject('QPInverseProblemSolver', name="QP", printLog="1")
    rootNode.addObject('GenericConstraintSolver')
    rootNode.addObject('DefaultPipeline', verbose="0")
    rootNode.addObject('BruteForceBroadPhase')
    rootNode.addObject('BVHNarrowPhase')
    rootNode.addObject('DefaultContactManager', response="FrictionContactConstraint")
    rootNode.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.003", contactDistance="0.0005")

    # ---------------------------------------------------------------------------------------------
    # ---------------------- Topology  ----------------------------------
    # ---------------------------------------------------------------------------------------------
    # GoalNode = rootNode.addChild('goal')
    # GoalNode.addObject('EulerImplicitSolver', firstOrder=True)
    # GoalNode.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")      
    # GoalNode.addObject('MechanicalObject', name="goalMO", position="0.0605 0.05 0.0")
    # GoalNode.addObject('SphereCollisionModel', radius="0.008", group="3")
    # GoalNode.addObject('UncoupledConstraintCorrection')
    
    # GoalNode.addObject('BoxROI', name="boxOnlyY", box="0.05 0.05 -0.01 0.07 0.07 0.01", drawBoxes=False)
    # GoalNode.addObject('PartialFixedConstraint', indices="@boxOnlyY.indices", fixedDirections="1 0 1")

    TopologyNode = rootNode.addChild('Topology')
    
    #TopologyNode.addObject('EulerSolver')
    TopologyNode.addObject('EulerImplicitSolver',name='eulerImpl',printLog=False, rayleighStiffness='0.1', rayleighMass='0', firstOrder=False)
    #TopologyNode.addObject('CGLinearSolver', name='linear_solver', iterations='500', tolerance='1.0e-18', threshold='1.0e-30')
    
    
    TopologyNode.addObject('ShewchukPCGLinearSolver',iterations="10", name="linearsolver", tolerance="1e-5", preconditioners="preconditioner", use_precond=True, update_step="1")
    
    

    test=TopologyNode.addObject('RegularGrid', name="grid", n="51 3 5", min="0 " +str(-epaisseur1)+ " "+str(-epaisseur2), max= str((numFrames-1)/100.0)+" "+str(epaisseur1)+ " "+str(epaisseur2))
    test.init();
    posTest= test.findData('position').value
    
    
    # ---------------------------------------------------------------------------------------------
    # ---------------------- topology of the deformable beam ----------------------------------
    # ---------------------------------------------------------------------------------------------
    NewPos = bezierVolume(ControlPoint,posTest)
    NewPosStr = transformTableInString(NewPos);
    NewPosRestStr =transformTableInString(transformDoubleTableInSimpleTable(posTest))
    
    MO=TopologyNode.addObject('MechanicalObject', template='Vec3', name='topo_dof', position=NewPosStr, rest_position=NewPosRestStr, showIndices='1', showIndicesScale='0.00001')
    MO.init()
    
    # J'ai repris la total Mass
    TopologyNode.addObject('UniformMass', totalMass="0.0205")    
    
    # BOX pour trouver hexa a rigidifier
    box= TopologyNode.addObject('BoxROI',name='box', box='-0.01 -0.001 -0.03    0.01 0.02 0.03          0.11 -0.001 -0.03    0.13 0.02 0.03    ', position=NewPosStr,drawBoxes='1', computeEdges='0', computeTriangles='0', computeTetrahedra='0', computeHexahedra='1', computeQuad='0')
    box.init()
    #16.2cm en dehors des pinces
    

    
    # rigid Hexahedrons:
    RigidHexaNode = TopologyNode.addChild('Rigid')
    RigidHexaNode.addObject('HexahedronSetTopologyContainer', name="rigidTopo_L", hexahedra="@../box.hexahedraInROI")
    RigidHexaNode.addObject('HexahedronFEMForceField', youngModulus="15000000", poissonRatio="0.3")
    
    fix = RigidHexaNode.addObject('PartialFixedConstraint', indices="@../box.indices",fixedDirections="1 0 1")
    

    TopologyNode.addObject('HexahedronFEMForceField', youngModulus='129000', poissonRatio='0.45')


    
    TopologyNode.addObject('SparseLDLSolver', name="preconditioner")
    
    TopologyNode.addObject('LinearSolverConstraintCorrection', solverName="preconditioner")
    
    
    TopologyNode.addObject('CylinderForceField', name="cyl1", stiffness="1000", damping="10", center="0.0105 0.0455 -0.02", radius="0.008", axis="0 0 0.04", indices="8 9 10 11 12 13 14 15      161 162 163 164 165 166 167 168      314 315 316 317 318 319 320 321      467 468 469 470 471 472 473 474     620 621 622 623 624 625 626 627", dir="-1 1 0", angle=" 0.78539816", delta="0.2", draw="1")
    TopologyNode.addObject('CylinderForceField', name="cyl2", stiffness="1000", damping="10", center="0.1105 0.0455 -0.02", radius="0.008", axis="0 0 0.04", indices="35 36 37 38 39 40 41 42      188 189 190 191 192 193 194 195      341 342 343 344 345 346 347 348      494 495 496 497 498 499 500 501     647 648 649 650 651 652 653 654",  dir="1 1 0", angle=" 0.78539816", delta="0.2", draw="1")
    TopologyNode.addObject('PythonScriptController', filename="CylinderStiffnessController.py", classname="controller")



    ControlNode = TopologyNode.addChild('Control')
    ControlNode.addObject('MechanicalObject', name="actuatedPoints", template="Vec3", position="0.10 0.0025 0  0.01 0 0   0.19 0.0 0     0.10 0.0015 0" )
    #ControlNode.addObject('MechanicalObject', name="actuatedPoints", template="Vec3", position="0 -2.8 0  0.09 -2.8 0   -0.09 -2.8 0     0 -2.8 0" )
    # ControlNode.addObject('InteractiveControl', name="DCMotors", address="169.254.8.220", port="1994", motorIndex="1", mode="3", baudRate="115200", 
    #                    printCableDisplacement="0", printLog="0",  entrees="@../../QP.delta")
    # ControlNode.addObject('PositionEffector', indices="0", axis='1 1 0', effectorGoal="@../../goal/goalMO.position", incrementEncoder="@DCMotors.deltaEncoder")
    # ControlNode.addObject('CableActuator', name="cable0", indices="1", pullPoint="0 -0.05 0", maxPositiveDisp="0.04", maxForce="0.05", minForce="0")
    # ControlNode.addObject('CableActuator', name="cable1", indices="2", pullPoint="0.121 -0.05 0", maxPositiveDisp="0.04", maxForce="0.05", minForce="0")
    ControlNode.addObject('CableConstraint', name="cable0", indices="1", pullPoint="0 -0.05 0", valueType="force", value='0.09')
    ControlNode.addObject('CableConstraint', name="cable1", indices="2", pullPoint="0.121 -0.05 0", valueType="force", value='0.09')
    # ControlNode.addObject('ForcePointActuator', name="doigt", indices="3", force="-0.005", direction="0 1 0")
    ControlNode.addObject('BarycentricMapping', mapForces=True, mapMasses=False)

    rootNode.addObject('OglGrid', size='10', nbSubdiv="1000")
        

    return rootNode


	


