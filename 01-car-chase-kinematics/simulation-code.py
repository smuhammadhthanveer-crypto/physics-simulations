Web VPython 3.2
g1 = graph(title="kinematics", fast=True)
f1 = gcurve(color=color.blue) 
f2 = gcurve(color=color.red) 
xA = 0.5 #m 
xB = 0 #m 
vA = 0.45 #m/s 
vB = 0 
aB = 0.2 #m/s^2 
t = 0 
dt = 0.01
while xA>=xB: 
    vB = vB+aB*dt 
    xB = xB+vB*dt 
    xA = xA+vA*dt 
    t = t+dt 
    f1.plot(t,xA) 
    f2.plot(t,xB)
print("time and position where both cars meet are at:", xA, " m at ", t, " s")
