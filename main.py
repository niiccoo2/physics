import matplotlib.pyplot as plt
from math import sin, cos, radians

def line(slope: float, y_intercept: float, detail: int = 20):
    y = 0
    x_list = []
    y_list = []
    for x in range(detail):
        y = (slope*x)+y_intercept
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list

def projectile_motion(v_i: float, angle: float, g: float = -9.81, detail: int = 20):
    rad = radians(angle)
    v_x_i = v_i*cos(rad)
    v_y_i = v_i*sin(rad)

    t_total = v_y_i/(.5*abs(g))
    amount = t_total/detail

    x_list = []
    y_list = []
    t=0
    while t <= t_total:
        y = (v_y_i*t)+(.5*g*(t*t))
        x = v_x_i*t
        x_list.append(x)
        y_list.append(y)
        t = t+amount
    print(x_list)
    print(y_list)
    return x_list, y_list

v_i = input('v_i (m/s): ')
angle = input('Angle (degrees): ')
g = input('Gravity (m/s^2): ')
detail = input('Detail: ')

x_list, y_list = projectile_motion(v_i=float(v_i), angle=float(angle), g=float(g), detail=int(detail))

plt.plot(x_list, y_list)
plt.ylabel('Height (m)')
plt.xlabel('Distance (m)')
plt.show()