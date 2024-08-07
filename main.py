import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# Constants
c_kilometers_per_msecond = 299.792458
r_earth = 6371
r_GEO = 35786
r_MEO = 8063
r_LEO_500 = 500
r_LEO_800 = 800
radius_array = [[r_GEO, "GEO", "Geostationary Orbit"], [r_MEO, "MEO", "8063 km"], [r_LEO_500, "LEO", "500 km"], [r_LEO_800, "LEO", "800 km"]]
print("d: ", np.sqrt((r_earth + r_MEO)**2 - r_earth**2))

# Create figure and subplots
fig, ax = plt.subplots(3)
#figsize=(20, 14)
# Loop through each satellite orbit
for i in range(len(radius_array)):
    el_angle = 0
    angle_list = []
    d_list = []
    while el_angle <= 180:
        el_angle_rad = math.radians(el_angle)
        #d = np.sqrt(r_earth**2 + (r_earth + radius_array[i][0])**2 - 2 * r_earth * (r_earth + radius_array[i][0]) * np.cos(np.pi/2 - el_angle_rad))
        #d = np.sqrt((r_earth * (np.cos(el_angle_rad)))**2 + (r_earth + radius_array[i][0])**2 - r_earth**2) - r_earth * np.cos(el_angle_rad)
        #d = np.sqrt((r_earth + radius_array[i][0])**2 - (r_earth * (np.cos(el_angle_rad)))**2) - r_earth * np.sin(el_angle_rad)
        d = np.sqrt(r_earth**2 + (r_earth + radius_array[i][0])**2 - 2 * r_earth * (r_earth + radius_array[i][0]) * np.cos(np.pi/2 - el_angle_rad - np.arcsin(r_earth * np.sin(np.pi/2 + el_angle_rad) / (r_earth + radius_array[i][0]))))
        angle_list.append(el_angle)
        d_list.append(d)
        el_angle += 5
    if i == 3:
      # Plot distance
      ax[2].plot(angle_list, d_list, label=radius_array[i][2])
      ax[2].set_title("LEO")
      ax[2].set_ylabel('Distance (km)')
      ax[2].grid(True)
      ax[2].legend(loc="lower left")

    else:
      # Plot distance
      ax[i].plot(angle_list, d_list, label=radius_array[i][2])
      ax[i].set_title(radius_array[i][1])
      ax[i].set_ylabel('Distance (km)')
      ax[i].grid(True)
      ax[i].legend(loc="lower left")

      # Set y-limits and y-ticks
      y_min = min(d_list)
      y_max = max(d_list) + 200
      if i == 2:
        y_max = max(d_list) + 1000
      y_ticks = np.arange(y_min, y_max, 1000)
      ax[i].set_yticks(y_ticks)
      ax[i].set_ylim(y_min, y_max)

      # Create a second y-axis for propagation delay
      ax2 = ax[i].twinx()
      ax2.set_ylabel('Propagation Delay (ms)')
      ax2.tick_params(axis='y')

      # Scale the second y-axis
      ax2.set_ylim(ax[i].get_ylim())
      ax2.set_yticks(ax[i].get_yticks())
      ax2.set_yticklabels(np.array(ax[i].get_yticks()) / c_kilometers_per_msecond)
      labels2 = [item.get_text() for item in ax2.get_yticklabels()]
      ax2.set_yticklabels([str(round(float(label), 2)) for label in labels2])

# Set x-axis label for the bottom subplot
ax[-1].set_xlabel('Elevation Angle (degrees)')

# Adjust layout for clarity

plt.tight_layout()
plt.show()
