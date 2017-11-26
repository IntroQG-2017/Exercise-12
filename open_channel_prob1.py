#!/usr/bin/env python3
"""Calculates flow velocities across an open channel.

Description:
    This script calculates and plots the solution for non-dimensional velocity as
    a function of non-dimensional distance across a channel
    
Usage:
    ./open_channel_prob1.py
    
Author:
    XXX YYY - DD.MM.YYYY
"""

# Import NumPy
import numpy as np
import matplotlib.pyplot as plt

#--- User-defined variables ---
a =                                     # Viscosity [1/(Pa**3.0 s)]
h =                                     # Channel width
y = np.linspace(-h/2.0, h/2.0, 101)     # Range of values across channel for velocity calculation
n_prof = 5                              # Number of velocity profiles to calculate

# Equations
u_nd = np.zeros([n_prof, len(y)])
n = 0

# Non-dimensional velocity profile for a Newtonian or non-Newtonian fluid
# Loop over all values of the power-law exponent
for i in range():
    n = 
    # Loop over all values of the width of the channel
    for j in range():
        if :
                                 # Equation 12, modified
        else:
                                 # Equation 12

# Calculate maximum percent change in velocity between n=2 and n=4
# Uncomment this line to add in the calculation
#max_percent_change = 

# Plot results
# Loop over all values of the power-law exponent
for i in range(n_prof):
    plt.plot()
    plt.text()
    
# Add axis labels and a title
plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.show()
