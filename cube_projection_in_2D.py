import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider,Button
import numpy as np

#Rotation matrix

#Rotation in xy plane
def RXY(t):
    t = (t*2*np.pi)/360
    return np.array([[np.cos(t),-np.sin(t),0],[np.sin(t),np.cos(t),0],[0,0,1]])

#Rotation in yz plane
def RYZ(t):
    t = (t*2*np.pi)/360
    return np.array([[1,0,0],[0,np.cos(t),-np.sin(t)],[0,np.sin(t),np.cos(t)]])

#Rotation in xz plane
def RXZ(t):
    t = (t*2*np.pi)/360
    return np.array([[np.cos(t),0,-np.sin(t)],[0,1,0],[np.sin(t),0,np.cos(t)]])

#rotation angle in every plane
a_xy = 0
a_yz = 0
a_xz = 0

#graph
fig,ax = plt.subplots(figsize=(16, 9))
plt.subplots_adjust(left=0.001, bottom=0.1, right=0.6, top=0.9, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
#points = np.array([[1,1,-1],[-1,1,-1],[-1,-1,-1],[1,-1,-1],[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]])

#points arrange in that way so a cube can be produce without exctra line
#two parts 0-7 and 8-15
points = np.array([[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1],[1,-1,-1],[1,1,-1],[1,1,1],[1,-1,1],
                   [-1,1,-1],[-1,1,1],[-1,-1,1],[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,-1]])

#transpose matrix of points
pointsT = points.transpose()
rotated = pointsT

#widgets place
xy = plt.axes([0.60, 0.6, 0.35, 0.05])
yz = plt.axes([0.60, 0.5, 0.35, 0.05])
xz = plt.axes([0.60, 0.4, 0.35, 0.05])
button = plt.axes([0.68,0.3,0.20,0.04])

#widgets
sxy = Slider(xy, 'Rotation in XY', -2, 2, valinit=a_xy)
syz = Slider(yz, 'Rotation in YZ', -2, 2, valinit=a_yz)
sxz = Slider(xz, 'Rotation in XZ', -2, 2, valinit=a_xz)
breset = Button(button,'Reset')

#initilize ploting
p, = ax.plot([],[],marker='o',color = 'C0')
q, = ax.plot([],[],marker='o',color = 'C0')

#animation function
def animate(val):
    global rotated

    #rotate the cube
    rotated = RXY(a_xy) @ rotated
    rotated = RYZ(a_yz) @ rotated
    rotated = RXZ(a_xz) @ rotated

    # projected matrix initilize with 0
    projected = np.zeros((2, 16))

    #project the point in 2d plane
    for i in range(16):
        # distance
        d = 3

        # point's projection ratio
        w = 1 / (d - rotated[2, i])

        # projection matrix
        PXY = np.array([[w, 0, 0], [0, w, 0]])

        # projected matrix
        projected[:, i] = PXY @ rotated[:, i]

    #set the size of cube
    projected = 2* projected

    # set points in graph
    p.set_data(projected[0,:8],projected[1,:8])
    q.set_data(projected[0, 8:], projected[1, 8:])

#animation
anim = FuncAnimation(fig, animate,frames=400, interval=5)

#execute when button is pressed
def reset(val):
    global rotated
    global pointsT
    global sxy
    global syz
    global sxz
    #reset every variable
    rotated = pointsT
    sxy.valinit = syz.valinit = sxz.valinit = 0
    sxy.reset()
    syz.reset()
    sxz.reset()
    fig.canvas.draw_idle()

#execute when value of slider is change
def update(val):
    global a_xy
    global a_yz
    global a_xz

    # set slider's value to the variables
    a_xy = sxy.val
    a_yz = syz.val
    a_xz = sxz.val

    fig.canvas.draw_idle()


sxy.on_changed(update)
syz.on_changed(update)
sxz.on_changed(update)
breset.on_clicked(reset)


plt.show()