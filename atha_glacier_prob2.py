"""
atha_glacier_prob2.py

This script ...

@author: NAME - DD.MM.YYYY
"""

# Import NumPy
import numpy as np
import matplotlib.pyplot as plt

# Open and read input file
data = np.loadtxt(fname='atha_glacier_velo.txt', delimiter=',')

# Create zeros arrays
data_depth = np.zeros(len(data))  # Create empty array for data depths [m]
data_z = np.zeros(len(data))      # Create empty array for data elevations from bed [m]
data_u_ma = np.zeros(len(data))   # Create empty array for data velocities [m/a]
data_u_ms = np.zeros(len(data))   # Create empty array for data velocities [m/s]

# Loop over lines in file and split into different variables
for line in data:
    data_depth[linecount] = line[0]
    data_z[linecount] = line[1]
    data_u_ma[linecount] = line[2]
    data_u_ms[linecount] = line[3]

#--- User-defined variables
a =                    # Viscosity [1/(Pa**3.0 s)]
h =                    # Flow height
z =                    # Range of elevation values in flow for velocity calculation
data_umax =            # Velocity at top of flow
data_ub =              # Velocity at base of flow
n_prof =               # Number of velocity profiles to calculate

# Equations
u = np.zeros([n_prof,len()])
n = 0

# Velocity profile for a Newtonian or non-Newtonian fluid
for i in range():
    n =
    if n == 1:

    else:
        ub =

    for j in range(len(z)):
                                # Equation 19 rearranged to solve for gamma_x
                                # Equation 19

# Plot predicted velocity profiles
plt.plot()

# Plot observed velocities
plt.plot()

# Add axis labels and a title
plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.show()
