import Sofa
import random

# utility methods

def fillIndexPairs(numNodeParent0, numNodeParent1):

	i=0
	indexPairs=[1,1]*(numNodeParent0+numNodeParent1)
	for j in range(360) :
		indexPairs[2*i] = 0
		indexPairs[2*i+1] = j
		i=i+1

	for j in range(36) :
		indexPairs[2*i] = 1
		indexPairs[2*i+1] = j
		i=i+1


	for j in range(10) :
		indexPairs[2*i] = 0
		indexPairs[2*i+1] = j+360
		i=i+1

	for j in range(1) :
		indexPairs[2*i] = 1
		indexPairs[2*i+1] = j+36
		i=i+1



	return indexPairs









# scene creation method
def createScene(rootNode):

	# scene global stuff
	rootNode.addObject('VisualStyle', displayFlags='showBehaviorModels hideCollisionModels hideMappings showForceFields')
	rootNode.addObject('DefaultPipeline', verbose=0, depth=10, draw=0)
	rootNode.addObject('BruteForceBroadPhase')
	rootNode.addObject('BVHNarrowPhase')
	rootNode.addObject('MinProximityIntersection', name='Proximity', alarmDistance=0.5, contactDistance=0.33)
	rootNode.addObject('DefaultContactManager', name='Response', response='default')
	rootNode.addObject('CollisionGroup', name='Group')
	rootNode.findData('dt').value=0.01

	rootNode.addObject('FreeMotionAnimationLoop')
	rootNode.addObject('GenericConstraintSolver', printLog='1')

       	# ---------------------------------------------------------------------------------------------
       	# ----------------------Noeud de definition des) points independants et lies -------------------
      	# ---------------------------------------------------------------------------------------------
	Silicon_topoNode = rootNode.addChild('Silicon_topo')
	Silicon_topoNode.addObject('MeshGmshLoader', name='loader', filename='cylinder.mesh')
	Silicon_topoNode.addObject('HexahedronSetTopologyContainer', src='@loader', name='mesh')
#	Silicon_topoNode.addObject('MechanicalObject',  showIndices=False)

	# -- option 1 => topo mapping... (does not work...)
	## Silicon_moduleNode = Silicon_topoNode.addChild('Silicon_module')
	## Silicon_moduleNode.addObject('TetrahedronSetTopologyContainer', name='Container', position="@../loader.position")
	## Silicon_moduleNode.addObject('TetrahedronSetTopologyModifier', name='Modifier')
	## Silicon_moduleNode.addObject('Hexa2TetraTopologicalMapping', name='topoMap', input='@../mesh', output='@Container' )
       	## Silicon_moduleNode.addObject('MechanicalObject',  showIndices=True)
       	## Silicon_moduleNode.addObject('BoxROI',name='box_roi',box='-0.013 -0.013 -0.001 0.013 0.013 0.001',drawBoxes='1')
       	## Silicon_moduleNode.addObject('BoxROI',name='box_roi_indep',box='-0.013 -0.013 -0.001 0.013 0.013 0.046',drawBoxes='1')
       	## Silicon_moduleNode.addObject('BoxROI',name='box_roi_rigid',box='-0.013 -0.013 0.048 0.013 0.013 0.05',drawBoxes='1')

	# -- option 2 => no topo mapping

	boxIndep = Silicon_topoNode.addObject('BoxROI',template="Vec3", name='box_roi_indep',box='-0.013 -0.013 -0.001 0.013 0.013 0.046',drawBoxes='0', drawPoints='0')
	boxRigi = Silicon_topoNode.addObject('BoxROI',template="Vec3", name='box_roi_rigid',box='-0.013 -0.013 0.048 0.013 0.013 0.05',drawBoxes='1', drawPoints='0')



	# composite model #
	compositeNode = rootNode.addChild('CompositeModel')
	compositeNode.addObject('EulerImplicitSolver',name='cg_odesolver',printLog=False, rayleighStiffness='0.0', rayleighMass='0', firstOrder=True)
	#compositeNode.addObject('PCGLinearSolver',name='linear solver',iterations='200',tolerance='1.0e-18',threshold='1.0e-30', preconditioners="precond")
	#compositeNode.addObject('JacobiPreconditioner', name="precond")
	compositeNode.addObject('SparseLUSolver', name="precond")
	compositeNode.addObject('GenericConstraintCorrection', solverName="precond")

	# ---------------------------------------------------------------------------------------------
	# ---------------------- Particules independantes ----------------------------------
	# ---------------------------------------------------------------------------------------------

	indep_particulesNode = compositeNode.addChild('Independant_Particules')
	indep_particulesNode.addObject('PointSetTopologyContainer', position='@../../Silicon_topo/box_roi_indep.pointsInROI')
	IndependantParticles_dof=indep_particulesNode.addObject('MechanicalObject', template='Vec3', name='IndependantParticles_dof')
	#indep_particulesNode.addObject('UniformMass',name='mass',totalMass='0.1')
	indep_particulesNode.addObject('BoxROI',name='box_roi',box='-0.013 -0.013 -0.001 0.013 0.013 0.001',drawBoxes='1', drawPoints='1')
	indep_particulesNode.addObject('FixedConstraint', indices='@box_roi.indices')

	DeformableGridNode = indep_particulesNode.addChild('DeformableGrid')
	# ---------------------------------------------------------------------------------------------
	# ---------------------- Top disque rigide ----------------------------------
	# ---------------------------------------------------------------------------------------------
	top_disc1Node = compositeNode.addChild('top_disc1')
	top_disc1Node.addObject('MechanicalObject', template="Rigid3",name='top_disc1',position='0 0 0.050 0 0 0 1')
	#top_disc1Node.addObject('UniformMass',name='mass',totalMass='0.000001',showAxisSizeFactor='0.005')
	top_disc1Node.addObject('PartialRigidificationConstraint')

	# ---------------------------------------------------------------------------------------------
	# ---------------------- Particules liees au rigide ----------------------
	# ---------------------------------------------------------------------------------------------
	Mapped_ParticuleNode = top_disc1Node.addChild('Mapped_Particule')
	Mapped_ParticuleNode.addObject('PointSetTopologyContainer', position='@../../../Silicon_topo/box_roi_rigid.pointsInROI')
	Mapped_Particles_dof=Mapped_ParticuleNode.addObject('MechanicalObject', template='Vec3', name='Mapped_Particles_dof',  showIndices=False)
	Mapped_ParticuleNode.addObject('RigidMapping', name="rigidMap", input='@..',output='@.', globalToLocalCoords=True)

	# ---------------------------------------------------------------------------------------------
	# ---------------------- Somme des particules et du rigide ----------------------
	# ---------------------------------------------------------------------------------------------

	Mapped_ParticuleNode.addChild(DeformableGridNode)
	DeformableGridNode.addObject('MeshTopology', src='@../../../../Silicon_topo/loader', name="mesh")
	DeformableGridNode.addObject('MechanicalObject',template='Vec3',name='deformableGrid_dof')
	DeformableGridNode.addObject('Point')



	DeformableGridNode.addObject('HexahedronFEMForceField', name="hexaFF", youngModulus="6000000")



	#-- init du mapping --
	PointsIndep = boxIndep.findData('pointsInROI').value
	PointsRigi = boxRigi.findData('pointsInROI').value



	indexPairsComputation = fillIndexPairs(370, 37)
	indexPairsStr = str(indexPairsComputation);


	print(indexPairsStr)


	deformableGrid_mappaddPointing = DeformableGridNode.addObject('SubsetMultiMapping',template='Vec3,Vec3d',name='deformableGrid_mapping', input='@../../../CompositeModel/Independant_Particules/IndependantParticles_dof @../../../CompositeModel/top_disc1/Mapped_Particule/Mapped_Particles_dof', output='@./deformableGrid_dof', indexPairs=indexPairsStr)
	compositeNode.addObject('PartialRigidificationForceField', object1='@./Independant_Particules/IndependantParticles_dof', object2='@./top_disc1/top_disc1', rigidMapping='@./top_disc1/Mapped_Particule/rigidMap', subsetMultiMapping='@./Independant_Particules/DeformableGrid/deformableGrid_mapping', mappedForceField='@./Independant_Particules/DeformableGrid/hexaFF' )




	return rootNode
