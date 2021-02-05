from non_type_adf import *
from a1a_type_adf import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

A_m = 0.99
f_m = 1020  # 1020 or 400 Hz audio signal
modulation_index = 1

message_signal = dd*np.sin(2 * np.pi * f_m * time)

''' second method: am modulation on-off keying'''
# message_signal = np.sin(2*np.pi*f_m*time)

# message_signal_temp = np.zeros(len(time))
# for i in range(0, len(time)):
#     if i < len(time)*0.1:
#         message_signal_temp[i] = message_signal[i]
#     elif i < len(time)*0.4:
#         message_signal_temp[i] = 0
#     elif i < len(time)*0.7:
#         message_signal_temp[i] = message_signal[i]
#     elif i < len(time) * 0.8:
#         message_signal_temp[i] = 0
#     elif i < len(time) * 0.9:
#         message_signal_temp[i] = message_signal[i]
#     else:
#         message_signal_temp[i] = 0

am_modulation = 1 + modulation_index*message_signal
plt.plot(am_modulation)
a2a_lc = loop_cosine * am_modulation
a2a_ls = loop_sine * am_modulation
a2a_sns = sense * am_modulation

fig, ax = plt.subplots(3)
fig.suptitle('ADF A2A Input Signals')

ax[0].set_title("A2A loop cosine")
ax[0].plot(time, a2a_lc, color='lightblue')
ax[0].grid()

ax[1].set_title("A2A loop sine")
ax[1].plot(time, a2a_ls, color='teal')
ax[1].grid()

ax[2].set_title("A2A sense")
ax[2].plot(time, a2a_sns, color="purple")
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
