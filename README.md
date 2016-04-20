# Lab-exercise-5

## Sources
This tutorial is based on a MATLAB exercise from [Prof. Todd Ehlers (Uni Tübingen)](http://www.geo.uni-tuebingen.de/?id=2183).

## Overview
As we’ve seen previously, most landforms on Earth are sculpted by the flow of fluids across the landscape. Erosion by glaciers can significantly change the Earth’s surface, moving vast quantities of material from high elevations to lower elevations. Glacial landscapes are unique and clearly reflect erosion by processes that differ greatly from those found in fluvial systems. To understand how material is moved within glacial systems, it is important to first understand the dominant controls on glacier velocities. As usual, you are asked to modify an starter Python script to produce plots and to answer questions related to the plots. We will again be using **Spyder** for these exercises.

## Getting started
1. You can start by making a folder to store files for this week's exercises in a Terminal.

    ```bash
    $ cd Desktop
    $ mkdir Lab-5
    $ cd Lab-5
    ```
**Reminder**: the `$` symbol above represents the command prompt in the Terminal window.
2. Now you can open **Spyder**.

    ```bash
    $ spyder
    ```

Now we are ready to start.

## Problem 1 - Non-Newtonian (nonlinear) flow in open channels
### Background and theory
I suggest you first read through the [background and theory](https://github.com/Intro-Quantitative-Geology/Viscous-flows/blob/master/Exercise-5-theory-1.md) before proceeding with the exercise.

### Planform flow velocity across a glacier
The goal of this exercise is to calculate horizontal velocity profiles across a glacier for Newtonian and non-Newtonian fluid flow resulting from a pressure gradient.

1. Modify the Python script file [`open_channel_ex1.py`](open_channel_ex1.py) to plot the non-dimensional velocity (*u*/*u*̅) of a fluid as a function of non-dimensional distance (*y*/*h*) across the channel of width *h* (Equation 12 from the the [background and theory](https://github.com/Intro-Quantitative-Geology/Viscous-flows/blob/master/Exercise-5-theory-1.md)). Assume the flow is symmetrical about *y* = 0 and the velocity is zero at the boundaries of the channel. In your Python script you should
  1. Solve for the non-dimensional velocity across the channel for a Newtonian fluid and for non-Newtonian fluid with power-law exponents of *n* = 2, 3, 4, 5

    :heavy_exclamation_mark: **NOTE**: The flow is symmetric about *y* = 0 and for negative *y* values the equation does not work properly. You can solve one half of the flow (*y* ≥ 0) and use symmetry to plot the other half of the flow.
  2. Create one plot of the non-dimensional velocity of all of the fluids as a function of non-dimensional distance.
    - Be sure to label your axes and add a title
    - Also include text labels beside each velocity profile listing the power-law exponent
    - **How sensitive is the velocity to the power-law exponent? What is the maximum percent difference in velocity between n = 2 and n = 4?**
  3. Include clear comments that explain what each section of your code does
2. The [Saskatchewan glacier near Banff in Alberta, Canada](https://goo.gl/maps/R9S48J4KYPr) (Figure 2) is 1400 m wide and part of a large ice field known as the Columbia Icefield.

    ![Saskatchewan glacier](https://upload.wikimedia.org/wikipedia/commons/a/a5/Saskatchewan_Glacier.jpg)<br/>
    *Figure 2. Saskatchewan glacier.*
    
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
     The file [`sask_glacier_velo.txt`](sask_glacier_velo.txt) contains a series of surface velocities measured at various locations across the glacier (Table 1). Modify the Python script [`sask_glacier_ex1.py`](sask_glacier_ex1.py) to plot the measured velocities as a function of distance from the center line of the glacier, and also plot predicted velocity profiles for several non-Newtonian fluids (Equation 10 from the the [background and theory](https://github.com/Intro-Quantitative-Geology/Viscous-flows/blob/master/Exercise-5-theory-1.md)). Assume *a* = 5 × 10<sup>-24</sup> Pa<sup>-3</sup> s<sup>-1</sup>. In your program you should
  1. Solve for the velocity profile of a non-Newtonian fluid with power-law exponents of *n* = 2, 3, 4, 5

    


## What to submit
**For this exercise, your modifications to the end of this document should include**

1. One plot each for Parts 1-3 and Part 5.
2. One plot for **each** combination of *m* and *n* values for Part 4.
3. A figure caption beneath **each** plot explaining what it shows as if it was in a scientific publication.
4. Answers to the questions in bold for Parts 1-5 inserted beneath the associated plots and captions in each Part.

# Answers
## Problem 1
This is some text. You can use *italics* or **bold** text easily. You may want to read a bit more about [formatting text in Github-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/). You can see an example of how to display an image with a caption below.

![Text shown if image does not load](Images/sine.png)<br/>
*Figure 2: Sine wave calculated from 0 to 2π*
