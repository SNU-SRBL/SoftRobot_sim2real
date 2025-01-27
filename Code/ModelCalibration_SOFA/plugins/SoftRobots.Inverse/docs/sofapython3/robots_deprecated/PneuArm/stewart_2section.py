
import Sofa

import os
path = os.path.dirname(os.path.abspath(__file__))+'/robot_challenge/'
meshRobot=path+'springy_robot_tetra_4000vert.vtu'
meshIntervertebra=path+'rigid-intervertebra-oneside.stl'
meshSelect=path+'BiggerSelect.stl'
path2 = os.path.dirname(os.path.abspath(__file__))+'/'
compliance2IntervertebraTXT = path2+'c2Intervertebra.txt'

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
    rootNode.findData('dt').value=0.1;
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
    goal.findData('activated').value=1;
    goal.addObject('EulerImplicitSolver', firstOrder=True)
    goal.addObject('CGLinearSolver', iterations='100', tolerance="1e-5", threshold="1e-10")
    goal.addObject('MechanicalObject', name='goalMORigide', template="Rigid3", position='0 10.5 0 0 0 0 1')
    goal.addObject('UniformMass',  totalMass='0.1')
    goal.addObject('UncoupledConstraintCorrection')
    goalPoints= goal.addChild('goalPoints')
    goalPoints.addObject('MechanicalObject', name='goalMO', template='Vec3', position='0 0 0  1 0 0  0 1 0  0 0 1')
    goalPoints.addObject('SphereCollisionModel', radius='0.2', group='1')
    goalPoints.addObject('RigidMapping', name="rigidMap", input='@..',output='@.')



    #mergeMesh
    mergeMesh = rootNode.addChild('mergeMesh')
    mergeMesh.findData('activated').value=0;
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



    # ---------------------------------------------------------------------------------------------
    # ----------------------  Simplified version ----------------------
    # ---------------------------------------------------------------------------------------------
    compareNode = rootNode.addChild('complianceCylinder')
    #compareNode.addObject('Euler')
    compareNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0.1', rayleighMass='10', firstOrder=False)
    #compareNode.addObject('CGLinearSolver', iterations='100', tolerance="1e-5", threshold="1e-10")
    compareNode.addObject('PCGLinearSolver', preconditioners='precond')
    compareNode.addObject('SparseLDLSolver', name="precond")
    compareNode.addObject('MechanicalObject', name='SimplifiedMO', template="Rigid3", position='0 0 0 0 0 0 1     0 5 0 0 0 0 1    0 10 0 0 0 0 1')
    compareNode.addObject('UniformMass',name='mass',totalMass='10',showAxisSizeFactor='1')
    compareNode.addObject('PREquivalentStiffnessForceField', complianceFile=compliance2IntervertebraTXT, printLog="1")
    compareNode.addObject('GenericConstraintCorrection', solverName='precond')
    compareNode.addObject('FixedConstraint', name='fixed', indices='0')


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cavity) ----------------------
    # ---------------------------------------------------------------------------------------------
    MappedCavity11Node=compareNode.addChild('MappedCavity11')
    MappedCavity11Node.addObject('MeshSTLLoader', name="loadCavity11", filename=meshSelect, translation="1.5 0 2.5")
    MappedCavity11Node.addObject('MeshTopology', src='@loadCavity11', name="cavityMesh")
    MappedCavity11Node.addObject('MechanicalObject',template='Vec3',name='cavity11Dofs')
    # MappedCavity11Node.addObject('Triangle')
    MappedCavity11Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles',  visualization='1', showVisuScale='0.0002')
    MappedCavity11Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity11Dofs" ,nbRef='2')

    MappedCavity12Node=compareNode.addChild('MappedCavity12')
    MappedCavity12Node.addObject('MeshSTLLoader', name="loadCavity12", filename=meshSelect, translation="1.5 0 -2.5",  rotation="0 120 0")
    MappedCavity12Node.addObject('MeshTopology', src='@loadCavity12', name="cavityMesh")
    MappedCavity12Node.addObject('MechanicalObject',template='Vec3',name='cavity12Dofs')
    # MappedCavity12Node.addObject('Triangle')
    MappedCavity12Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles',  visualization='1', showVisuScale='0.0002')
    MappedCavity12Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity12Dofs" ,nbRef='2')

    MappedCavity13Node=compareNode.addChild('MappedCavity13')
    MappedCavity13Node.addObject('MeshSTLLoader', name="loadCavity13", filename=meshSelect, translation="-3 0 0",  rotation="0 240 0")
    MappedCavity13Node.addObject('MeshTopology', src='@loadCavity13', name="cavityMesh")
    MappedCavity13Node.addObject('MechanicalObject',template='Vec3',name='cavity13Dofs')
    # MappedCavity13Node.addObject('Triangle')
    MappedCavity13Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles',  visualization='1', showVisuScale='0.0002')
    MappedCavity13Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity13Dofs" ,nbRef='2')




    MappedCavity21Node=compareNode.addChild('MappedCavity21')
    MappedCavity21Node.addObject('MeshSTLLoader', name="loadCavity21", filename=meshSelect, translation="1.5 5 2.5")
    MappedCavity21Node.addObject('MeshTopology', src='@loadCavity21', name="cavityMesh")
    MappedCavity21Node.addObject('MechanicalObject',template='Vec3',name='cavity21Dofs')
    # MappedCavity21Node.addObject('Triangle')
    MappedCavity21Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles',  visualization='1', showVisuScale='0.0002')
    MappedCavity21Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity21Dofs" ,nbRef='2')

    MappedCavity22Node=compareNode.addChild('MappedCavity22')
    MappedCavity22Node.addObject('MeshSTLLoader', name="loadCavity22", filename=meshSelect, translation="1.5 5 -2.5",  rotation="0 120 0")
    MappedCavity22Node.addObject('MeshTopology', src='@loadCavity22', name="cavityMesh")
    MappedCavity22Node.addObject('MechanicalObject',template='Vec3',name='cavity22Dofs')
    # MappedCavity22Node.addObject('Triangle')
    MappedCavity22Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', visualization='1', showVisuScale='0.0002')
    MappedCavity22Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity22Dofs" ,nbRef='2')

    MappedCavity23Node=compareNode.addChild('MappedCavity23')
    MappedCavity23Node.addObject('MeshSTLLoader', name="loadCavity23", filename=meshSelect, translation="-3 5 0",  rotation="0 240 0")
    MappedCavity23Node.addObject('MeshTopology', src='@loadCavity23', name="cavityMesh")
    MappedCavity23Node.addObject('MechanicalObject',template='Vec3',name='cavity23Dofs')
    # MappedCavity23Node.addObject('Triangle')
    MappedCavity23Node.addObject('SurfacePressureActuator', template='Vec3', triangles='@cavityMesh.triangles', visualization='1', showVisuScale='0.0002')
    MappedCavity23Node.addObject('SkinningMapping', name='baryMap', input="@../SimplifiedMO", output="@cavity23Dofs" ,nbRef='2')



    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (cables) ----------------------
    # ---------------------------------------------------------------------------------------------
    MappedCables = compareNode.addChild('cables')
    MappedCables.addObject('MechanicalObject', name="cablePoint", position="3 0 0  -1.5 0 2.5  -1.5 0 -2.5   3 0 0  -1.5 0 2.5  -1.5 0 -2.5 ")
    MappedCables.addObject('RigidMapping', rigidIndexPerPoint="1 1 1 2 2 2", name="rigidMapCablePoints", input='@..',output='@.')

    MappedCables.addObject('CableActuator', template="Vec3", name="c11" , indices="3 0", pullPoint="3 0 0" )
    MappedCables.addObject('CableActuator', template="Vec3", name="c22" , indices="4 1", pullPoint="-1.5 0 2.5" )
    MappedCables.addObject('CableActuator', template="Vec3", name="c33" , indices="5 2", pullPoint="-1.5 0 -2.5")


    # steewart platform
    MappedCables.addObject('CableActuator', template="Vec3", name="c1" , indices="0", pullPoint="4 0 4" )
    MappedCables.addObject('CableActuator', template="Vec3", name="c2" , indices="1", pullPoint="1.46 0 5.46" )
    MappedCables.addObject('CableActuator', template="Vec3", name="c3" , indices="2", pullPoint="-5.46 0 -1.46" )
    MappedCables.addObject('CableActuator', template="Vec3", name="c4" , indices="0", pullPoint="4 0 -4" )
    MappedCables.addObject('CableActuator', template="Vec3", name="c5" , indices="1", pullPoint="-5.46 0 1.46" )
    MappedCables.addObject('CableActuator', template="Vec3", name="c6" , indices="2", pullPoint="1.46 0 -5.46" )
    # ---------------------------------------------------------------------------------------------
    # ---------------------- Contraintes (Effector) ----------------------
    # ---------------------------------------------------------------------------------------------
    # ---------------------- version 6D ----------------------
    compareNode.addObject('PositionEffector', template="Rigid3", indices="2", effectorGoal="@../goal/goalMORigide.position")


    # ---------------------------------------------------------------------------------------------
    # ---------------------- Visu (Intervertebra) ----------------------
    # ---------------------------------------------------------------------------------------------
    visuIntervertebra1= compareNode.addChild('visuIntervertebra1')
    visuIntervertebra1.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, translation="-3 0 0",  rotation="0 0 0")
    visuIntervertebra1.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra1.addObject('OglModel')
    visuIntervertebra1.addObject('RigidMapping', index="1", name="rigidMapVisu", input='@..',output='@.')

    visuIntervertebra2= compareNode.addChild('visuIntervertebra2')
    visuIntervertebra2.addObject('MeshSTLLoader', name="loadIntervertebra", filename=meshIntervertebra, translation="-3 0 0",  rotation="0 0 0")
    visuIntervertebra2.addObject('MeshTopology', src='@loadIntervertebra', name="intervertebraMesh")
    visuIntervertebra2.addObject('OglModel')
    visuIntervertebra2.addObject('RigidMapping', index="2", name="rigidMapVisu", input='@..',output='@.')

    return rootNode
