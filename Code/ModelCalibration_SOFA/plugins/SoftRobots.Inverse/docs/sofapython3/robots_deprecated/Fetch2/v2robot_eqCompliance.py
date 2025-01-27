 
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
    rootNode.addObject('VisualStyle', displayFlags='showVisualModels showForceFields showInteractionForceFields hideCollisionModels hideBoundingCollisionModels hideWireframe');

    #Required plugin
    rootNode.addObject('RequiredPlugin', pluginName='SoftRobots');

    rootNode.addObject('FreeMotionAnimationLoop')
    rootNode.addObject('GenericConstraintSolver', printLog='1')
    
    rootNode.addObject('DefaultPipeline', verbose='0')
    rootNode.addObject('BruteForceBroadPhase')
    rootNode.addObject('BVHNarrowPhase')
    rootNode.addObject('DefaultContactManager', response='FrictionContactConstraint')
    rootNode.addObject('LocalMinDistance', name="Proximity", alarmDistance='0', contactDistance='0')

                
    #rootNode.addObject('ClipPlane', normal='0 0 1')
    

                
                
    #mergeMesh
    mergeMesh = rootNode.addChild('mergeMesh')
    l1=mergeMesh.addObject('MeshVTKLoader', name="mesh1", filename=meshRobot, translation="28 5 0")
    l2=mergeMesh.addObject('MeshVTKLoader', name="mesh2", filename=meshRobot, translation=str(tr_x)+' 5 '+ str(tr_z), rotation="0 120 0")
    l3=mergeMesh.addObject('MeshVTKLoader', name="mesh3", filename=meshRobot, translation=str(tr_x)+' 5 '+ str(-tr_z), rotation="0 240 0")


    
    mergeEngine=mergeMesh.addObject('MergeMeshes', name="Merge", nbMeshes="3", position1="@mesh1.position", tetrahedra1="@mesh1.tetrahedra",
                                position2="@mesh2.position", tetrahedra2="@mesh2.tetrahedra",
                                position3="@mesh3.position", tetrahedra3="@mesh3.tetrahedra")
    mergeEngine.init();

                    
    boxFix= mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_fix',box='-60 -1 -60 60 5 60',drawBoxes='1', drawPoints='1', position="@Merge.position")
    boxIndep=mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_indep',box='-60 -6 -60 60 70 60',drawBoxes='1', drawPoints='0', position="@Merge.position")
    boxFrame1= mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_frame1',box='-60 70.0000001 -60 60 76 60',drawBoxes='1', drawPoints='1', position="@Merge.position")

    boxIndep2=mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_indep2',box='-60 -6 -60 60 75 60',drawBoxes='1', drawPoints='0', position="@Merge.position")
    boxFrame2= mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_frame2',box='-60 75.0000001 -60 60 81 60',drawBoxes='1', drawPoints='1', position="@Merge.position")

    ####################################################
    # Fill list for subsetmultimapping
    numPoints = mergeEngine.findData('npoints').value;
    boxFrame1.init();
    IndicesFrame1= boxFrame1.findData('indices').value;
    IndicesFrame1 = flatten(IndicesFrame1);
    
    boxIndep.init();
    freeNodes= boxIndep.findData('indices').value;
    freeNodes = flatten(freeNodes);
    
    rigidBlocks = [IndicesFrame1];
    
    indexPairs = rigidification.fillIndexPairs(numPoints,freeNodes,rigidBlocks)
    indexPairsStr = str(indexPairs)
    ####################################################

    
    # composite model
    compositeNode = rootNode.addChild('CompositeModel')
    compositeNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0', rayleighMass='0', firstOrder=False)
    compositeNode.addObject('SparseLDLSolver', name="ldlsolveur")
    #compositeNode.addObject('CGLinearSolver', iterations='50', tolerance="1e-5", threshold="1e-10")
    compositeNode.addObject('GenericConstraintCorrection', solverName='ldlsolveur')
                    

        
    #---------------------------------------------------------------------------------------------
    # ---------------------- Intervertebre rigide ----------------------------------
    #---------------------------------------------------------------------------------------------
    interv1Node = compositeNode.addChild('Intervertebra1')
    interv1Node.addObject('MechanicalObject', template="Rigid3",name='interv1MO',position='0 80 0 0 0 0 1')
    #top_disc1Node.addObject('UniformMass',name='mass',totalMass='0.000001',showAxisSizeFactor='0.005')
    interv1Node.addObject('PartialRigidificationConstraint')
    #interv1Node.addObject('ConstantForceField', force='0 100 0 0 0 0')
    
    #---------------------------------------------------------------------------------------------
    # ---------------------- Particules independantes ----------------------------------
    #---------------------------------------------------------------------------------------------
    indep_particulesNode = compositeNode.addChild('Independant_Particules')
    indep_particulesNode.addObject('PointSetTopologyContainer', position='@../../mergeMesh/box_roi_indep2.pointsInROI')
    IndependantParticles_dof=indep_particulesNode.addObject('MechanicalObject', template='Vec3', name='IndependantParticles_dof')
    #indep_particulesNode.addObject('UniformMass',name='mass',totalMass='0.1')
    indep_particulesNode.addObject('BoxROI',name='box_roi',box='-60 -1 -60 60 5 60',drawBoxes='1', drawPoints='1')
    indep_particulesNode.addObject('FixedConstraint', indices='@box_roi.indices')
    
    DeformableGridNode = indep_particulesNode.addChild('DeformableGrid')
    
    
    
    #---------------------------------------------------------------------------------------------
    # ---------------------- Particules liees au rigide ----------------------
    #---------------------------------------------------------------------------------------------
    Mapped_ParticuleNode = interv1Node.addChild('Mapped_Particule')
    Mapped_ParticuleNode.addObject('PointSetTopologyContainer', position='@../../../mergeMesh/box_roi_frame2.pointsInROI')
    Mapped_Particles_dof=Mapped_ParticuleNode.addObject('MechanicalObject', template='Vec3', name='Mapped_Particles_dof',  showIndices=False)
    Mapped_ParticuleNode.addObject('RigidMapping', name="rigidMap", input='@..',output='@.', globalToLocalCoords=True)
    
        
    #---------------------------------------------------------------------------------------------
    # ---------------------- Somme des particules et du rigide ----------------------
    #---------------------------------------------------------------------------------------------
        
    Mapped_ParticuleNode.addChild(DeformableGridNode)
    DeformableGridNode.addObject('MeshTopology', src='@../../../../mergeMesh/Merge', name="mesh")
    DeformableGridNode.addObject('MechanicalObject',template='Vec3',name='mergeDofs')
        
    DeformableGridNode.addObject('TetrahedronFEMForceField', name="tetraFF", youngModulus="600", poissonRatio="0.45")

    deformableGrid_mappaddPointing = DeformableGridNode.addObject('SubsetMultiMapping',template='Vec3,Vec3d',name='deformableGrid_mapping', input='@../../../CompositeModel/Independant_Particules/IndependantParticles_dof @../../../CompositeModel/Intervertebra1/Mapped_Particule/Mapped_Particles_dof ', output='@./mergeDofs', indexPairs=indexPairsStr)
    compositeNode.addObject('PartialRigidificationForceField', object1='@./Independant_Particules/IndependantParticles_dof', object2='@./Intervertebra1/interv1MO', rigidMapping='@./Intervertebra1/Mapped_Particule/rigidMap', subsetMultiMapping='@./Independant_Particules/DeformableGrid/deformableGrid_mapping', mappedForceField='@./Independant_Particules/DeformableGrid/tetraFF' )
    
 

    
    # ---------------------- version mappee ------------------
    #effector = interv1Node.addChild('effector')
    #effector.addObject('MechanicalObject', name="effectorPoint", position="0 0 0")
    #effector.addObject('SphereCollisionModel', radius='0.05', group='1')
    #effector.addObject('PositionEffector', template='Vec3', indices="0 1", effectorGoal="@../../../goal/goalPoints/goalMO.position")
    #effector.addObject('RigidMapping', name="rigidMap", input='@..',output='@.')


    #mergeMesh.addObject('MeshVTKLoader', name="mesh2", filename=meshRobot, translation="1.5 0 -2.5")
    #mergeMesh.addObject('MeshVTKLoader', name="mesh3", filename=meshRobot, translation="-3 0 0")
    
    
    #---------------------------------------------------------------------------------------------
    # ---------------------- Visu (Intervertebra) ----------------------
    #---------------------------------------------------------------------------------------------
    visuIntervertebra= interv1Node.addChild('visuIntervertebra')
    visuIntervertebra.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, scale='9,6',translation="28 0 0",  rotation="0 180 0")
    visuIntervertebra.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra.addObject('OglModel')
    visuIntervertebra.addObject('RigidMapping', name="rigidMapVisu", input='@..',output='@.')
        
        
        
    return rootNode

