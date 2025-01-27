import Sofa

import os
path = os.path.dirname(os.path.abspath(__file__))+'/mesh/'
dirpath = os.path.dirname(os.path.abspath(__file__))+'/'

def createScene(rootNode):
                rootNode.addObject('RequiredPlugin', pluginName='SoftRobots')
                rootNode.addObject('RequiredPlugin', pluginName='BeamAdapter')
                rootNode.addObject('VisualStyle', displayFlags='showVisualModels hideBehaviorModels showCollisionModels hideBoundingCollisionModels hideForceFields showInteractionForceFields hideWireframe')

                rootNode.addObject('FreeMotionAnimationLoop')
		rootNode.addObject('QPInverseProblemSolver', printLog="1", epsilon="0.001", QPSolver="CGAL", inputDLength="0 0 0 0 0 0", outputDPressure="0 0 0 0 0 0")
                rootNode.addObject('BackgroundSetting', color='1 1 1')
                rootNode.addObject('OglSceneFrame', style="Arrows", alignment="TopRight")

                #rootNode.addObject('OglGrid', nbSubdiv='10', size='1000')#This just adds a grid to the scene

		#Frames: We create the rigid frames along the virtual backbone of the CBHA

		frames= rootNode.addChild('frames')
		frames.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="1", printLog=False)
		frames.addObject('PCGLinearSolver', preconditioners="preconditioner", tolerance="1e-30")
		frames.addObject('BTDLinearSolver', name="preconditioner", verbose="0")
		frames.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20")
		frames.addObject('MechanicalObject', template="Rigid3", name="DOFs", position=("-40 0 0 0 0 0 1 " + "-30 0 0 0 0 0 1 " + "-20 0 0 0 0 0 1 " +
				    "-10 0 0 0 0 0 1 " + "0 0 0 0 0 0 1 " + "10 0 0 0 0 0 1 " + "20 0 0 0 0 0 1 " + "30 0 0 0 0 0 1 " + "40 0 0 0 0 0 1 " + "50 0 0 0 0 0 1 " +
				    "60 0 0 0 0 0 1 " + "70 0 0 0 0 0 1 " + "80 0 0 0 0 0 1 " + "90 0 0 0 0 0 1 " + "100 0 0 0 0 0 1 " + "110 0 0 0 0 0 1 " + "120 0 0 0 0 0 1 " +
				    "130 0 0 0 0 0 1 " + "140 0 0 0 0 0 1 " + "150 0 0 0 0 0 1 " + "160 0 0 0 0 0 1 "),  scale3d="1.25 1.25 1.25")
		frames.addObject('UniformMass', showAxisSizeFactor="10", totalMass='250')
		frames.addObject('LinearSolverConstraintCorrection', solverName="preconditioner")
		frames.addObject('PREquivalentStiffnessForceField', complianceFile=dirpath+"compFullArm.txt",  coefForce='32.5')

		#For the interactive control

		goal = rootNode.addChild('goal')
                goal.addObject('EulerImplicitSolver', firstOrder=True)
                goal.addObject('CGLinearSolver', iterations='100', tolerance="1e-5", threshold="1e-5")

                # Set the initial position of the effector goal
                goal.addObject('MechanicalObject', name='goalMO',
                                  position='200  0  0')
                goal.addObject('SphereCollisionModel', radius='5')
                goal.addObject('UncoupledConstraintCorrection')


	        ##########################################
                # Effector                               #
                ##########################################
                # effector = frames.addChild('armtip')
                # # Set the effector position(s)
                # effector.addObject('MechanicalObject',
                #         position=("200  0  0"))
                #
                # # Case of position effector
                # #      indices :
                # #      effectorGoal:
                # effector.addObject('PositionEffector', template='Vec3',
                #         indices="0",
                #         effectorGoal="@../../goal/goalMO.position")
                # effector.addObject('RigidMapping', mapForces=False, mapMasses=False, index='20')
                #
                #
                #








                # Sensor: We create the sensors by specifying the position of the sensor guides in CBHA.

                sensor = frames.addChild('sensor')
                sensor.addObject('MechanicalObject', position="1 0 -67 " + "0 0 -65.6625 " + "0 0 -64.325 " + "-1 0 -62.9875 " + "-1.5 0 -61.65 " + "-2 0 -60.3125 " +
				    "-2.5 0 -58.975 " + "-3 0 -57.6375 " + "0 0 -56.3 " + "-1 0 -54.9625 " + "-1.5 0 -53.625 " + "-2 0 -52.2875 " + "-2.55 0 -50.95 " +
				    "-3.5 0 -49.6125 " + "-4 0 -48.275 " + "-4.5 0 -46.9375 " + "-5 0 -45.6 " + "0 -58.0239960339 33.499490806 " + "0 -56.8656811877 32.8307509709 " +
				    "-0.4 -55.7073663415 32.1620111358 " + "-0.9 -54.5490514953 31.4932713006 " + "-1.4 -53.3907366491 30.8245314655 " +
				    "-1.8 -52.2324218029 30.1557916304 " + "-2.5 -51.0741069567 29.4870517953 " + "-3 -49.9157921105 28.8183119602 " + "-1 -48.7574772643 28.149572125 " +
				    "-1 -47.5991624181 27.4808322899 " + "-1.8 -46.4408475719 26.8120924548 " + "-2.3 -45.2825327257 26.1433526197 " + "-2.8 -44.1242178795 25.4746127846 " +
				    "-3.5 -42.9659030333 24.8058729494 " + "-4 -41.8075881871 24.1371331143 " + "-4.8 -40.6492733409 23.4683932792 " + "-5.3 -39.4909584947 22.7996534441 " +
				    "0.5 58.0239960339 33.499490806 " + "0 56.8656811877 32.8307509709 " + "-0.3 55.7073663415 32.1620111358 " + "-0.6 54.5490514953 31.4932713006 " +
				    "-1.3 53.3907366491 30.8245314655 " + "-2 52.2324218029 30.1557916304 " + "-2.5 51.0741069567 29.4870517953 " + "-3 49.9157921105 28.8183119602 " +
				    "-1 48.7574772643 28.149572125 " + "-1.5 47.5991624181 27.4808322899 " + "-2 46.4408475719 26.8120924548 " + "-2.5 45.2825327257 26.1433526197 " +
				    "-3 44.1242178795 25.4746127846 " + "-3.5 42.9659030333 24.8058729494 " + "-3.8 41.8075881871 24.1371331143 " + "-4.2 40.6492733409 23.4683932792 " +
				    "-5 39.4909584947 22.7996534441" )

		# The cable effector allows us to have the lengths of the actuators as inputs for the simulation

		sensor.addObject('CableEffector', name='s1', pullPoint="-5 0 -67", desiredLength="105.607435153", indices="0 1 2 3 4 5 6 7 8") #Put position of the cable points at base vertebra
		sensor.addObject('CableEffector', name='s2', pullPoint="-5 0 -67", desiredLength="201.251475933", indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16") # Put position of the cable points at base vertebra
		sensor.addObject('CableEffector', name='s3', pullPoint="-10 -58.0239960339 33.499490806", desiredLength="109.629190155", indices="17 18 19 20 21 22 23 24 25") # Put position of the cable points at base vertebra
		sensor.addObject('CableEffector', name='s4', pullPoint="-10 -58.0239960339 33.499490806", desiredLength="205.903964704", indices="17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33") # Put position of the cable points at base vertebra
		sensor.addObject('CableEffector', name='s5', pullPoint="-10 58.0239960339 33.499490806", desiredLength="109.631501832", indices="34 35 36 37 38 39 40 41 42") # Put position of the cable points at base vertebra
		sensor.addObject('CableEffector', name='s6', pullPoint="-10 58.0239960339 33.499490806", desiredLength="206.204680909", indices="34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50") # Put position of the cable points at base vertebra
		sensor.addObject('SphereCollisionModel')
		sensor.addObject('RigidMapping', rigidIndexPerPoint="4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")

		#This controller updates the desired lenghts at each simulation step. The lengths are listed in "lengths_inputs_CBHA". The position outputs of this model are listed
		#in the file "results" each time we run the simulation
		sensor.addObject('PythonScriptController', filename="LengthsDataLoader.py", classname="controller")




		#This creates the central beams in between each rigid frame and maps the forces of the nodes kinematically attached to it

		centralBeams=frames.addChild('centralBeams')
		centralBeams.addObject('MeshTopology', name="lines", lines=" 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12  12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20")
		centralBeams.addObject('BeamInterpolation', name="BeamInterpolation",  dofsAndBeamsAligned=True, radius="1.0", defaultYoungModulus="20000000")
		centralBeams.addObject('AdaptiveBeamForceFieldAndMass', name="BeamForceField", computeMass="1", massDensity="0.001")

		#Next, we create each pneumatic actuator and map the DoF to the frames. The number of actuator coincides with the Festo numeration.

		#Actuator 1

		actuator1=frames.addChild('actuator1')
		#actuator1.addObject('VisualStyle', displayFlags='hideBehavior')
		actuator1.addObject('MeshTopology', name="lines", lines="4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12")
		actuator1.addObject('BeamInterpolation', name="BeamInterpolation",  dofsAndBeamsAligned=False, radius="40", innerRadius="39.8",
					DOF0TransformNode0=("0.    0.  -33.2    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -32.4    0.  -0.0498137    0.    0.9987585 " +
							    "0.    0.  -31.6    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -30.8    0.  -0.0498137    0.    0.9987585 " +
							    "0.    0.  -30.     0.  -0.0498137    0.    0.9987585 " + "0.    0.  -29.2    0.  -0.0498137    0.    0.9987585 " +
							    "0.    0.  -28.4    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -27.6    0.  -0.0498137    0.    0.9987585"),
					DOF1TransformNode1=("0.    0.  -32.4    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -31.6    0.  -0.0498137    0.    0.9987585 " +
							    "0.    0.  -30.8    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -30.     0.  -0.0498137    0.    0.9987585 " +
							    "0.    0.  -29.2    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -28.4    0.  -0.0498137    0.    0.9987585 " +
							    "0.    0.  -27.6    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -26.8    0.  -0.0498137    0.    0.9987585"))

		actuator1Constrain=actuator1.addChild('actuator1Constrain')
		actuator1Constrain.addObject('MeshObjLoader', name="loader", filename="Robotino_new/Rototino_Bottom_X_aligned_Triangles.obj",  scale="1.0", triangulate=False, translation="-5 0 -5")
		actuator1Constrain.addObject('MeshTopology', src="@loader", name="topo")
		actuator1Constrain.addObject('MechanicalObject', name="cavity")
		actuator1Constrain.addObject('SurfacePressureActuator', tags='1', triangles="@topo.triangles", maxPressure="200000", minPressure="0")
		actuator1Constrain.addObject('AdaptiveBeamMapping', isMechanical=True, input="@../../DOFs", interpolation="@../BeamInterpolation", useCurvAbs=True, output="@cavity", mapForces="1", mapMasses="0")


		#Actuator 2

		actuator2=frames.addChild('actuator2')
		actuator2.addObject('MeshTopology', name="lines", lines="4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12")
		actuator2.addObject('BeamInterpolation', name="BeamInterpolation",  dofsAndBeamsAligned=False, radius="40", innerRadius="39.8",
					DOF0TransformNode0=("0.    28.752043    16.6    0.    0.0273396    0.    0.9996262 " + "0.    28.059223    16.2    0.    0.0273396    0.    0.9996262 " +
							    "0.    27.366403    15.8    0.    0.0273396    0.    0.9996262 " + "0.    26.673582    15.4    0.    0.0273396    0.    0.9996262 " +
							    "0.    25.980762    15.     0.    0.0273396    0.    0.9996262 " + "0.    25.287942    14.6    0.    0.0273396    0.    0.9996262 " +
							    "0.    24.595121    14.2    0.    0.0273396    0.    0.9996262 " + "0.    23.902301    13.8    0.    0.0273396    0.    0.9996262"),
					DOF1TransformNode1=("0.    28.059223    16.2    0.    0.0273396    0.    0.9996262 " + "0.    27.366403    15.8    0.    0.0273396    0.    0.9996262 " +
							    "0.    26.673582    15.4    0.    0.0273396    0.    0.9996262 " + "0.    25.980762    15.     0.    0.0273396    0.    0.9996262 " +
							    "0.    25.287942    14.6    0.    0.0273396    0.    0.9996262 " + "0.    24.595121    14.2    0.    0.0273396    0.    0.9996262 " +
							    "0.    23.902301    13.8    0.    0.0273396    0.    0.9996262 " + "0.    23.209481    13.4    0.    0.0273396    0.    0.9996262"))

		actuator2Constrain=actuator2.addChild('actuator2Constrain')
		actuator2Constrain.addObject('MeshObjLoader', name="loader", filename="Robotino_new/Rototino_Bottom_X_aligned_Triangles.obj",  scale="1.0",   triangulate=False, translation="-5 5 5")
		actuator2Constrain.addObject('MeshTopology', src="@loader", name="topo")
		actuator2Constrain.addObject('MechanicalObject', name="cavity")
		actuator2Constrain.addObject('SurfacePressureActuator', tags='2', triangles="@topo.triangles", maxPressure="200000", minPressure="0")
		actuator2Constrain.addObject('AdaptiveBeamMapping', isMechanical=True, input="@../../DOFs", interpolation="@../BeamInterpolation", useCurvAbs=True, output="@cavity", mapForces="1", mapMasses="0")

		#Actuator 3

		actuator3=frames.addChild('actuator3')
		actuator3.addObject('MeshTopology', name="lines", lines="4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12")
		actuator3.addObject('BeamInterpolation', name="BeamInterpolation",  dofsAndBeamsAligned=False, radius="40", innerRadius="39.8",
					DOF0TransformNode0=("0.  -28.752043    16.6    0.    0.0229892    0.    0.9997357 " + "0.  -28.059223    16.2    0.    0.0229892    0.    0.9997357 " +
    							    "0.  -27.366403    15.8    0.    0.0229892    0.    0.9997357 " + "0.  -26.673582    15.4    0.    0.0229892    0.    0.9997357 " +
							    "0.  -25.980762    15.     0.    0.0229892    0.    0.9997357 " + "0.  -25.287942    14.6    0.    0.0229892    0.    0.9997357 " +
							    "0.  -24.595121    14.2    0.    0.0229892    0.    0.9997357 " + "0.  -23.902301    13.8    0.    0.0229892    0.    0.9997357"),
					DOF1TransformNode1=("0.  -28.059223    16.2    0.    0.0229892    0.    0.9997357 " + "0.  -27.366403    15.8    0.    0.0229892    0.    0.9997357 " +
    							    "0.  -26.673582    15.4    0.    0.0229892    0.    0.9997357 " + "0.  -25.980762    15.     0.    0.0229892    0.    0.9997357 " +
    							    "0.  -25.287942    14.6    0.    0.0229892    0.    0.9997357 " + "0.  -24.595121    14.2    0.    0.0229892    0.    0.9997357 " +
    							    "0.  -23.902301    13.8    0.    0.0229892    0.    0.9997357 " + "0.  -23.209481    13.4    0.    0.0229892    0.    0.9997357"))

		actuator3Constrain=actuator3.addChild('actuator3Constrain')
		actuator3Constrain.addObject('MeshObjLoader', name="loader", filename="Robotino_new/Rototino_Bottom_X_aligned_Triangles.obj",  scale="1.0",   triangulate=False, translation="-5 -7 5")
		actuator3Constrain.addObject('MeshTopology', src="@loader", name="topo")
		actuator3Constrain.addObject('MechanicalObject', name="cavity")
		actuator3Constrain.addObject('SurfacePressureActuator', tags='3', triangles="@topo.triangles", maxPressure="200000", minPressure="0")
		actuator3Constrain.addObject('AdaptiveBeamMapping', isMechanical=True, input="@../../DOFs", interpolation="@../BeamInterpolation", useCurvAbs=True, output="@cavity", mapForces="1", mapMasses="0")

		#Actuator 4

		actuator4=frames.addChild('actuator4')
		actuator4.addObject('MeshTopology', name="lines", lines="12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20")
		actuator4.addObject('BeamInterpolation', name="BeamInterpolation",  dofsAndBeamsAligned=False, radius="40", innerRadius="39.8",
					DOF0TransformNode0=("0.    0.  -26.8    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -26.     0.  -0.0498137    0.    0.9987585 " +
    							    "0.    0.  -25.2    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -24.4    0.  -0.0498137    0.    0.9987585 " +
    							    "0.    0.  -23.6    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -22.8    0.  -0.0498137    0.    0.9987585 " +
    							    "0.    0.  -22.     0.  -0.0498137    0.    0.9987585 " + "0.    0.  -21.2    0.  -0.0498137    0.    0.9987585"),
					DOF1TransformNode1=("0.    0.  -26.     0.  -0.0498137    0.    0.9987585 " + "0.    0.  -25.2    0.  -0.0498137    0.    0.9987585 " +
    							    "0.    0.  -24.4    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -23.6    0.  -0.0498137    0.    0.9987585 " +
    							    "0.    0.  -22.8    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -22.     0.  -0.0498137    0.    0.9987585 " +
    							    "0.    0.  -21.2    0.  -0.0498137    0.    0.9987585 " + "0.    0.  -20.4    0.  -0.0498137    0.    0.9987585"))

		actuator4Constrain=actuator4.addChild('actuator4Constrain')
		actuator4Constrain.addObject('MeshObjLoader', name="loader", filename="Robotino_new/Rototino_Top_X_aligned_Triangles.obj",  scale="1.0",   triangulate=False, translation="-8 0 -5")
		actuator4Constrain.addObject('MeshTopology', src="@loader", name="topo")
		actuator4Constrain.addObject('MechanicalObject', name="cavity")
		actuator4Constrain.addObject('SurfacePressureActuator', tags='4', triangles="@topo.triangles", maxPressure="200000", minPressure="0")
		actuator4Constrain.addObject('AdaptiveBeamMapping', isMechanical=True, input="@../../DOFs", interpolation="@../BeamInterpolation", useCurvAbs=True, output="@cavity", mapForces="1", mapMasses="0")

		#Actuator 5

		actuator5=frames.addChild('actuator5')
		actuator5.addObject('MeshTopology', name="lines", lines="12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20")
		actuator5.addObject('BeamInterpolation', name="BeamInterpolation",  dofsAndBeamsAligned=False, radius="40", innerRadius="39.8",
					DOF0TransformNode0=("0.    23.209481    13.4    0.    0.0273396    0.    0.9996262 " + "0.    22.51666     13.     0.    0.0273396    0.    0.9996262 " +
    							    "0.    21.82384     12.6    0.    0.0273396    0.    0.9996262 " + "0.    21.13102     12.2    0.    0.0273396    0.    0.9996262 " +
    							    "0.    20.4382      11.8    0.    0.0273396    0.    0.9996262 " + "0.    19.745379    11.4    0.    0.0273396    0.    0.9996262 " +
    							    "0.    19.052559    11.     0.    0.0273396    0.    0.9996262 " + "0.    18.359739    10.6    0.    0.0273396    0.    0.9996262"),
					DOF1TransformNode1=("0.    22.51666     13.     0.    0.0273396    0.    0.9996262 " + "0.    21.82384     12.6    0.    0.0273396    0.    0.9996262 " +
    							    "0.    21.13102     12.2    0.    0.0273396    0.    0.9996262 " + "0.    20.4382      11.8    0.    0.0273396    0.    0.9996262 " +
    							    "0.    19.745379    11.4    0.    0.0273396    0.    0.9996262 " + "0.    19.052559    11.     0.    0.0273396    0.    0.9996262 " +
    							    "0.    18.359739    10.6    0.    0.0273396    0.    0.9996262 " + "0.    17.666918    10.2    0.    0.0273396    0.    0.9996262"))

		actuator5Constrain=actuator5.addChild('actuator5Constrain')
		actuator5Constrain.addObject('MeshObjLoader', name="loader", filename="Robotino_new/Rototino_Top_X_aligned_Triangles.obj",  scale="1.0",   triangulate=False, translation="4 5 3")
		actuator5Constrain.addObject('MeshTopology', src="@loader", name="topo")
		actuator5Constrain.addObject('MechanicalObject', name="cavity")
		actuator5Constrain.addObject('SurfacePressureActuator', tags='5', triangles="@topo.triangles", maxPressure="200000", minPressure="0")
		actuator5Constrain.addObject('AdaptiveBeamMapping', isMechanical=True, input="@../../DOFs", interpolation="@../BeamInterpolation", useCurvAbs=True, output="@cavity", mapForces="1", mapMasses="0")

		#Actuator 6

		actuator6=frames.addChild('actuator6')
		actuator6.addObject('MeshTopology', name="lines", lines="12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20")
		actuator6.addObject('BeamInterpolation', name="BeamInterpolation",  dofsAndBeamsAligned=False, radius="40", innerRadius="39.8",
					DOF0TransformNode0=("0.  -23.209481    13.4    0.    0.0229892    0.    0.9997357 " + "0.  -22.51666     13.     0.    0.0229892    0.    0.9997357 " +
    							    "0.  -21.82384     12.6    0.    0.0229892    0.    0.9997357 " + "0.  -21.13102     12.2    0.    0.0229892    0.    0.9997357 " +
    							    "0.  -20.4382      11.8    0.    0.0229892    0.    0.9997357 " + "0.  -19.745379    11.4    0.    0.0229892    0.    0.9997357 " +
    							    "0.  -19.052559    11.     0.    0.0229892    0.    0.9997357 " + "0.  -18.359739    10.6    0.    0.0229892    0.    0.9997357"),
					DOF1TransformNode1=("0.  -22.51666     13.     0.    0.0229892    0.    0.9997357 " + "0.  -21.82384     12.6    0.    0.0229892    0.    0.9997357 " +
    							    "0.  -21.13102     12.2    0.    0.0229892    0.    0.9997357 " + "0.  -20.4382      11.8    0.    0.0229892    0.    0.9997357 " +
    							    "0.  -19.745379    11.4    0.    0.0229892    0.    0.9997357 " + "0.  -19.052559    11.     0.    0.0229892    0.    0.9997357 " +
    							    "0.  -18.359739    10.6    0.    0.0229892    0.    0.9997357 " + "0.  -17.666918    10.2    0.    0.0229892    0.    0.9997357"))

		actuator6Constrain=actuator6.addChild('actuator6Constrain')
		actuator6Constrain.addObject('MeshObjLoader', name="loader", filename="Robotino_new/Rototino_Top_X_aligned_Triangles.obj",  scale="1.0",   triangulate=False, translation="4 -5 4")
		actuator6Constrain.addObject('MeshTopology', src="@loader", name="topo")
		actuator6Constrain.addObject('MechanicalObject', name="cavity")
		actuator6Constrain.addObject('SurfacePressureActuator', tags='6', triangles="@topo.triangles", maxPressure="200000", minPressure="0")
		actuator6Constrain.addObject('AdaptiveBeamMapping', isMechanical=True, input="@../../DOFs", interpolation="@../BeamInterpolation", useCurvAbs=True, output="@cavity", mapForces="1", mapMasses="0")

		#Next we specify the fixed frames in our geometric hideBehaviorModels
		fix=frames.addChild('fix')
		fix.addObject('FixedConstraint', name="FixedConstraint", indices="0 1 2 3 4")

		#The skinning to make the visual model deform according to the mechanical model
		MappedVisualModel=frames.addChild('MappedVisualModel')
		MappedVisualModel.addObject('MeshObjLoader', name="loader", filename="Robotino_Decim.obj",  translation="-128 0 93.25", scale="1.0")
		MappedVisualModel.addObject('MeshTopology', src="@loader")
		MappedVisualModel.addObject('OglModel', name="RobotinoVisu", ry="-40",  color="0.3 0.3 0.3 0.3")
		MappedVisualModel.addObject('SkinningMapping',  isMechanical=False, input="@../DOFs",  output="@RobotinoVisu", mapForces="1", mapMasses="0")
