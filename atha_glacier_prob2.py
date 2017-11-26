#!/usr/bin/env python3
"""Calculates flow velocities through a valley glacier cross-section.

Description:
    This script calculates and plots the solution for dimensional velocity as
    a function of dimensional distance from the base of a valley glacier. It also
    loads and plots observed flow velocities from a file.
    
Usage:
    ./atha_glacier_prob2.py
    
Author:
    XXX YYY - DD.MM.YYYY
"""

# Import NumPy
import numpy as np
import matplotlib.pyplot as plt

# Open and read input file
data = np.loadtxt(fname='atha_glacier_velo.txt', delimiter=',')

# Split file data columns into different variables using data slices
data_depth =        # Array for data depths [m]
data_z =            # Array for data elevations from bed [m]
data_u_ma =         # Array for data velocities [m/a]
data_u_ms =         # Array for data velocities [m/s]

#--- User-defined variables
a =                             # Viscosity [1/(Pa**3.0 s)]
h =                             # Flow height
z = np.linspace(0, h, 101)      # Range of elevation values in flow for velocity calculation
data_umax =                     # Velocity at top of flow
data_ub =                       # Velocity at base of flow
n_prof = 5                      # Number of velocity profiles to calculate

# Equations
u = np.zeros([n_prof, len(z)])
n = 0

# Non-dimensional velocity profile for a Newtonian or non-Newtonian fluid
# Loop over all values of the power-law exponent
for i in range():
    n = 
    if n == 1:
        
    else:
        ub = 
    # Loop over all values of the height of the channel
    for j in range():
                                # Equation 19 rearranged to solve for gamma_x
                                # Equation 19

# Plot results
# Loop over all values of the power-law exponent
for i in range(n_prof):
    plt.plot()

# Plot observed velocities
plt.plot()

# Add axis labels and a title
plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.show()
