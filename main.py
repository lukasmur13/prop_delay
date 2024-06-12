import numpy as np
import math
import matplotlib.pyplot as plt

r_earth = 6371
r_GEO = 35786
r_MEO = 8063
r_LEO_500 = 500
r_LEO_800 = 800
radius_array = [[r_GEO, "GEO"], [r_MEO, "MEO"], [r_LEO_500, "LEO"], [r_LEO_800, "LEO"]]



for i in range(len(radius_array)):
  el_angle = 0
  angle_list = []
  d_list = []
  
  while el_angle <= 180:
    el_angle_rad = math.radians(el_angle)
    d = np.sqrt(r_earth**2 + (r_earth + radius_array[i][0])**2 - 2 * r_earth * (r_earth + radius_array[i][0]) * np.cos(np.pi/2 - el_angle_rad))
    angle_list.append(el_angle)
    d_list.append(d)
    el_angle = el_angle + 5

  if i == 3:
    plt.subplot(1, 3, i)
  else:
    plt.subplot(1, 3, i + 1)
    plt.grid()
    plt.yticks(np.arange(min(d_list), max(d_list), 500))

  plt.plot(angle_list, d_list)
  plt.title(radius_array[i][1])

plt.show()