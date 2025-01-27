 
import Sofa

import os
path = os.path.dirname(os.path.abspath(__file__))+'/robot_challenge/'
meshRobot=path+'springy_robot_tetra_4000vert.vtu'
meshIntervertebra=path+'rigid-intervertebra-oneside.stl'
meshSelect=path+'BiggerSelect.stl'
path2 = os.path.dirname(os.path.abspath(__file__))+'/'
complianceIntervertebraTXT = path2+'cIntervertebra.txt'

print("")
print('033[36m' + '033[1m' + " [Informations about the scene]" + '033[0m')
print(" (please refer to the README file for more informations)")
print("")

# utility methods

def fillIndexPairs(indexIn, numPoints):
    max = len(indexIn)

    j=0;
    k=0;
    l=0;
    indexPairs=[1,1]*(numPoints)
    for i in range(numPoints):
        # print [i,j]
        if j<max:
            if  indexIn[j][0]==i :
                indexPairs[2*i  ]=1;
                indexPairs[2*i+1]=k;
                j=j+1;
                k=k+1;
            else :
                indexPairs[2*i  ]=0;
                indexPairs[2*i+1]=l;
                l=l+1;
        else :
            indexPairs[2*i  ]=0;
            indexPairs[2*i+1]=l;
            l=l+1;

    return indexPairs




def createScene(rootNode):
    # Root node
    rootNode.findData('dt').value=0.01;
    rootNode.findData('gravity').value='0 0 0';
    rootNode.addObject('VisualStyle', displayFlags='showVisualModels showForceFields showInteractionForceFields hideCollisionModels hideBoundingCollisionModels hideWireframe');

    #Required plugin
    rootNode.addObject('RequiredPlugin', pluginName='SoftRobots');

    rootNode.addObject('FreeMotionAnimationLoop')
    rootNode.addObject('QPInverseProblemSolver', printLog='1', epsilon='0.01')
    
    
    rootNode.addObject('DefaultPipeline', verbose='0')
    rootNode.addObject('BruteForceBroadPhase')
    rootNode.addObject('BVHNarrowPhase')
    rootNode.addObject('DefaultContactManager', response='FrictionContactConstraint')
    rootNode.addObject('LocalMinDistance', name="Proximity", alarmDistance='0', contactDistance='0')

                
    #rootNode.addObject('ClipPlane', normal='0 0 1')
                
    #goal
    goal = rootNode.addChild('goal')
    goal.addObject('EulerImplicitSolver', firstOrder=True)
    goal.addObject('CGLinearSolver', iterations='100', tolerance="1e-5", threshold="1e-10")
    goal.addObject('MechanicalObject', name='goalMORigide', template="Rigid3", position='0 5.5 0 0 0 0 1')
    goal.addObject('UniformMass',  totalMass='0.1')
    goal.addObject('UncoupledConstraintCorrection')
    goalPoints= goal.addChild('goalPoints')
    goalPoints.addObject('MechanicalObject', name='goalMO', template='Vec3', position='0 0 0  1 0 0  0 1 0  0 0 1')
    goalPoints.addObject('SphereCollisionModel', radius='0.2', group='1')
    goalPoints.addObject('RigidMapping', name="rigidMap", input='@..',output='@.')


  
    
    # ---------------------------------------------------------------------------------------------
    # ----------------------  Simplified version ----------------------
    # ---------------------------------------------------------------------------------------------
    compareNode = rootNode.addChild('complianceCylinder')
    compareNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='10.0', rayleighMass='0.1', firstOrder=False)
    compareNode.addObject('SparseLDLSolver', name="precond")
    compareNode.addObject('MechanicalObject', name='SimplifiedMO', template="Rigid3", position='0 0 0 0 0 0 1 	0 5 0 0 0 0 1')
    compareNode.addObject('UniformMass',name='mass',totalMass='0.1',showAxisSizeFactor='0.005')
    compareNode.addObject('PREquivalentStiffnessForceField', complianceFile=complianceIntervertebraTXT)
    compareNode.addObject('GenericConstraintCorrection', solverName='precond')
    compareNode.addObject('FixedConstraint', name='fixed', indices='0')
    
    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cavity) ----------------------
    # ---------------------------------------------------------------------------------------------
    MappedCavity11Node=compareNode.addChild('MappedCavity11')
    MappedCavity11Node.addObject('MeshSTLLoader', name="loadCavity11", filename=meshSelect, translation="1.5 0 2.5")
    MappedCavity11Node.addObject('MeshTopology', src='@loadCavity11', name="cavityMesh")
    MappedCavity11Node.addObject('MechanicalObject',template='Vec3',name='cavity11Dofs')
    # Cavity11Node.addObject('Triangle')
    MappedCavity11Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure='10', minPressure='0', visualization='1', showVisuScale='0.0002')
    MappedCavity11Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity11Dofs")

    MappedCavity12Node=compareNode.addChild('MappedCavity12')
    MappedCavity12Node.addObject('MeshSTLLoader', name="loadCavity12", filename=meshSelect, translation="1.5 0 -2.5",  rotation="0 120 0")
    MappedCavity12Node.addObject('MeshTopology', src='@loadCavity12', name="cavityMesh")
    MappedCavity12Node.addObject('MechanicalObject',template='Vec3',name='cavity12Dofs')
    # Cavity12Node.addObject('Triangle')
    MappedCavity12Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure='10', minPressure='0', visualization='1', showVisuScale='0.0002')
    MappedCavity12Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity12Dofs")
    
    MappedCavity13Node=compareNode.addChild('MappedCavity13')
    MappedCavity13Node.addObject('MeshSTLLoader', name="loadCavity13", filename=meshSelect, translation="-3 0 0",  rotation="0 240 0")
    MappedCavity13Node.addObject('MeshTopology', src='@loadCavity13', name="cavityMesh")
    MappedCavity13Node.addObject('MechanicalObject',template='Vec3',name='cavity13Dofs')
    # Cavity13Node.addObject('Triangle')
    MappedCavity13Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure='10', minPressure='0', visualization='1', showVisuScale='0.0002')
    MappedCavity13Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity13Dofs")
    
    
    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cables) ----------------------
    # ---------------------------------------------------------------------------------------------
    MappedCables = compareNode.addChild('cables')
    MappedCables.addObject('MechanicalObject', name="cablePoint", position="3 0 0  -1.5 0 2.5  -1.5 0 -2.5")
    MappedCables.addObject('RigidMapping', index="1", name="rigidMapCablePoints", input='@..',output='@.')

    MappedCables.addObject('CableActuator', template="Vec3", name="c1" , indices="0", pullPoint="3 0 0" , maxPositiveDisp="5", maxNegativeDisp="0")
    MappedCables.addObject('CableActuator', template="Vec3", name="c2" , indices="1", pullPoint="-1.5 0 2.5" , maxPositiveDisp="5", maxNegativeDisp="0")
    MappedCables.addObject('CableActuator', template="Vec3", name="c3" , indices="2", pullPoint="-1.5 0 -2.5" , maxPositiveDisp="5", maxNegativeDisp="0")


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (Effector) ----------------------
    # ---------------------------------------------------------------------------------------------
    # ---------------------- version 6D ----------------------
    compareNode.addObject('PositionEffector', template="Rigid3", indices="1", effectorGoal="@../goal/goalMORigide.position", useDirections='1 1 1 1 0 1')
    
    
    # ---------------------------------------------------------------------------------------------
    # ---------------------- Visu ----------------------
    # ---------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # ---------------------- Visu (Intervertebra) ----------------------
    # ---------------------------------------------------------------------------------------------
    visuIntervertebra= compareNode.addChild('visuIntervertebra')
    visuIntervertebra.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, translation="-3 0 0",  rotation="0 0 0")
    visuIntervertebra.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra.addObject('OglModel')
    visuIntervertebra.addObject('RigidMapping', index="1", name="rigidMapVisu", input='@..',output='@.')
    
    
    return rootNode

