import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor


def onclick(event):
    x1, y1 = event.xdata, event.ydata
    print(x1, y1)


'''
Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
AM Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)

Loop Cosine V1=A.cos(theta).cos(2*pi*f_c*t + phase_lc)
Loop Sine   V2=A.sin(theta).cos(2*pi*f_c*t + phase_ls)
Sense       V3=B.sin(2*pi*f_c*t + phase_sns)
'''

A = 0.99  # float(input('Enter the carrier amplitude of loop cos & sine: '))
B = 0.99  # float(input('Enter the carrier amplitude of sense: '))
theta = 120  # float(input("Enter the angle between aircraft and ground station(theta): "))
f_c = 1e6  # float(input("Enter the carrier frequency: "))

theoretical_phase = 90 - 2*np.rad2deg(np.arctan(f_c/577000))
phase_lc = np.deg2rad(0)
phase_ls = np.deg2rad(0)
phase_sns = np.deg2rad(0) + np.deg2rad(theoretical_phase)

f_s = 15.625e6  # sampling frequency
t_s = 1/f_s
T = 400e-3
N = int(T/t_s)
time = np.arange(0, 1, t_s)

loop_cosine = A * np.cos(np.deg2rad(theta)) * np.cos(2*np.pi*f_c*time + phase_lc)
loop_sine = A * np.sin(np.deg2rad(theta)) * np.cos(2*np.pi*f_c*time + phase_ls)
sense = B * np.sin(2*np.pi*f_c*time + phase_sns)

fig, ax = plt.subplots(3)
fig.suptitle('ADF NON Input Signals')

ax[0].set_title("loop cosine")
ax[0].plot(loop_cosine, 'lightblue')
ax[0].grid()

ax[1].set_title("loop sine")
ax[1].plot(loop_sine, 'teal')
ax[1].grid()

ax[2].set_title("sense")
ax[2].plot(sense, color="purple")
ax[2].grid()

plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
figs = plt.gcf()
figs.set_size_inches(16, 9)

cursor0 = Cursor(ax[0], horizOn=True, vertOn=True, color='grey', linestyle='dotted', linewidth=1.0)
cursor1 = Cursor(ax[1], horizOn=True, vertOn=True, color='grey', linestyle='dotted', linewidth=1.0)
cursor2 = Cursor(ax[2], horizOn=True, vertOn=True, color='grey', linestyle='dotted', linewidth=1.0)
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
