import numpy as np
import matplotlib.pyplot as plt

def r(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

fig,ax = plt.subplots()
plt.subplots_adjust(left=0, bottom=0., right=1, top=1, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim(-83,83)
ax.set_ylim(-40,40)

ys = (-(26.5 - np.sqrt(15.5**2 + 9**2))/2)
xs = ys*np.sqrt(3)

points = np.array([[xs-7.75,xs-15.5,xs-15.5,xs-7.75,xs+7.5,xs,xs,xs-7.75,xs-7.75],[ys+4.5,ys+9,ys+35.5,ys+40,ys+30.8,ys+26.5,ys,ys+4.5,ys+40]])
ax.plot(points[0],points[1],'black')

for i in range(6):
    points = r(np.pi/3)@points
    ax.plot(points[0],points[1],'black')

#ax.plot(0,0,marker = '+')
plt.show()