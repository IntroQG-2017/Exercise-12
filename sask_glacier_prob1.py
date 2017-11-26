#!/usr/bin/env python3
"""Calculates flow velocities across an open channel.

Description:
    This script calculates and plots the solution for dimensional velocity as
    a function of dimensional distance across a channel. In addition, the
    script loads and plots observed velocity data from a file.
    
Usage:
    ./sask_glacier_prob1.py
    
Author:
    XXX YYY - DD.MM.YYYY
"""

# Import NumPy
import numpy as np
import matplotlib.pyplot as plt

#--- User-defined variables
a =                                     # Viscosity [1/(Pa**3.0 s)]
h =                                     # Channel width
y = np.linspace(-h/2.0, h/2.0, 101)     # Range of values across channel for velocity calculation
umax =                                  # Velocity at center of channel
n_prof = 4                              # Number of velocity profiles to calculate

# Open and read input file
data = np.loadtxt(fname='sask_glacier_velo.txt', delimiter=',')

# Split file data columns into different variables
data_y =            # Array for data positions across channel width [m]
data_u_ma =         # Array for data velocities [m/a]
data_u_ms =         # Array for data velocities [m/s]

# Equations
u = np.zeros([n_prof, len(y)])
n = 1

# Velocity profile for a Newtonian or non-Newtonian fluid
# Loop over all values of the power-law exponent
for i in range():
    n =
    p =                      # Equation 10 rearranged to solve for (p1-p0)/L
    # Loop over all values of the width of the channel
    for j in range():
        if :
                             # Equation 10, modified
        else:
                             # Equation 10

# Plot predicted velocity profiles
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
