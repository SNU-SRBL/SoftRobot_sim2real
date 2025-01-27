
import Sofa

import os
path = os.path.dirname(os.path.abspath(__file__))+'/robot_challenge/'
meshRobot=path+'springy_robot_tetra_1000vert.vtu'
meshIntervertebra=path+'rigid-intervertebra-oneside.stl'
meshSelect=path+'BiggerSelect.stl'

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
    rootNode.findData('dt').value=1;
    rootNode.findData('gravity').value='0 0 0';
    rootNode.addObject('VisualStyle', displayFlags='showVisualModels showForceFields showInteractionForceFields hideCollisionModels hideBoundingCollisionModels hideWireframe');

    #Required plugin
    rootNode.addObject('RequiredPlugin', pluginName='SoftRobot');

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
    mergeMesh.addObject('MeshVTKLoader', name="mesh1", filename=meshRobot, translation="1.5 0 2.5")
    mergeMesh.addObject('MeshVTKLoader', name="mesh2", filename=meshRobot, translation="1.5 0 -2.5", rotation="0 120 0")
    mergeMesh.addObject('MeshVTKLoader', name="mesh3", filename=meshRobot, translation="-3 0 0", rotation="0 240 0")
    mergeEngine=mergeMesh.addObject('MergeMeshes', name="Merge", nbMeshes="3", position1="@mesh1.position", tetrahedra1="@mesh1.tetrahedra",
                                position2="@mesh2.position", tetrahedra2="@mesh2.tetrahedra",
                                position3="@mesh3.position", tetrahedra3="@mesh3.tetrahedra")


    boxFix= mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_fix',box='-6 -0.01 -6 6 1 6',drawBoxes='1', drawPoints='0', position="@Merge.position")
    boxIndep=mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_indep',box='-6 -0.01 -6 6 4 6',drawBoxes='1', drawPoints='0', position="@Merge.position")
    boxFrame1= mergeMesh.addObject('BoxROI',template="Vec3", name='box_roi_frame1',box='-6 4 -6 6 5 6',drawBoxes='1', drawPoints='0', position="@Merge.position")

    # tetra topology => triangle topology
    mergeMesh.addObject('TetrahedronSetTopologyContainer', src='@Merge', name='container')
    mergeMesh.addObject('TetrahedronSetTopologyModifier')

    mergeMesh.addObject('MechanicalObject', name='tetras', template='Vec3', showIndices=False, showIndicesScale='4e-5', rx='0', dz='0')
    #mergeMesh.addObject('TetrahedronFEMForceField', name="tetraFF", youngModulus="600", poissonRatio="0.45")
    # triangle topology
    mergeMeshTri = mergeMesh.addChild('tri')
    mergeMeshTri.addObject('TriangleSetTopologyContainer', name='container', position='@../container.position')
    mergeMeshTri.addObject('TriangleSetTopologyModifier')
    mergeMeshTri.addObject('Tetra2TriangleTopologicalMapping', name='Mapping', object1='../container', object2='container')
    mergeMeshTri.addObject('MeshSTLLoader', name="loadCavity11", filename=meshSelect, translation="1.5 0 2.5") #scale3d='1.1 1.1 1.1'
    cavityBox11= mergeMeshTri.addObject('MeshROI', name="meshROI11", position="@../container.position", triangles="@container.triangles", ROIposition="@loadCavity11.position", ROItriangles="@loadCavity11.triangles",computeEdges='0', computeTriangles='1', computeTetrahedra='0' )

    mergeMeshTri.addObject('MeshSTLLoader', name="loadCavity12", filename=meshSelect, translation="1.5 0 -2.5") #scale3d='1.1 1.1 1.1'
    cavityBox12= mergeMeshTri.addObject('MeshROI', name="meshROI12", position="@../container.position", triangles="@container.triangles", ROIposition="@loadCavity12.position", ROItriangles="@loadCavity12.triangles",computeEdges='0', computeTriangles='1', computeTetrahedra='0' )

    mergeMeshTri.addObject('MeshSTLLoader', name="loadCavity13", filename=meshSelect, translation="-3 0 0") #scale3d='1.1 1.1 1.1'
    cavityBox13= mergeMeshTri.addObject('MeshROI', name="meshROI13", position="@../container.position", triangles="@container.triangles", ROIposition="@loadCavity13.position", ROItriangles="@loadCavity13.triangles",computeEdges='0', computeTriangles='1', computeTetrahedra='0' )


    mergeEngine.init();
    numPoints = mergeEngine.findData('npoints').value;
    boxFrame1.init();
    IndicesFrame1= boxFrame1.findData('indices').value;
    #print "PointRigi";
    #print IndicesFrame1;
    print(numPoints)

    print('+++++++++++++++++++++++++++++++++++')
    print(len(IndicesFrame1))
    print('+++++++++++++++++++++++++++++++++++')

    indexPairs = fillIndexPairs(IndicesFrame1, numPoints);
    indexPairsStr = str(indexPairs)


    # composite model
    compositeNode = rootNode.addChild('CompositeModel')
    compositeNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0', rayleighMass='0', firstOrder=False)
    compositeNode.addObject('SparseLDLSolver', name="ldlsolveur")
    #compositeNode.addObject('CGLinearSolver', iterations='50', tolerance="1e-5", threshold="1e-10")
    compositeNode.addObject('GenericConstraintCorrection', solverName='ldlsolveur')



    # ---------------------------------------------------------------------------------------------
    # ---------------------- Intervertebre rigide ----------------------------------
    # ---------------------------------------------------------------------------------------------
    interv1Node = compositeNode.addChild('Intervertebra1')
    interv1Node.addObject('MechanicalObject', template="Rigid3",name='interv1MO',position='0 5 0 0 0 0 1')
    #top_disc1Node.addObject('UniformMass',name='mass',totalMass='0.000001',showAxisSizeFactor='0.005')
    interv1Node.addObject('PartialRigidificationConstraint')
    interv1Node.addObject('ConstantForceField', force='0 100 0 0 0 0')

    # ---------------------------------------------------------------------------------------------
    # ---------------------- Particules independantes ----------------------------------
    # ---------------------------------------------------------------------------------------------
    indep_particulesNode = compositeNode.addChild('Independant_Particules')
    indep_particulesNode.addObject('PointSetTopologyContainer', position='@../../mergeMesh/box_roi_indep.pointsInROI')
    IndependantParticles_dof=indep_particulesNode.addObject('MechanicalObject', template='Vec3', name='IndependantParticles_dof')
    #indep_particulesNode.addObject('UniformMass',name='mass',totalMass='0.1')
    indep_particulesNode.addObject('BoxROI',name='box_roi',box='-6 -0.01 -6 6 1 6',drawBoxes='1', drawPoints='1')
    indep_particulesNode.addObject('FixedConstraint', indices='@box_roi.indices')

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


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Visu (Intervertebra) ----------------------
    # ---------------------------------------------------------------------------------------------
    visuIntervertebra= interv1Node.addChild('visuIntervertebra')
    visuIntervertebra.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, translation="-3 0 0",  rotation="0 0 0")
    visuIntervertebra.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra.addObject('OglModel')
    visuIntervertebra.addObject('RigidMapping', name="rigidMapVisu", input='@..',output='@.')



    return rootNode
