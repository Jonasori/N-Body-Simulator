"""Constants for the n-body simulator."""

# PACKAGES
import datetime
import astropy.constants as c

# CONSTANTS
G = -c.G.value                                   # m3 kg-1 s-2
AU = c.au.value                                  # m
mSol = c.M_sun.value                             # kg
rSol = c.R_sun.value                             # m
mEarth = c.M_earth.value                         # kg
rEarth = c.R_earth.value                         # m


# Note that this is the only place dt is defined
# For stellar scales (v2434)
# dt = 30000
# axlims = 220 * AU
dt = 1800                                        # duration of one timestep (s)
axlims = 2 * AU                                  # AU

theta = 0.0                                      # s/d, for BH Approx
steps = []                                       # the output file; not sure why this is here.


# FILENAMES
# Automatically make good new file names.
now = datetime.datetime.now()
months = ['jan', 'feb', 'march', 'april', 'may', 'june',
          'july', 'aug', 'sep', 'oct', 'nov', 'dec']
today = months[now.month - 1] + str(now.day)
logfileName = today + 'run.log'
gifOutName = today + 'run.gif'
trajOutName = today + '_run.png'


# ARRAYS FOR LATER
gifNames      = []
elapsedTimeBF = []
elapsedTimeBH = []
durationBF    = []
durationBH    = []
