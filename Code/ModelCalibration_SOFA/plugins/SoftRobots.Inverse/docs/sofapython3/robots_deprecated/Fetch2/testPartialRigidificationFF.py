
import Sofa
import rigidification
from compiler.ast import flatten
import math

import os
path = os.path.dirname(os.path.abspath(__file__))+'/mesh_files/'
meshRobot=path+'actuator_mesh0_aligned.vtu'
meshIntervertebra=path+'rigid-intervertebra-oneside.stl'
meshSelect=path+'actuator_with_cut.stl'
meshCavity=path+'pneumatic_actuator_inner_aligned.stl'

print("")
print('\033[36m' + '\033[1m' + " [Informations about the scene]" + '\033[0m')
print(" (please refer to the README file for more informations)")
print("")

tr_x = 28*math.cos(2.0*math.pi/3.0)
tr_z = 28*math.sin(2.0*math.pi/3.0)




def createScene(rootNode):
    # Root node
    rootNode.findData('dt').value=1;
    rootNode.findData('gravity').value='0 0 0';
    rootNode.addObject('VisualStyle', displayFlags='showVisualModels showForceFields showInteractionForceFields showCollisionModels hideBoundingCollisionModels hideWireframe showBehaviorModels');

    #Required plugin
    rootNode.addObject('RequiredPlugin', pluginName='SoftRobots');

    #rootNode.addObject('FreeMotionAnimationLoop')
    #rootNode.addObject('QPInverseProblemSolver', printLog='1', epsilon='0.01')
    #rootNode.addObject('GenericConstraintSolver', printLog='1')

    #rootNode.addObject('DefaultPipeline', verbose='0')
    #rootNode.addObject('BruteForceBroadPhase')
    #rootNode.addObject('BVHNarrowPhase')
    #rootNode.addObject('DefaultContactManager', response='FrictionContactConstraint')
    #rootNode.addObject('LocalMinDistance', name="Proximity", alarmDistance='0', contactDistance='0')


    #rootNode.addObject('ClipPlane', normal='0 0 1')

    #goal
    goal = rootNode.addChild('goal')
    goal.findData('activated').value='1'
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



    #mergeMesh
    mergeMesh = rootNode.addChild('mergeMesh')
    #l1=mergeMesh.addObject('MeshVTKLoader', name="mesh", filename=meshRobot, translation="28 5 0")
    mergeMesh.addObject('RegularGridTopology', name='mesh', min='-10 0 -10', max='10 75 10', n='10 13 10')
    mergeMesh.init();
    meshHex= mergeMesh.addObject('MeshTopology', name="Merge", src='@mesh')
    
    #l2=mergeMesh.addObject('MeshVTKLoader', name="mesh2", filename=meshRobot, translation=str(tr_x)+' 5 '+ str(tr_z), rotation="0 120 0")
    #l3=mergeMesh.addObject('MeshVTKLoader', name="mesh3", filename=meshRobot, translation=str(tr_x)+' 5 '+ str(-tr_z), rotation="0 240 0")



    #mergeEngine=mergeMesh.addObject('MergeMeshes', name="Merge", nbMeshes="3", position1="@mesh1.position", hexahedra1="@mesh1.hexahedra",
    #                            position2="@mesh2.position", hexahedra2="@mesh2.hexahedra",
    #                            position3="@mesh3.position", hexahedra3="@mesh3.hexahedra")
    #mergeEngine.init();

                    
    boxFix= mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_fix',box='-60 -1 -60 60 5 60',drawBoxes='1', drawPoints='1', hexahedra="@Merge.hexahedra" , position="@Merge.position")
    boxIndep=mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_indep',box='-60 -6 -60 60 70 60',drawBoxes='1', drawPoints='0', hexahedra="@Merge.hexahedra" ,position="@Merge.position")
    boxFrame1= mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_frame1',box='-60 70.0000001 -60 60 76 60',drawBoxes='1', drawPoints='1', hexahedra="@Merge.hexahedra" ,position="@Merge.position")



    position = meshHex.findData('position').value;
    numPoints = len(position)
    print('numPoints '+ str(numPoints))
    print('position:')
    print(position)
    
    
    
    boxFrame1.init();
    IndicesFrame1= boxFrame1.findData('indices').value;
    IndicesFrame1 = flatten(IndicesFrame1);

    print('+++++++++++++++++++++++++++++++++++')
    print('IndicesFrame1' + str(IndicesFrame1))
    print('+++++++++++++++++++++++++++++++++++')

    boxIndep.init();
    freeNodes= boxIndep.findData('indices').value;
    freeNodes = flatten(freeNodes);

    rigidBlocks = [IndicesFrame1];

    #print(numPoints)
    #print '+++++++++++++++++++++++++++++++++++'
    print(rigidBlocks)
    #print '+++++++++++++++++++++++++++++++++++'
    print(freeNodes)
    #print '+++++++++++++++++++++++++++++++++++'

    indexPairs = rigidification.fillIndexPairs(numPoints,freeNodes,rigidBlocks)

    indexPairsStr = str(indexPairs)




    # composite model
    compositeNode = rootNode.addChild('CompositeModel')
    compositeNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='1', rayleighMass='0', firstOrder=False)
    compositeNode.addObject('SparseLDLSolver', name="ldlsolveur")

    #compositeNode.addObject('CGLinearSolver', iterations='50', tolerance="1e-5", threshold="1e-10")
    compositeNode.addObject('GenericConstraintCorrection', solverName='ldlsolveur')
    #compositeNode.addObject('PythonScriptController', filename="controller2.py", classname="controller")



    # ---------------------------------------------------------------------------------------------
    # ---------------------- Intervertebre rigide ----------------------------------
    # ---------------------------------------------------------------------------------------------
    interv1Node = compositeNode.addChild('Intervertebra1')
    interv1Node.addObject('MechanicalObject', template="Rigid3",name='interv1MO',position='0 80 0 0 0 0 1')
    #top_disc1Node.addObject('UniformMass',name='mass',totalMass='0.000001',showAxisSizeFactor='0.005')
    #interv1Node.addObject('PartialRigidificationConstraint')

    # ---------------------------------------------------------------------------------------------
    # ---------------------- Particules independantes ----------------------------------
    # ---------------------------------------------------------------------------------------------
    indep_particulesNode = compositeNode.addChild('Independant_Particules')
    indep_particulesNode.addObject('PointSetTopologyContainer', position='@../../mergeMesh/box_roi_indep.pointsInROI')
    IndependantParticles_dof=indep_particulesNode.addObject('MechanicalObject', template='Vec3', name='IndependantParticles_dof')
    indep_particulesNode.addObject('UniformMass',name='mass',totalMass='0.1')

    ### WARNING, same as above
    indep_particulesNode.addObject('BoxROI',name='box_roi',box='-60 -1 -60 60 5 60',drawBoxes='1', drawPoints='1')
    indep_particulesNode.addObject('RestShapeSpringsForceField', points='@box_roi.indices', stiffness='1e12')
    #indep_particulesNode.addObject('FixedConstraint', indices='@box_roi.indices')

    DeformableGridNode = indep_particulesNode.addChild('DeformableGrid')



    # ---------------------------------------------------------------------------------------------
    # ---------------------- Particules liees au rigide ----------------------
    # ---------------------------------------------------------------------------------------------
    Mapped_ParticuleNode = interv1Node.addChild('Mapped_Particule')
    Mapped_ParticuleNode.addObject('PointSetTopologyContainer', position='@../../../mergeMesh/box_roi_frame1.pointsInROI')
    Mapped_Particles_dof=Mapped_ParticuleNode.addObject('MechanicalObject', template='Vec3', name='Mapped_Particles_dof',  showIndices=False)
    Mapped_ParticuleNode.addObject('RigidMapping', name="rigidMap", input='@..',output='@.', globalToLocalCoords=True)


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Somme des particules et du rigide ----------------------
    # ---------------------------------------------------------------------------------------------

    Mapped_ParticuleNode.addChild(DeformableGridNode)
    DeformableGridNode.addObject('MeshTopology', src='@../../../../mergeMesh/Merge', name="mesh")
    DeformableGridNode.addObject('MechanicalObject',template='Vec3',name='mergeDofs')

    DeformableGridNode.addObject('HexahedronFEMForceField', name="tetraFF", youngModulus="1800", poissonRatio="0.3")


    deformableGrid_mappaddPointing = DeformableGridNode.addObject('SubsetMultiMapping',template='Vec3,Vec3d',name='deformableGrid_mapping', input='@../../../CompositeModel/Independant_Particules/IndependantParticles_dof @../../../CompositeModel/Intervertebra1/Mapped_Particule/Mapped_Particles_dof ', output='@./mergeDofs', indexPairs=indexPairsStr)




    compositeNode.addObject('MappedMatrixForceField', template='Vec3,Rigid', object1='@./Independant_Particules/IndependantParticles_dof', object2='@./Intervertebra1/interv1MO', mappedForceField='@./Independant_Particules/DeformableGrid/tetraFF' )




    # ---------------------- version 6D ----------------------
    #interv1Node.addObject('PositionEffector', template="Rigid3", indices="0", effectorGoal="@../../goal/goalMORigide.position")




    #mergeMesh.addObject('MeshVTKLoader', name="mesh2", filename=meshRobot, translation="1.5 0 -2.5")
    #mergeMesh.addObject('MeshVTKLoader', name="mesh3", filename=meshRobot, translation="-3 0 0")


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Visu (Intervertebra) ----------------------
    # ---------------------------------------------------------------------------------------------
    visuIntervertebra= interv1Node.addChild('visuIntervertebra')
    visuIntervertebra.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, translation="27 0 0",  rotation="0 180 0", scale='10')
    visuIntervertebra.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra.addObject('OglModel')
    visuIntervertebra.addObject('RigidMapping', name="rigidMapVisu", input='@..',output='@.')



    return rootNode
