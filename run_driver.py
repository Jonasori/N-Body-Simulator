"""Set up and execute an n-body simulation.

Exoplanets Final Project: N-Body Simulation
@author: Jonas Powell
October 2017

"If you just have a stupid sense of humor,
you'll never run out of things to laugh at."
- Ryan's UBinghamton friend Eli

"The larger our ignorance, the stronger the magnetic field."
- Woltier
"""


# CONSTANTS
from barnes_hut_gridding import node, tree
from brute_force import systemBF
from constants import axlims


# Choose which type of run to do and run it.
meth = raw_input("Which simulation method do you want to use?\n['bh', 'bf']: ")

if meth.lower() == 'bh':
    n = node('root', [-axlims, axlims], [-axlims, axlims], None)
    bh = tree(n)
    bh.visualizeTree()
    # nTimesteps, nSmallBods
    bh.run(30000, 0)

elif meth.lower() == 'bf':
    print "Starting Brute Force sim"
    bf = systemBF()
    bf.run(100, 0)  # nTimesteps, nSmallBods

else:
    print "Please choose Barnes-Hut (BH) or Brute Force (BF) and try again."
