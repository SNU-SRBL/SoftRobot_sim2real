

import Sofa
import math
import os
path = os.path.dirname(os.path.abspath(__file__))+'/mesh_files/'
meshRobot=path+'springy_robot_tetra_4000vert.vtu'
meshIntervertebra=path+'rigid-intervertebra-oneside.stl'
meshCavity=path+'pneumatic_actuator_inner_aligned.stl'
path2 = os.path.dirname(os.path.abspath(__file__))+'/'
complianceIntervertebraTXT = path2+'cIntervertebra3.txt'

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
    dt=0.1
    rootNode.findData('dt').value=dt;
    rootNode.findData('gravity').value='0 0 0';
    rootNode.addObject('VisualStyle', displayFlags='showVisualModels showForceFields showInteractionForceFields showCollisionModels hideBoundingCollisionModels hideWireframe');

    #Required plugin
    rootNode.addObject('RequiredPlugin', pluginName='SoftRobots');

    rootNode.addObject('FreeMotionAnimationLoop')
    rootNode.addObject('QPInverseProblemSolver', printLog='0', epsilon='0.00001')


    rootNode.addObject('DefaultPipeline', verbose='0')
    rootNode.addObject('BruteForceBroadPhase')
    rootNode.addObject('BVHNarrowPhase')
    rootNode.addObject('DefaultContactManager', response='FrictionContactConstraint')
    rootNode.addObject('LocalMinDistance', name="Proximity", alarmDistance='0', contactDistance='0')

    rootNode.addObject('PythonScriptController', classname="controller", filename="ArduinoInterface.py");
    rootNode.addObject('SerialPortBridgeGeneric', name="serial", port="/dev/ttyACM0", baudRate="115200", size="18", listening=True)

    #rootNode.addObject('ClipPlane', normal='0 0 1')

    #goal
    goal = rootNode.addChild('goal')
    goal.findData('activated').value='0'
    goal.addObject('EulerImplicitSolver', firstOrder=True)
    goal.addObject('CGLinearSolver', iterations='100', tolerance="1e-5", threshold="1e-10")
    goal.addObject('MechanicalObject', name='goalMORigide', template="Rigid3", position='0 80 0 0 0 0 1')
    goal.addObject('UniformMass',  totalMass='0.1')
    goal.addObject('UncoupledConstraintCorrection')
    goalPoints= goal.addChild('goalPoints')
    goalPoints.addObject('MechanicalObject', name='goalMO', template='Vec3', position='0 0 0 ')
    # 1 0 0  0 1 0  0 0 1
    goalPoints.addObject('SphereCollisionModel', radius='5', group='1')
    goalPoints.addObject('RigidMapping', name="rigidMap", input='@..',output='@.')

    #goal2
    goal2 = rootNode.addChild('goal2')
    goal2.findData('activated').value='1'
    goal2.addObject('EulerImplicitSolver', firstOrder=True)
    goal2.addObject('CGLinearSolver', iterations='100', tolerance="1e-5", threshold="1e-10")
    goal2.addObject('MechanicalObject', name='goalMORigide', template="Rigid3", position='0 240 0 0 0 0 1')
    goal2.addObject('UniformMass',  totalMass='0.1')
    goal2.addObject('UncoupledConstraintCorrection')
    goalPoints= goal2.addChild('goalPoints')
    goalPoints.addObject('MechanicalObject', name='goalMO', template='Vec3', position='0 0 0  10 0 0  0 10 0  0 0 10')
    # 1 0 0  0 1 0  0 0 1
    goalPoints.addObject('SphereCollisionModel', radius='3', group='1')
    goalPoints.addObject('RigidMapping', name="rigidMap", input='@..',output='@.')


    # ---------------------------------------------------------------------------------------------
    # ----------------------  Simplified version ----------------------
    # ---------------------------------------------------------------------------------------------
    compareNode = rootNode.addChild('complianceSection')
    compareNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0.3', rayleighMass='0.1', firstOrder=False)
    compareNode.addObject('SparseLDLSolver', name="precond")
    compareNode.addObject('MechanicalObject', name='SimplifiedMO', template="Rigid3", position='0 0 0 0 0 0 1 	0 80 0 0 0 0 1   0 160 0 0 0 0 1   0 240 0 0 0 0 1')
    compareNode.addObject('UniformMass',name='mass',totalMass='0.1',showAxisSizeFactor='0.005')
    compareNode.addObject('PREquivalentStiffnessForceField', complianceFile=complianceIntervertebraTXT)
    compareNode.addObject('GenericConstraintCorrection', solverName='precond')
    compareNode.addObject('FixedConstraint', name='fixed', indices='0')

    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cavity) ----------------------
    # ---------------------------------------------------------------------------------------------
    activateCavities=0;
    MappedCavity11Node=compareNode.addChild('MappedCavity11')
    MappedCavity11Node.findData('activated').value=str(activateCavities)
    MappedCavity11Node.addObject('MeshSTLLoader', name="loadCavity11", filename=meshCavity, translation='28 5 0')
    MappedCavity11Node.addObject('MeshTopology', src='@loadCavity11', name="cavityMesh")
    MappedCavity11Node.addObject('MechanicalObject',template='Vec3',name='cavity11Dofs')
    MappedCavity11Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity11Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity11Dofs", nbRef='2')

    MappedCavity12Node=compareNode.addChild('MappedCavity12')
    MappedCavity12Node.findData('activated').value=str(activateCavities)
    MappedCavity12Node.addObject('MeshSTLLoader', name="loadCavity12", filename=meshCavity, translation=str(tr_x)+' 5 '+ str(tr_z))
    MappedCavity12Node.addObject('MeshTopology', src='@loadCavity12', name="cavityMesh")
    MappedCavity12Node.addObject('MechanicalObject',template='Vec3',name='cavity12Dofs')
    MappedCavity12Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity12Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity12Dofs", nbRef='2')

    MappedCavity13Node=compareNode.addChild('MappedCavity13')
    MappedCavity13Node.findData('activated').value=str(activateCavities)
    MappedCavity13Node.addObject('MeshSTLLoader', name="loadCavity13", filename=meshCavity, translation=str(tr_x)+' 5 '+ str(-tr_z))
    MappedCavity13Node.addObject('MeshTopology', src='@loadCavity13', name="cavityMesh")
    MappedCavity13Node.addObject('MechanicalObject',template='Vec3',name='cavity13Dofs')
    MappedCavity13Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity13Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity13Dofs", nbRef='2')

    MappedCavity21Node=compareNode.addChild('MappedCavity21')
    MappedCavity21Node.findData('activated').value=str(activateCavities)
    MappedCavity21Node.addObject('MeshSTLLoader', name="loadCavity11", filename=meshCavity, translation='28 85 0')
    MappedCavity21Node.addObject('MeshTopology', src='@loadCavity11', name="cavityMesh")
    MappedCavity21Node.addObject('MechanicalObject',template='Vec3',name='cavity21Dofs')
    MappedCavity21Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity21Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity21Dofs", nbRef='2')

    MappedCavity22Node=compareNode.addChild('MappedCavity22')
    MappedCavity22Node.findData('activated').value=str(activateCavities)
    MappedCavity22Node.addObject('MeshSTLLoader', name="loadCavity22", filename=meshCavity, translation=str(tr_x)+' 85 '+ str(tr_z))
    MappedCavity22Node.addObject('MeshTopology', src='@loadCavity22', name="cavityMesh")
    MappedCavity22Node.addObject('MechanicalObject',template='Vec3',name='cavity22Dofs')
    MappedCavity22Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity22Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity22Dofs", nbRef='2')

    MappedCavity23Node=compareNode.addChild('MappedCavity23')
    MappedCavity23Node.findData('activated').value=str(activateCavities)
    MappedCavity23Node.addObject('MeshSTLLoader', name="loadCavity23", filename=meshCavity, translation=str(tr_x)+' 85 '+ str(-tr_z))
    MappedCavity23Node.addObject('MeshTopology', src='@loadCavity23', name="cavityMesh")
    MappedCavity23Node.addObject('MechanicalObject',template='Vec3',name='cavity23Dofs')
    MappedCavity23Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity23Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity23Dofs", nbRef='2')


    MappedCavity31Node=compareNode.addChild('MappedCavity31')

    MappedCavity31Node.findData('activated').value=str(activateCavities)
    MappedCavity31Node.addObject('MeshSTLLoader', name="loadCavity11", filename=meshCavity, translation='28 165 0')
    MappedCavity31Node.addObject('MeshTopology', src='@loadCavity11', name="cavityMesh")
    MappedCavity31Node.addObject('MechanicalObject',template='Vec3',name='cavity31Dofs')
    MappedCavity31Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity31Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity31Dofs", nbRef='2')

    MappedCavity32Node=compareNode.addChild('MappedCavity32')
    MappedCavity32Node.findData('activated').value=str(activateCavities)
    MappedCavity32Node.addObject('MeshSTLLoader', name="loadCavity32", filename=meshCavity, translation=str(tr_x)+' 165 '+ str(tr_z))
    MappedCavity32Node.addObject('MeshTopology', src='@loadCavity32', name="cavityMesh")
    MappedCavity32Node.addObject('MechanicalObject',template='Vec3',name='cavity32Dofs')
    MappedCavity32Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity32Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity32Dofs", nbRef='2')

    MappedCavity33Node=compareNode.addChild('MappedCavity33')
    MappedCavity33Node.findData('activated').value=str(activateCavities)
    MappedCavity33Node.addObject('MeshSTLLoader', name="loadCavity33", filename=meshCavity, translation=str(tr_x)+' 165 '+ str(-tr_z))
    MappedCavity33Node.addObject('MeshTopology', src='@loadCavity33', name="cavityMesh")
    MappedCavity33Node.addObject('MechanicalObject',template='Vec3',name='cavity33Dofs')
    MappedCavity33Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', maxPressure=str(dt*500), minPressure='0', visualization='1', maxVolumeGrowth='100000',  maxVolumeGrowthVariation='10000')
    MappedCavity33Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity33Dofs", nbRef='2')


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cables) ----------------------
    # ---------------------------------------------------------------------------------------------
    MappedCables = compareNode.addChild('cables')
    MappedCables.findData('activated').value='1'
    MappedCables.addObject('MechanicalObject', name="cablePoint", position= str(px1)+' 0 '+str(pz1)+ ' '+ str(px2)+' 0 '+str(pz2)+' '+str(px3)+' 0 '+str(pz3)+ ' '   + str(px1)+' 0 '+str(pz1)+ ' '+ str(px2)+' 0 '+str(pz2)+' '+str(px3)+' 0 '+str(pz3)+ ' '  + str(px1)+' 0 '+str(pz1)+ ' '+ str(px2)+' 0 '+str(pz2)+' '+str(px3)+' 0 '+str(pz3)+ ' ' )
    MappedCables.addObject('RigidMapping', rigidIndexPerPoint="1 1 1  2 2 2  3 3 3", name="rigidMapCablePoints", input='@..',output='@.')

    MappedCables.addObject('CableActuator', template="Vec3", name="c1" , indices="0", pullPoint=str(px1)+' 0 '+str(pz1) , maxPositiveDisp="10", maxNegativeDisp="10", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c2" , indices="1", pullPoint=str(px2)+' 0 '+str(pz2) , maxPositiveDisp="10", maxNegativeDisp="10", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c3" , indices="2", pullPoint=str(px3)+' 0 '+str(pz3) , maxPositiveDisp="10", maxNegativeDisp="10", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c4" , indices="0 3", pullPoint=str(px1)+' 0 '+str(pz1) , maxPositiveDisp="20", maxNegativeDisp="20", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c5" , indices="1 4", pullPoint=str(px2)+' 0 '+str(pz2) , maxPositiveDisp="20", maxNegativeDisp="20", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c6" , indices="2 5", pullPoint=str(px3)+' 0 '+str(pz3) , maxPositiveDisp="20", maxNegativeDisp="20", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c7" , indices="0 3 6", pullPoint=str(px1)+' 0 '+str(pz1) , maxPositiveDisp="30", maxNegativeDisp="30", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c8" , indices="1 4 7", pullPoint=str(px2)+' 0 '+str(pz2) , maxPositiveDisp="30", maxNegativeDisp="30", minForce='0')
    MappedCables.addObject('CableActuator', template="Vec3", name="c9" , indices="2 5 8", pullPoint=str(px3)+' 0 '+str(pz3) , maxPositiveDisp="30", maxNegativeDisp="30", minForce='0')


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (Effector) ----------------------
    # ---------------------------------------------------------------------------------------------
    # ---------------------- version 6D ----------------------
    #compareNode.addObject('PositionEffector', template="Rigid3", indices="1", effectorGoal="@../goal/goalMORigide.position", useDirections='1 1 1 0 0 0')
    compareNode.addObject('PositionEffector', template="Rigid3", indices="3", effectorGoal="@../goal2/goalMORigide.position", useDirections='1 1 1 1 0 1')


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Visu ----------------------
    # ---------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # ---------------------- Visu (Intervertebra) ----------------------
    # ---------------------------------------------------------------------------------------------
    visuIntervertebra1= compareNode.addChild('visuIntervertebra1')
    visuIntervertebra1.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, scale='9,6',translation="28 0 0",  rotation="0 180 0")
    visuIntervertebra1.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra1.addObject('OglModel')
    visuIntervertebra1.addObject('RigidMapping', name="rigidMapVisu", input='@..',output='@.', index='1')


    visuIntervertebra2= compareNode.addChild('visuIntervertebra2')
    visuIntervertebra2.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, scale='9,6',translation="28 0 0",  rotation="0 180 0")
    visuIntervertebra2.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra2.addObject('OglModel')
    visuIntervertebra2.addObject('RigidMapping', name="rigidMapVisu", input='@..',output='@.', index='2')


    visuIntervertebra3= compareNode.addChild('visuIntervertebra3')
    visuIntervertebra3.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, scale='9,6',translation="28 0 0",  rotation="0 180 0")
    visuIntervertebra3.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra3.addObject('OglModel')
    visuIntervertebra3.addObject('RigidMapping', name="rigidMapVisu", input='@..',output='@.', index='3')

    return rootNode
