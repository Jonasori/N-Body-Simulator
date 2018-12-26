# N-Body Simulator

A pretty-much-functional, astronomically-motivated n-body simulator.

## Motivation:
This was written as a class project in the fall of 2017, I have used it as a side-project since then as a way to work on following best-practice guidelines, as well as adding some small improvements here and there.

## Features:
The package has two primary functions: running an n-body sim by brute force (calculating the force contribution from every body in the system in each step), or running one using Barnes-Hut gridding, which uses some simple approximations to limit the number of force contributions that need to be calculated at each step, reducing the computational cost of a run pretty significantly (from O(n<sup>2</sup>) to O(n logn))).


## Structure:
This package is structured to be run with a simple '''python python run_driver.py'''. From this point, the user may choose a brute-force or barnes-hut run.

**run_driver.py** initiates a run, as chosen by the user.

**constants.py** just centralizes all the constants we use (i.e. physical constants, path names, and so on).

**barnes_hut_gridding.py** sets up *tree* and *node* objects. The *tree* object holds the whole system of bodies, and has a bunch of features, including a run-initiator, visualization stuff, and a bunch of others.

**brute_force.py** sets up the equivalent structures for a brute-force run, except for that we don't need to treat this one as a graph so things are a little simpler in it.

**body.py** holds the actual body object definition that is used throughout to create bodies (i.e. planets, stars, planetesimals). Nice and simple.

**analysis.py** holds some functions to deal with/analyze the output files of a completed run (plotting, mostly).

**time_analysis.py** has functionality to run sims of varying number of bodies (number increases follow the Golden Ratio) and log how long those runs take. It also has a function to do that for both methods and plot a comparison of the two, which should return a plot like the one shown above. This is currently untested.



## Visualization:
The results can be visualized in a couple different ways:

First, as a simple trajectory plot, for both brute-force and barnes-hut methods:

![](Figures/solarsystem.png)

If we have a Barnes-Hut run, we can gif the graph evolution (two here because I just love how they look):

![](Figures/solarsystem.gif)

![](Figures/grid_evolution.gif)


We may also plot the RV curve of a system, comparing it with the trajectory plot above.

![](Figures/rv_and_orbit_jup.png)


By running a bunch of sims, we can plot the time-cost. This demonstrates that the Barnes-Hut gridding is actually doing its job and creating a log cost.

![](Figures/cost_evaluation.png)

I once saw [a video](https://www.facebook.com/brightside/videos/893000730828671/UzpfSTEwMDAxMTExMzQxNTc2Njo1MzYwMzg1ODAxMDk5MTg/?story_fbid=536038580109918&id=100011113415766&notif_id=1513793777241322&notif_t=feedback_reaction_generic_tagged) that purported to show an animation of lines connecting two planets at a bunch of timesteps through a few orbits, which created some "sacred geometry" and looked really nice. However, I was a little suspicious of it and, realizing that I had the tools to test whether or not it was true, I added a plotting feature (plotLines in analysis.py) to recreate the plot. Unfortunately, they're on a remote computer that I don't currently have access to, but I'll hopefully add some of the resulting plots soon if I remember (spoiler: they didn't work out to show sacred geometry in our Solar System).




## To-Do:
* It would be nice to have each run set up its own directory and store its output in there, just to simplify things.
