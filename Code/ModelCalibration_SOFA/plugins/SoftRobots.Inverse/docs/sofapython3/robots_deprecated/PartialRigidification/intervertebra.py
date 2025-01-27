from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

global degree
degree = 3
def evalBezier3(dim, cpOrig, nPts, rBegin, rEnd, offset):
	curve = []
	cp = [cpOrig[i] for i in range(len(cpOrig))]
	cp[dim-1] = cp[dim-1]*rBegin
	cp[2*dim-1] = cp[2*dim-1]*rBegin
	cp[-1] = cp[-1]*rEnd
	cp[-(dim+1)] = cp[-(dim+1)] * rEnd
	
	global degree
	nSegment = ((len(cp)//dim)-1)//degree
	#ptsPerSegment = nPts/
	#print "len(cp) = " + str(len(cp))
	#print "nSegment = " + str(nSegment)
	
	for p in range(nPts):
		segment = int((p*nSegment)/(nPts))
		t = ((p*nSegment)/(nPts-1)) - segment
		
		spanStart = segment*degree
		spanEnd = spanStart + degree + 1
		span = cp[3*spanStart:3*spanEnd]
		p0 = span[0:dim]
		p1 = span[dim:2*dim]
		p2 = span[2*dim:3*dim]
		p3 = span[3*dim:4*dim]
	
		print("p" , p, "t = ", str(t) ," ; segment = " ,str(segment))
		#print str(p0) + ", " + str(p1) + ", " + str(p2) + ", " + str(p3)
		P = [0]*dim
		for d in range(dim):
			P[d] = ((1-t)**3)*p0[d] + (3*t*((1-t)**2))*p1[d] + 3*((1-t)*(t**2))*p2[d] + (t**3)*p3[d]
			
		#print 'P'+str(p) + " : " + str(P)

		P[0] = P[0] + offset
		curve = curve + P
	
	#for points in range(0, len(cpOrig)-degree, 3*dim) :
		#span = cp[points:points+4*dim]
		#p0 = span[0:dim]
		#p1 = span[dim:2*dim]
		#p2 = span[2*dim:3*dim]
		#p3 = span[3*dim:4*dim]

		#for i in range(nPts) :
			#t = i/(nPts-1)
			#P = [0]*dim
			#for d in range(dim):
				#P[d] = ((1-t)**3)*p0[d] + (3*t*((1-t)**2))*p1[d] + 3*((1-t)*(t**2))*p2[d] + (t**3)*p3[d]

			#P[0] = P[0] + offset
			#curve = curve + P
				
		
	return curve


#def evalBezier3(dim, cpOrig, nPts, rBegin, rEnd, offset):
	##print(list(range(0, len(cpOrig)-degree, 3*dim)))
	#curve = []
	#cp = [cpOrig[i] for i in range(len(cpOrig))]
	#cp[dim-1] = cp[dim-1]*rBegin
	#cp[2*dim-1] = cp[2*dim-1]*rBegin
	#cp[-1] = cp[-1]*rEnd
	#cp[-(dim+1)] = cp[-(dim+1)] * rEnd
	#for points in range(0, len(cpOrig)-degree, 3*dim) :
		##print(list(range(span, span + 4*dim)))
		#span = cp[points:points+4*dim]
		##print(cp)
		#p0 = span[0:dim]
		#p1 = span[dim:2*dim]
		#p2 = span[2*dim:3*dim]
		#p3 = span[3*dim:4*dim]
		#print(p0, p1, p2, p3)
		##p0[2] = p0[2]*rBegin
		##p1[2] = p1[2]*rBegin
		
		#for i in range(nPts) :
			#t = i/(nPts-1)
			#P = [0]*dim
			#for d in range(dim):
				#P[d] = ((1-t)**3)*p0[d] + (3*t*((1-t)**2))*p1[d] + 3*((1-t)*(t**2))*p2[d] + (t**3)*p3[d]

			#P[0] = P[0] + offset
			#curve = curve + P
				
		##p0 = cp[9:12]
		##p1 = cp[12:15]
		##p2 = cp[15:18]
		##p3 = cp[18:21]
		
		##p2[2] = p2[2]*rEnd
		##p3[2] = p3[2]*rEnd
		
		
		##for i in range(nPts) :
			##t = i/(nPts-1)
			##P = [0]*dim
			##for d in range(dim):
				##P[d] = ((1-t)**3)*p0[d] + (3*t*((1-t)**2))*p1[d] + 3*((1-t)*(t**2))*p2[d] + (t**3)*p3[d]

			
			##P[0] = P[0] + offset
			##curve = curve + P

		##for i in range(nPts) :
			##t = i/(nPts-1)
			##x = ((1-t)**3)*p0[0] + 3*(t*(1-t)**3)*p1[0] + 3*(t**2*(1-t))*p2[0] + t**3*p3[0]
			##y = ((1-t)**3)*p0[1] + 3*(t*(1-t)**3)*p1[1] + 3*(t**2*(1-t))*p2[1] + t**3*p3[1]
			##z = ((1-t)**3)*p0[2] + 3*(t*(1-t)**3)*p1[2] + 3*(t**2*(1-t))*p2[2] + t**3*p3[2]
			
			##curve = curve + [x, y, z]
		
	#return curve


def genRadius(a, b, n):
	return [a+i*((b-a)/n) for i in range(n+1)]

controlPoints = [5.2289833, 0, -13.032512, 16.331092, 0, -12.243574,  4.3410441, 0, -30.59501, 12.685578, 0, -30.002031, 20.146103, 0, -30.59501, 8.1560552, 0, -12.243574, 19.258164, 0, -13.032512]

#controlPoints = [-2, 0, 2,
				 #0, 0, 2,
				 #-1, 0, 0,
				 #0, 0, 0,
				 #1, 0, 0,
				 #0, 0, 2,
				 #2, 0, 2]
				 
#controlPoints = [0, 0, 2, 2, 0, 2, 1, 0, 0, 3, 0, 0, 5, 0, 0, 4, 0, 2, 6, 0, 2]



nPtsPerVertebra = 67
xOffset = max(controlPoints[::3]) - min(controlPoints[::3])
yOffset = -39

for i in range(2,len(controlPoints),3):
	controlPoints[i] = controlPoints[i] - yOffset

vertebraRadius = max(controlPoints[2::3]) - min(controlPoints[2::3])
nVertebra = 1
radii = genRadius(1, 0.1, nVertebra)
print(controlPoints)
cv = []
for i in range(nVertebra):
	cv = cv + evalBezier3(3, controlPoints, nPtsPerVertebra, radii[i], radii[i+1], i*xOffset)
#cv = cv + evalBezier3(3, controlPoints[9:21], 60, 1, 1)



fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
#ax.set_xticks(range(0,10,1)) 
#ax.set_zticks(range(-20,10,1)) 

ax.set_xlim3d([min(cv[::3]), max(cv[::3])])
ax.set_zlim3d(0, - yOffset)
ax.plot(cv[0:len(cv):3], cv[1:len(cv):3], cv[2:len(cv):3])
#ax.plot(cv[0:len(cv):3], cv[1:len(cv):3], cv[2:len(cv):3])
#ax.plot(controlPoints[0:len(controlPoints):3], controlPoints[1:len(controlPoints):3], controlPoints[2:len(controlPoints):3])
ax.pbaspect = [1.0, 1.0, 1]
plt.tight_layout()
plt.show()