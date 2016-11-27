# Exercise 12: Viscous flow of ice

## Sources
This tutorial is based on a MATLAB exercise from [Prof. Todd Ehlers (University of Tübingen, Germany)](http://www.geo.uni-tuebingen.de/?id=2183).

## Overview
As we’ve seen previously, most landforms on Earth are sculpted by the flow of fluids across the landscape.
Erosion by glaciers can significantly change the Earth's surface, moving vast quantities of material from high elevations to lower elevations.
Glacial landscapes are unique and clearly reflect erosion by processes that differ greatly from those found in fluvial systems.
To understand how material is moved within glacial systems, it is important to first understand the dominant controls on glacier velocities.
As usual, you are asked to modify an starter Python script to produce plots and to answer questions related to the plots.

## Problem 1 - Non-Newtonian (nonlinear) flow in open channels
### Background and theory
I suggest you first read through the [background and theory](https://github.com/Intro-Quantitative-Geology/Lesson-12-Viscous-flows/blob/master/Lesson/Exercise-12-theory-1.md) before proceeding with this problem.

### Planform flow velocity across a glacier
The goal of this exercise is to calculate horizontal velocity profiles across a glacier for Newtonian and non-Newtonian fluid flow resulting from a pressure gradient.

1. Modify the Python script file [`open_channel_prob1.py`](open_channel_prob1.py) to plot the non-dimensional velocity (*u*/*u*̅) of a fluid as a function of non-dimensional distance (*y*/*h*) across the channel of width *h* (Equation 12 from the the [background and theory](https://github.com/Intro-Quantitative-Geology/Lesson-12-Viscous-flows/blob/master/Lesson/Exercise-12-theory-1.md)).
Assume the flow is symmetrical about *y* = 0 and the velocity is zero at the boundaries of the channel.
In your Python script you should
  1. Solve for the non-dimensional velocity across the channel for a Newtonian fluid and for non-Newtonian fluid with power-law exponents of *n* = 2, 3, 4, 5

    :heavy_exclamation_mark: **NOTE**: The flow is symmetric about *y* = 0 and for negative *y* values the equation does not work properly. You can solve one half of the flow (*y* ≥ 0) and use symmetry to plot the other half of the flow.
  2. Create one plot of the non-dimensional velocity of all of the fluids as a function of non-dimensional distance.
    - Be sure to label your axes and add a title
    - Also include text labels beside each velocity profile listing the power-law exponent
    - **How sensitive is the velocity to the power-law exponent? What is the maximum percent difference in velocity between n = 2 and n = 4?**
  3. Include clear comments that explain what each section of your code does
2. The [Saskatchewan glacier near Banff in Alberta, Canada](https://goo.gl/maps/R9S48J4KYPr) (Figure 1) is 1400 m wide and part of a large ice field known as the Columbia Icefield.

    ![Saskatchewan glacier](https://upload.wikimedia.org/wikipedia/commons/a/a5/Saskatchewan_Glacier.jpg)<br/>
    *Figure 1. Saskatchewan glacier.*
    
     Distance from center line [m] | Velocity [m/a] | Velocity [m/s]
     ----------------------------- | -------------- | --------------
     -660 | 12 | 3.80E-07
     -640 | 22 | 7.00E-07
     -570 | 42 | 1.33E-06
     -460 | 63 | 2.00E-06
     -220 | 74 | 2.35E-06
     40 | 76 | 2.41E-06
     180 | 74 | 2.35E-06
     260 | 72 | 2.28E-06
     500 | 51 | 1.62E-06
     *Table 1. Velocity measurements across the Saskatchewan glacier.*<br/><br/>
     The file [`sask_glacier_velo.txt`](sask_glacier_velo.txt) contains a series of surface velocities measured at various locations across the glacier (Table 1). Modify the Python script [`sask_glacier_prob1.py`](sask_glacier_prob1.py) to plot the measured velocities as a function of distance from the center line of the glacier, and also plot predicted velocity profiles for several non-Newtonian fluids (Equation 10 from the the [background and theory](https://github.com/Intro-Quantitative-Geology/Lesson-12-Viscous-flows/blob/master/Lesson/Exercise-12-theory-1.md)). Assume *a* = 5 × 10<sup>-24</sup> Pa<sup>-3</sup> s<sup>-1</sup>. In your program you should
  1. Solve for the velocity profile of a non-Newtonian fluid with power-law exponents of *n* = 2, 3, 4, 5

    :heavy_check_mark: **HINT**: The term (p<sub>1</sub> - p<sub>0</sub>) / *L* in Equation 10 is an unknown. However, you can solve for it using the condition that the maximum flow velocity (~2.41 × 10<sup>-6</sup> m/s) occurs at *y* = 0. Once you have solved for that term, you can insert it back into Equation 10 to solve for the velocities elsewhere.<br/><br/>
    :heavy_exclamation_mark: **NOTE**: Again, the flow is symmetric about *y* = 0 and for negative *y* values Equation 10 does not work properly. You can solve one half of the flow (*y* ≥ 0) and use symmetry to plot the other half of the flow.
  2. Load the observed velocity data
  3. Plot the measured velocities along with the 4 predicted velocity profiles. Be sure to label your axes and include a title. Also include text labels beside each velocity profile listing the power-law exponent.
  4. Include clear comments explaining what each section of the code does.

## Problem 2 - Non-Newtonian (nonlinear) flow down an inclined plane
### Background and theory
Again, I suggest you first read through the [background and theory](https://github.com/Intro-Quantitative-Geology/Lesson-12-Viscous-flows/blob/master/Lesson/Exercise-12-theory-2.md) before proceeding with this problem.

### Glacial flow velocities along a vertical profile
The goal of this exercise is to calculate vertical velocity profiles across a glacier for Newtonian and non-Newtonian fluid flow resulting from a gravitational forces on the glacier.

1. The [Athabasca glacier](https://goo.gl/maps/HggYfoKxEUQ2) (Figure 2) is another glacier in the Columbia Icefield.

    ![Athabasca glacier](https://upload.wikimedia.org/wikipedia/commons/4/41/Icefields_parkway.jpg)<br/>
    *Figure 2. Athabasca glacier.*

    Depth from surface [m] | Height from base z [m] | Horizontal velocity [m/a] | Horizontal velocity [m/s]
    ---------------------- | ---------------------- | ------------------------- | -------------------------
    0 | 209 | 28.6 | 9.10E-07
    15 | 195 | 28.5 | 9.00E-07
    30 | 180 | 28.5 | 9.00E-07
    45 | 165 | 28.4 | 9.00E-07
    60 | 150 | 28.2 | 8.90E-07
    75 | 135 | 28.0 | 8.90E-07
    90 | 120 | 27.7 | 8.80E-07
    105 | 105 | 27.2 | 8.60E-07
    120 | 90 | 26.5 | 8.40E-07
    135 | 75 | 25.5 | 8.10E-07
    150 | 60 | 24.0 | 7.60E-07
    165 | 45 | 21.5 | 6.80E-07
    180 | 30 | 17.5 | 5.50E-07
    195 | 15 | 10 | 3.20E-07
    209 | 0 | 4 | 1.30E-07
*Table 2. Velocities measured from a vertical profile through Athabasca glacier.*<br/><br/>
A vertical velocity profile for the Athabasca glacier has been measured and the measurements are in the file [`atha_glacier_velo.txt`](atha_glacier_velo.txt) (Table 2). Modify the provided Python script [`atha_glacier_prob2.py`](atha_glacier_prob2.py) to plot the velocity measurements (*x*-axis) versus the height (*z*-axis) from the bed. On the same plot, include Newtonian and non-Newtonian fluid flow profiles as well (Equation 19 from the [background and theory](https://github.com/Intro-Quantitative-Geology/Lesson-12-Viscous-flows/blob/master/Lesson/Exercise-12-theory-2.md)). Assume *a* = 5 × 10<sup>-24</sup> Pa<sup>-3</sup> s<sup>-1</sup>. In your code, you should
  1. Solve for the velocity profile for a Newtonian fluid. Your profile should have a no-slip basal boundary condition (*u*<sub>b</sub> = 0) and honor the observed surface velocity.

    :heavy_exclamation_mark: **NOTE**: Again, in this problem there is an unknown term *γ*<sub>x</sub> in Equation 19. However, you can solve for it using the condition that the maximum flow velocity (~0.91 × 10<sup>-6</sup> m/s) occurs at *z* = *h* = 209 m. Once you have solved for that term, you can insert it back into Equation 19 to solve for the velocities elsewhere.
  2. Solve for the velocity profiles of non-Newtonian fluids with power-law exponents of *n* = 2, 3, 4, 5 (Equation 19). You should set ub equal to the observed value (Table 2) and your Python program should honour the observed surface velocity (see tip above).
  3. Load in the observed velocity profile data
  4. Generate a plot of the observed velocity values, the predicted Newtonian velocity profile and the 4 non-Newtonian velocity profiles
  5. Include clear comments that explain what each section of the program does

## What to submit
**For this exercise, your modifications to the end of this document should include**

1. Plots of the non-dimensional velocity profiles for Newtonian and non-Newtonian fluids **AND** the velocity profile across the Saskatchewan glacier with points showing the measured velocities for Problem 1
2. One plot of the Newtonian and non-Newtonian velocity profiles across the Athabasca glacier with data points showing the measured velocities for Problem 2
3. Figure captions for each plot describing the plot as if it were in a scientific journal article.
  - For the second plot in Problem 1, list the most likely power-law exponent *n* for the Saskatchewan glacier in the caption
  - For Problem 2, list the most likely value for the power-law *n* exponent for the Athabasca glacier in the caption
4. Answers to the questions in bold for Problem 1
5. Copies of your modified Python scripts for Problems 1 and 2

# Answers
## Problem 1
This is some text. You can use *italics* or **bold** text easily. You may want to read a bit more about [formatting text in Github-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/). You can see an example of how to display an image with a caption below.

![Text shown if image does not load](Images/sine.png)<br/>
*Figure 3: Sine wave calculated from 0 to 2π*
