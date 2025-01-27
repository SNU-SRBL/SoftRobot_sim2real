"""
    This file aims to initialize the main parameters of the scene
"""

# Simulation parameters
hrDT_value = 0.001               # Time step for the high frequency loop
lrDT_value = 0.02               # Time step for the low frequency loop
useOmni = False                 # Set the parameter to True if you use the haptic device

# Instrument parameters
m = 0.3                         # Mass (in kg)
K = 6e4                         # Spring's stifness (in N.m-1)
L = 0.1                         # Length without hooke(in m)
initPos = '0 0.25 0'            # Initial position (in m)
solver = 'SparseLDLSolver'      # Solver
Rm_HR = 1e-1                     # Rayleigh mass of HR intrument
Rk_HR = 1e-5                     # Rayleigh stifness of HR intrument
Rm_LR = 1e-1                     # Rayleigh mass of proxy
Rk_LR = 1e-5                     # Rayleigh stifness of proxy

# Cylinder parameters
D = 0.05                        # Diameter (in m)
M = 0.0107                         # Mass (in kg)
E = 129000                       # Young's modulus (in Pa)
v = 0.45                        # Poisson's ratio (]-1;0.5[)
Solver = 'SparseLDLSolver'       # Solver
RM_HR = 1e-0
RK_HR = 1e-2
RM_LR = 1e-0
RK_LR = 1e-2

# printLogs
printATAL = 0                   # AsynchroThreadedAnimationLoop
printAHRCS = 0                  # AsynchroHighRateConstraintSolver
printALRAL = 0                  # AsynchroLowRateAnimationLoop
printALRCS = 0                  # AsynchroLowRateConstraintSolver

# Coding parameters
#path = '/home/sofa/Sofa/applications-dev/plugins/AsynchroHaptics/scenes/IROS2013/'
#path2 = '/home/sofa/Desktop/Valerian/Python/scene1/'
path = 'C:\Users\SOFA\Desktop\Valerian\Scenes\_data/'

# Others
HRTag = 'highRate'
LRTag = 'lowRate'
scaleCylinder = str(D*0.5) + ' ' + str(D*0.5) + ' ' + str(D*0.5)
scaleInstrument = str(L/6) + ' ' + str(L/6) + ' ' + str(L/6)
