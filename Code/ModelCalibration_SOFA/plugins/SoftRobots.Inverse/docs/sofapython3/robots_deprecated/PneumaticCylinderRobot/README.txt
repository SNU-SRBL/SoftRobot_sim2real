			***REQUIREMENT***

SOFA-EXTERNAL
	-SOFA-EXTERNAL_SPARSE
	-SOFA-EXTERNAL_METIS 


**For the Control**

To use the SerialPortBridgePressureControl please download vrpn --> http://www.cs.unc.edu/Research/vrpn/downloads/
Build vrpn:

./configure
make
make install

Don't forget the "make install" step.
In the cmake-gui, activate the option SOFTROBOTS-PRESSURECYLINDERROBOT_CONTROLLER


