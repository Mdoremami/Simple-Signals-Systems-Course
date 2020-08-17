import matplotlib.pyplot as plt
import numpy as np
Left_lim=int(input('Please Enter The Interval Beginning Number:\n'))
Right_lim=int(input('Please Enter The Interval Ending Number:\n'))
t=np.arange(Left_lim,Right_lim+1)
def unit_step(a):
    u=np.zeros(len(a))
    for i in a:
        if a[i]>=0:
            u[i]=1
        else:
            u[i]=0
    return u


def unit_impulse(b):
    u=np.diff(unit_step(b))
    return u
u1= unit_step(t)
u2= unit_step(t-4)
u3= unit_step(t-8)
u4= unit_step(t-20)
d1=unit_impulse(t)
d2=unit_impulse(t-4)
d3=unit_impulse(t-8)
d4=unit_impulse(t-20)
f=u1-u2
g=np.add(np.subtract(np.multiply(t,u1),np.multiply(2*(t-4),u2)),np.multiply((t-8),u3))
x=d1-2*d2
y=np.multiply((0.9*t),(u1-u4))
v=np.multiply(np.cos(np.multiply(0.12*np.pi,t)),u1)

plt.stem(f)
plt.title('F')
plt.show()

plt.stem(g)
plt.title('G')
plt.show()

plt.stem(x)
plt.title('X')
plt.show()

plt.stem(y)
plt.title('Y')
plt.show()

plt.stem(v)
plt.title('V')
plt.show()

