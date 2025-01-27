
import Sofa

import os
path = os.path.dirname(os.path.abspath(__file__))+'/robot_challenge/'
meshRobot=path+'springy_robot_tetra_2000vert.vtu'
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
    rootNode.findData('dt').value=0.01;
    rootNode.findData('gravity').value='0 -981 0';
    rootNode.addObject('VisualStyle', displayFlags='showVisualModels showForceFields showInteractionForceFields hideCollisionModels hideBoundingCollisionModels hideWireframe');

    #Required plugin
    rootNode.addObject('RequiredPlugin', pluginName='SoftRobots');

    rootNode.addObject('FreeMotionAnimationLoop')
    rootNode.addObject('GenericConstraintSolver')

    rootNode.addObject('DefaultPipeline', verbose='0')
    rootNode.addObject('BruteForceBroadPhase')
    rootNode.addObject('BVHNarrowPhase')
    rootNode.addObject('DefaultContactManager', response='FrictionContactConstraint')
    rootNode.addObject('LocalMinDistance', name="Proximity", alarmDistance='0', contactDistance='0')
    rootNode.addObject('BackgroundSetting', color='0 0.168627 0.211765')
    rootNode.addObject('OglSceneFrame', style="Arrows", alignment="TopRight")

    rootNode.addObject('ClipPlane', normal='0 0 1')




    ##########################################
    # FEM Model                              #
    ##########################################
    SingleActuator = rootNode.addChild('SingleActuator')
    SingleActuator.addObject('EulerImplicitSolver', name='odesolver', firstOrder=True)
    SingleActuator.addObject('ShewchukPCGLinearSolver', iterations='15', name='linearsolver', tolerance='1e-5', preconditioners='preconditioner', use_precond=True, use_first_precond=False, update_step='1')

    SingleActuator.addObject('MeshVTKLoader', name='loader', filename=meshRobot)
    SingleActuator.addObject('TetrahedronSetTopologyContainer', src='@loader', name='container')
    SingleActuator.addObject('TetrahedronSetTopologyModifier')

    SingleActuator.addObject('MechanicalObject', name='tetras', template='Vec3', showIndices=False, showIndicesScale='4e-5', rx='0', dz='0')
    SingleActuator.addObject('UniformMass', totalMass='0.5')
    SingleActuator.addObject('TetrahedronFEMForceField', template='Vec3', name='FEM', method='large', poissonRatio='0.3',  youngModulus='18000')

    SingleActuator.addObject('BoxROI', name='ROI1', box='-6 -0.01 -6 6 0.5 6', drawBoxes=True)

    SingleActuator.addObject('RestShapeSpringsForceField', points='@ROI1.indices', stiffness='1e12')

    SingleActuator.addObject('SparseLDLSolver', name='preconditioner', useWarping=True)
    SingleActuator.addObject('LinearSolverConstraintCorrection', solverName='preconditioner')

    mergeMeshTri = SingleActuator.addChild('tri')
    mergeMeshTri.addObject('TriangleSetTopologyContainer', name='container', position='@../container.position')
    mergeMeshTri.addObject('TriangleSetTopologyModifier')
    mergeMeshTri.addObject('Tetra2TriangleTopologicalMapping', name='Mapping', object1='../container', object2='container')
    mergeMeshTri.addObject('MeshSTLLoader', name="loadCavity", filename=meshSelect) #scale3d='1.1 1.1 1.1'
    cavityBox11= mergeMeshTri.addObject('MeshROI', name="meshROI", position="@../container.position", triangles="@container.triangles", ROIposition="@loadCavity.position", ROItriangles="@loadCavity.triangles",computeEdges='0', computeTriangles='1', computeTetrahedra='0' )



    cavity = SingleActuator.addChild('cavity')
    cavity.addObject('MeshTopology', position='@../container.position', triangles="@../tri/meshROI.trianglesInROI", name="cavityMesh")
    cavity.addObject('SurfacePressureConstraint', template='Vec3', triangles='@cavityMesh.triangles', valueType='volumeGrowth', value="8", visualization='1', showVisuScale='0.0002')
    cavity.addObject('PythonScriptController', filename="controller.py", classname="controller")
    cavity.addObject('Triangle')









    return rootNode
