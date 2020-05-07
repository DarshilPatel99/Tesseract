import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider ,Button
import numpy as np

#Rotation matrix

#Rotation in xy plane
def RXY(t):
    t = (t*2*np.pi)/360
    return np.array([[np.cos(t),-np.sin(t),0,0],[np.sin(t),np.cos(t),0,0],[0,0,1,0],[0,0,0,1]])

#Rotation in yz plane
def RYZ(t):
    t = (t*2*np.pi)/360
    return np.array([[1,0,0,0],[0,np.cos(t),-np.sin(t),0],[0,np.sin(t),np.cos(t),0],[0,0,0,1]])

#Rotation in xz plane
def RXZ(t):
    t = (t*2*np.pi)/360
    return np.array([[np.cos(t),0,-np.sin(t),0],[0,1,0,0],[np.sin(t),0,np.cos(t),0],[0,0,0,1]])

#Rotation in xw plane
def RXW(t):
    t = (t*2*np.pi)/360
    return np.array([[np.cos(t),0,0,-np.sin(t)],[0,1,0,0],[0,0,1,0],[np.sin(t),0,0,np.cos(t)]])

#Rotation in yw plane
def RYW(t):
    t = (t*2*np.pi)/360
    return np.array([[1,0,0,0],[0,np.cos(t),0,-np.sin(t)],[0,0,1,0],[0,np.sin(t),0,np.cos(t)]])

#Rotation in zw plane
def RZW(t):
    t = (t*2*np.pi)/360
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,np.cos(t),-np.sin(t)],[0,0,np.sin(t),np.cos(t)]])

#rotation angle in every plane
a_xy = 0
a_yz = 0
a_xz = 0
a_xw = 0
a_yw = 0
a_zw = 0

#graph
fig = plt.figure(figsize=(16, 9))
ax = plt.axes(projection='3d')
plt.subplots_adjust(left=0, bottom=0, right=0.5, top=1, wspace=0, hspace=0)
ax.set_axis_off()
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-4,4)

#points = np.array([[1,1,1,1],[-1,1,1,1],[-1,-1,1,1],[1,-1,1,1],[1,1,-1,1],[-1,1,-1,1],[-1,-1,-1,1],[1,-1,-1,1],[1,1,1,-1],[-1,1,1,-1],[-1,-1,1,-1],[1,-1,1,-1],[1,1,-1,-1],[-1,1,-1,-1],[-1,-1,-1,-1],[1,-1,-1,-1]])

#points arrange in that way so a tasserect can be produce without exctra line
#four parts 0-8 , 9-17 , 18-26 , 27-35
points = np.array([[1,1,1,-1],[-1,1,1,-1],[-1,-1,1,-1],[1,-1,1,-1],[1,-1,1,1],[-1,-1,1,1],[-1,1,1,1],[1,1,1,1],[1,1,1,-1],
                   [1,1,-1,-1],[1,1,1,-1],[1,-1,1,-1],[1,-1,-1,-1],[1,-1,-1,1],[1,-1,1,1],[1,1,1,1],[1,1,-1,1],[1,1,-1,-1],
                   [-1,1,-1,-1],[1,1,-1,-1],[1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,1],[1,-1,-1,1],[1,1,-1,1],[-1,1,-1,1],[-1,1,-1,-1],
                   [-1,1,1,-1],[-1,1,-1,-1],[-1,-1,-1,-1],[-1,-1,1,-1],[-1,-1,1,1],[-1,-1,-1,1],[-1,1,-1,1],[-1,1,1,1],[-1,1,1,-1]])

#transpose matrix of points
pointsT = points.transpose()
rotated = pointsT

#widgets place
xy = plt.axes([0.70, 0.9, 0.25, 0.05])
yz = plt.axes([0.70, 0.8, 0.25, 0.05])
xz = plt.axes([0.70, 0.7, 0.25, 0.05])
xw = plt.axes([0.70, 0.6, 0.25, 0.05])
yw = plt.axes([0.70, 0.5, 0.25, 0.05])
zw = plt.axes([0.70, 0.4, 0.25, 0.05])
button = plt.axes([0.78,0.3,0.10,0.04])

#widgets
sxy = Slider(xy, 'Rotation in XY', -2, 2, valinit=a_xy)
syz = Slider(yz, 'Rotation in YZ', -2, 2, valinit=a_yz)
sxz = Slider(xz, 'Rotation in XZ', -2, 2, valinit=a_xz)
sxw = Slider(xw, 'Rotation in XW', -2, 2, valinit=a_xw)
syw = Slider(yw, 'Rotation in YW', -2, 2, valinit=a_yw)
szw = Slider(zw, 'Rotation in ZW', -2, 2, valinit=a_zw)
breset = Button(button,'Reset')

#initilize ploting
p, = ax.plot([],[],[],color = 'C0',linewidth=4)
q, = ax.plot([],[],[],color = 'C0',linewidth=4)
r, = ax.plot([],[],[],color = 'C0',linewidth=4)
s, = ax.plot([],[],[],color = 'C0',linewidth=4)

#animation function
def animate(val):
    global rotated

    # rotate the cube
    rotated = RXY(a_xy) @ rotated
    rotated = RYZ(a_yz) @ rotated
    rotated = RXZ(a_xz) @ rotated
    rotated = RXW(a_xw) @ rotated
    rotated = RYW(a_yw) @ rotated
    rotated = RZW(a_zw) @ rotated

    # projected matrix initilize with 0
    projected = np.zeros((3,36))

    # project the point in 2d plane
    for i in range(36):

        # distance
        d = 3

        # point's projection ratio
        w = 1/(d - rotated[3,i])

        # projection matrix
        PXYZ = np.array([[w, 0, 0, 0], [0, w, 0, 0], [0, 0, w, 0]])

        # projected matrix
        projected[:,i] = PXYZ @ rotated[:,i]

    #set the size of tasserect
    projected = 8* projected

    # set points in graph
    p.set_xdata(projected[0,:9])
    p.set_ydata(projected[1, :9])
    p.set_3d_properties(projected[2, :9])
    q.set_xdata(projected[0,9:18])
    q.set_ydata(projected[1, 9:18])
    q.set_3d_properties(projected[2, 9:18])
    r.set_xdata(projected[0,18:27])
    r.set_ydata(projected[1, 18:27])
    r.set_3d_properties(projected[2, 18:27])
    s.set_xdata(projected[0,27:])
    s.set_ydata(projected[1, 27:])
    s.set_3d_properties(projected[2, 27:])

#animation
anim = FuncAnimation(fig, animate,frames=400, interval=5)

#execute when button is pressed
def reset(val):
    global rotated
    global pointsT
    global sxy
    global syz
    global sxz
    global sxw
    global syw
    global szw

    # reset every variable
    rotated = pointsT
    sxy.valinit = syz.valinit = sxz.valinit = sxw.valinit = syw.valinit = szw.valinit = 0
    sxy.reset()
    syz.reset()
    sxz.reset()
    sxw.reset()
    syw.reset()
    szw.reset()
    fig.canvas.draw_idle()

#execute when value of slider is change
def update(val):
    global a_xy
    global a_yz
    global a_xz
    global a_xw
    global a_yw
    global a_zw

    # set slider's value to the variables
    a_xy = sxy.val
    a_yz = syz.val
    a_xz = sxz.val
    a_xw = sxw.val
    a_yw = syw.val
    a_zw = szw.val

    fig.canvas.draw_idle()


sxy.on_changed(update)
syz.on_changed(update)
sxz.on_changed(update)
sxw.on_changed(update)
syw.on_changed(update)
szw.on_changed(update)
breset.on_clicked(reset)

plt.show()