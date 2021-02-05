from non_type_adf import *
from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt
import numpy as np


''' first method: ID declaration as dot-dash-dot = R '''
bit_arr = np.array([1, 0, 1, 1, 1, 0, 0, 0, 1, 0])
samples_per_bit = f_s/bit_arr.size
dd = np.repeat(bit_arr, samples_per_bit)

a1a_lc = dd*loop_cosine
a1a_ls = dd*loop_sine
a1a_sns = dd*sense

''' second method: ID declaration as on-off keying '''
# a1a_lc = np.zeros(len(time))
# a1a_ls = np.zeros(len(time))
# a1a_sns = np.zeros(len(time))
# for i in range(1, len(time)):
#     if i < len(time)*0.3:
#         a1a_lc[i] = loop_cosine[i]
#         a1a_ls[i] = loop_sine[i]
#         a1a_sns[i] = sense[i]
#     elif i < len(time)*0.4:
#         a1a_lc[i] = 0
#         a1a_ls[i] = 0
#         a1a_sns[i] = 0
#     elif i < len(time)*0.5:
#         a1a_lc[i] = loop_cosine[i]
#         a1a_ls[i] = loop_sine[i]
#         a1a_sns[i] = sense[i]
#     elif i < len(time) * 0.6:
#         a1a_lc[i] = 0
#         a1a_ls[i] = 0
#         a1a_sns[i] = 0
#     elif i < len(time) * 0.7:
#         a1a_lc[i] = loop_cosine[i]
#         a1a_ls[i] = loop_sine[i]
#         a1a_sns[i] = sense[i]
#     elif i < len(time) * 0.8:
#         a1a_lc[i] = 0
#         a1a_ls[i] = 0
#         a1a_sns[i] = 0
#     elif i < len(time) * 0.9:
#         a1a_lc[i] = loop_cosine[i]
#         a1a_ls[i] = loop_sine[i]
#         a1a_sns[i] = sense[i]
#     else:
#         a1a_lc[i] = 0
#         a1a_ls[i] = 0
#         a1a_sns[i] = 0


fig, ax = plt.subplots(3)
fig.suptitle('ADF A1A Input Signals')

ax[0].set_title("A1A loop cosine")
ax[0].plot(time, a1a_lc, color='lightblue')
ax[0].grid()

ax[1].set_title("A1A loop sine")
ax[1].plot(time, a1a_ls, color='teal')
ax[1].grid()

ax[2].set_title("A1A sense")
ax[2].plot(time, a1a_sns, color="purple")
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
