# open_channel.py
#
# This script calculates and plots the solution for non-dimensional velocity as
# a function of non-dimensional distance across a channel
#
# NAME - DATE

# Import NumPy
import numpy as np
import matplotlib.pyplot as plt

#--- User-defined variables ---
a =                    # Viscosity [1/(Pa**3.0 s)]
h =                    # Channel width
y =                    # Range of values across channel for velocity calculation
n_prof = 5             # Number of velocity profiles to calculate

# Equations
u_nd = np.zeros([n_prof,len()])
n=0

# Non-dimensional velocity profile for a Newtonian or non-Newtonian fluid
for i in range():
    n = 
    for j in range():
        if :
                                 # Equation 12
        else:
                                 # Equation 12

# Calculate maximum percent change in velocity between n=2 and n=4
# Uncomment this line to add in the calculation
#max_percent_change = 

# Plot results
plt.plot()
plt.text()
    
# Add axis labels and a title
plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.show()