
import Sofa
import math
import os
path = os.path.dirname(os.path.abspath(__file__))+'/mesh_files/'
meshRobot=path+'springy_robot_tetra_4000vert.vtu'
meshIntervertebra=path+'rigid-intervertebra-oneside.stl'
meshCavity=path+'pneumatic_actuator_inner_aligned.stl'
path2 = os.path.dirname(os.path.abspath(__file__))+'/'
complianceIntervertebraTXT = path2+'cIntervertebra.txt'

tr_x = 28*math.cos(2.0*math.pi/3.0)
tr_z = 28*math.sin(2.0*math.pi/3.0)

r_cable=31.5;
px1 = r_cable*math.cos(1.0*math.pi/3.0)
pz1 = r_cable*math.sin(1.0*math.pi/3.0)
px2 = r_cable*math.cos(3.0*math.pi/3.0)
pz2 = r_cable*math.sin(3.0*math.pi/3.0)
px3 = r_cable*math.cos(5.0*math.pi/3.0)
pz3 = r_cable*math.sin(5.0*math.pi/3.0)


def createScene(rootNode):
    # Root node
    rootNode.findData('dt').value=0.1;
    rootNode.findData('gravity').value='0 0 0';
    rootNode.addObject('VisualStyle', displayFlags='showVisualModels showForceFields showInteractionForceFields showCollisionModels hideBoundingCollisionModels hideWireframe');

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
    goal.findData('activated').value='1'
    goal.addObject('EulerImplicitSolver', firstOrder=True)
    goal.addObject('CGLinearSolver', iterations='100', tolerance="1e-5", threshold="1e-10")
    goal.addObject('MechanicalObject', name='goalMORigide', template="Rigid3", position='0 80 0 0 0 0 1')
    goal.addObject('UniformMass',  totalMass='0.1', showAxisSizeFactor='8')
    goal.addObject('UncoupledConstraintCorrection')
    goalPoints= goal.addChild('goalPoints')
    goalPoints.addObject('MechanicalObject', name='goalMO', template='Vec3', position='0 0 0 ')
    # 1 0 0  0 1 0  0 0 1
    goalPoints.addObject('SphereCollisionModel', radius='5', group='1')
    goalPoints.addObject('RigidMapping', name="rigidMap", input='@..',output='@.')




    # ---------------------------------------------------------------------------------------------
    # ----------------------  Simplified version ----------------------
    # ---------------------------------------------------------------------------------------------
    compareNode = rootNode.addChild('complianceSection')
    compareNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0.1', rayleighMass='0.1', firstOrder=False)
    compareNode.addObject('SparseLDLSolver', name="precond")
    compareNode.addObject('MechanicalObject', name='SimplifiedMO', template="Rigid3", position='0 0 0 0 0 0 1 	0 80 0 0 0 0 1')
    compareNode.addObject('UniformMass',name='mass',totalMass='0.1',showAxisSizeFactor='5')
    compareNode.addObject('PREquivalentStiffnessForceField', complianceFile=complianceIntervertebraTXT)
    compareNode.addObject('GenericConstraintCorrection', solverName='precond')
    compareNode.addObject('FixedConstraint', name='fixed', indices='0')

    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cavity) ----------------------
    # ---------------------------------------------------------------------------------------------
    MappedCavity11Node=compareNode.addChild('MappedCavity11')
    MappedCavity11Node.addObject('MeshSTLLoader', name="loadCavity11", filename=meshCavity, translation='28 5 0')
    MappedCavity11Node.addObject('MeshTopology', src='@loadCavity11', name="cavityMesh")
    MappedCavity11Node.addObject('MechanicalObject',template='Vec3',name='cavity11Dofs')
    # Cavity11Node.addObject('Triangle')
    MappedCavity11Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure='50', minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity11Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity11Dofs")

    MappedCavity12Node=compareNode.addChild('MappedCavity12')
    MappedCavity12Node.addObject('MeshSTLLoader', name="loadCavity12", filename=meshCavity, translation=str(tr_x)+' 5 '+ str(tr_z))
    MappedCavity12Node.addObject('MeshTopology', src='@loadCavity12', name="cavityMesh")
    MappedCavity12Node.addObject('MechanicalObject',template='Vec3',name='cavity12Dofs')
    # Cavity12Node.addObject('Triangle')
    MappedCavity12Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure='50', minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity12Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity12Dofs")

    MappedCavity13Node=compareNode.addChild('MappedCavity13')
    MappedCavity13Node.addObject('MeshSTLLoader', name="loadCavity13", filename=meshCavity, translation=str(tr_x)+' 5 '+ str(-tr_z))
    MappedCavity13Node.addObject('MeshTopology', src='@loadCavity13', name="cavityMesh")
    MappedCavity13Node.addObject('MechanicalObject',template='Vec3',name='cavity13Dofs')
    # Cavity13Node.addObject('Triangle')
    MappedCavity13Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure='50', minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity13Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity13Dofs")


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cables) ----------------------
    # ---------------------------------------------------------------------------------------------
    MappedCables = compareNode.addChild('cables')
    MappedCables.findData('activated').value='0'
    MappedCables.addObject('MechanicalObject', name="cablePoint", position= str(px1)+' 0 '+str(pz1)+ ' '+ str(px2)+' 0 '+str(pz2)+' '+str(px3)+' 0 '+str(pz3))
    MappedCables.addObject('RigidMapping', index="1", name="rigidMapCablePoints", input='@..',output='@.')

    MappedCables.addObject('CableActuator', template="Vec3", name="c1" , indices="0", pullPoint=str(px1)+' 0 '+str(pz1) , maxPositiveDisp="50", maxNegativeDisp="20")
    MappedCables.addObject('CableActuator', template="Vec3", name="c2" , indices="1", pullPoint=str(px2)+' 0 '+str(pz2) , maxPositiveDisp="50", maxNegativeDisp="20")
    MappedCables.addObject('CableActuator', template="Vec3", name="c3" , indices="2", pullPoint=str(px3)+' 0 '+str(pz3) , maxPositiveDisp="50", maxNegativeDisp="20")


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
    visuIntervertebra.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, scale='9,6',translation="28 0 0",  rotation="0 180 0")
    visuIntervertebra.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra.addObject('OglModel')
    visuIntervertebra.addObject('RigidMapping', name="rigidMapVisu", input='@..',output='@.', index='1')


    return rootNode
