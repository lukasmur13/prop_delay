import numpy as np
import matplotlib.pyplot as plt

# Constants
R_E = 6371  # Earth's radius in km
h = 600     # Satellite altitude in km
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M = 5.972e24  # Mass of the Earth in kg
el_angle_deg = 0  # Elevation angle in degree

angle_list = []
radial_speed_list = []

while el_angle_deg <= 180:
  # Convert elevation angle to radians
  el_angle_rad = np.radians(el_angle_deg)

  # Satellite's orbital velocity
  r = R_E + h  # Distance from Earth's center to satellite in km
  r_m = r * 1000  # Convert to meters
  v = np.sqrt(G * M / r_m)  # Orbital velocity in m/s
  v_km_s = v / 1000  # Convert to km/s

  # Compute the slant range
  angle_term = (np.pi / 2) - el_angle_rad - np.arcsin(R_E * np.sin((np.pi / 2) + el_angle_rad) / (R_E + h))
  d = np.sqrt(R_E**2 + (R_E + h)**2 - 2 * R_E * (R_E + h) * np.cos(angle_term))

  # Calculate the radial speed
  # Here, we assume a small time interval dt to approximate the derivative
  dt = 1  # time step in seconds
  angle_change = v_km_s * dt / r  # Change in angle per second

  # Recompute slant range for the next time step
  new_el_angle_rad = el_angle_rad + angle_change
  new_angle_term = (np.pi / 2) - new_el_angle_rad - np.arcsin(R_E * np.sin((np.pi / 2) + new_el_angle_rad) / (R_E + h))
  new_d = np.sqrt(R_E**2 + (R_E + h)**2 - 2 * R_E * (R_E + h) * np.cos(new_angle_term))

  # Radial speed is the change in slant range over time
  radial_speed = (new_d - d) / dt

  angle_list.append(el_angle_deg)
  radial_speed_list.append(radial_speed)

  el_angle_deg += 1

plt.figure(figsize=(10, 6))
plt.plot(angle_list, radial_speed_list)
plt.title('Radial Speed of Satellite (LEO, 600 km)')
plt.xlabel('Elevation Angle (degrees)')
plt.ylabel('Radial Speed (km/s)')
plt.grid(True)
plt.show()