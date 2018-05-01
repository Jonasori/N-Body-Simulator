"""Set up and execute a run.

Choose a method (BF or BH), how many things, etc and run.
Outputs {some stuff}

Exoplanets Final Project: N-Body Simulation
@author: Jonas Powell
October 2017

"If you just have a stupid sense of humor,
you'll never run out of things to laugh at."
- Ryan's Binghamton friend Eli

"The larger our ignorance, the stronger the magnetic field."
- Woltier
"""

# PACKAGES
import datetime
import astropy.constants as c
# from twilio.rest import Client

# CONSTANTS
from barnes_hut_gridding import node, tree
from brute_force import systemBF

G = -c.G.value                                   # m3 kg-1 s-2
AU = c.au.value                                  # m
mSol = c.M_sun                                   # kg
rSol = c.R_sun                                   # m
mEarth = c.M_earth                               # kg
rEarth = c.R_earth                               # m


# Note that this is the only place dt is defined
# (not passed as an argument anywhere).

# For stellar scales (v2434)
# dt = 30000
# axlims = 220 * AU

dt = 1800                                        # duration of one timestep (s)
axlims = 2 * AU                                  # AU
theta = 0.0                                      # for BH Approx
steps = []                                       # the output file

# Automatically make good new file names.
now = datetime.datetime.now()
months = ['jan', 'feb', 'march', 'april', 'may', 'june',
          'july', 'aug', 'sep', 'oct', 'nov', 'dec']
today = months[now.month - 1] + str(now.day)
logfileName = today + 'run.log'
gifOutName = today + 'run.gif'
trajOutName = 'z' + today + 'run.png'

# Initialize arrays to hold stuff used later on.
gifNames = []
elapsedTimeBF = []
durationBF = []
elapsedTimeBH = []
durationBH = []

# Choose which type of run to do and run it.
bh = True

if bh:
    n = node('root', [-axlims, axlims], [-axlims, axlims], None)
    bh = tree(n)
    bh.visualizeTree()
    # nTimesteps, nSmallBods
    bh.run_BarnesHut(30000, 0)

else:
    bf = systemBF()
    # nTimesteps, nSmallBods
    bf.run_BruteForce(100, 0)
