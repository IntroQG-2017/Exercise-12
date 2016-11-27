"""
sask_glacier_prob1.py

This script ...

@author: NAME - DD.MM.YYYY
"""

# Import NumPy
import numpy as np
import matplotlib.pyplot as plt

#--- User-defined variables
a =                    # Viscosity [1/(Pa**3.0 s)]
h =                    # Channel width
y =                    # Range of values across channel for velocity calculation
umax =                 # Velocity at center of channel
n_prof = 4             # Number of velocity profiles to calculate

# Open and read input file
data = np.loadtxt(fname='sask_glacier_velo.txt', delimiter=',')

# Create zeros arrays
data_y = np.zeros(len(data))     # Create empty array for data y-values
data_u_ma = np.zeros(len(data))  # Create empty array for data velocities [m/a]
data_u_ms = np.zeros(len(data))  # Create empty array for data velocities [m/s]

# Loop over lines in file and split into different variables
for line in data:
    data_y[linecount] = line[0]
    data_u_ma[linecount] = line[1]
    data_u_ms[linecount] = line[2]
    linecount = linecount + 1

# Equations
u = np.zeros([n_prof,len()])
n = 1

# Velocity profile for a Newtonian or non-Newtonian fluid
for i in range():
    n =
    p =                      # Equation 10 rearranged to solve for (p1-p0)/L
    for j in range():
        if :
                             # Equation 10
        else:
                             # Equation 10

# Plot predicted velocity profiles
plt.plot()

# Plot observed velocities
plt.plot()

# Add axis labels and a title
plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.show()
