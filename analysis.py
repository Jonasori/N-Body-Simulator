"""
Macroscopic analysis tools for looking at runs.

Note that all these tools draw on runs that have already been executed
(i.e. this only draws on files from completed runs, rather than starting
runs of it's own.)
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from constants import trajOutName, axlims, AU, gifOutName, rSol


def plotTrajectories(save_plot=False):
    # Make a trajectory (smeared) plot from a some coordinate outfiles. Show or savefig().
    outname = trajOutName
    filenames = pd.read_table('filenames.log').Name

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    ax.axis([-axlims, axlims, -axlims, axlims])
    bg = plt.Circle((0, 0), radius=np.sqrt(2)*axlims, color='black', alpha=0.9)
    ax.add_artist(bg)

    for f in filenames:
        print f
        p = pd.read_table(f, delim_whitespace=True)
        if f == 'Star.txt':
            plt.plot(p.XS, p.YS, 'oy')
        plt.plot(p.XS, p.YS)

    #plt.legend()
    plt.title('Orbital Paths')
    plt.xlabel('Distance (meters)')
    plt.ylabel('Distance (meters)')

    if save_plot is True:
        plt.savefig(outname)
        print "Trajectories plotted in", outname
    else:
        plt.show()


def plotLines(saveFigs=False):
    """
    Plot lines connecting trajectory steps.

    To mimic this: https://www.facebook.com/permalink.php?story_fbid=536038580109918&id=100011113415766&notif_id=1513793777241322&notif_t=feedback_reaction_generic_tagged

    Obviously, do a run before doing this.

    Args:
        saveFigs (bool): saves (if True) or shows (if False) each step's plot.
    """
    axlims = 1.5 * AU
    outname = 'orbitLines'

    # Figure setup
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    ax.axis([-axlims, axlims, -axlims, axlims])
    bg = plt.Circle((0, 0), radius=np.sqrt(2)*axlims, color='black', alpha=0.9)
    ax.add_artist(bg)

    # Start out by just pulling in the Sun.
    sun = pd.read_table('Star.txt', delim_whitespace=True)
    # Set something up to store the planets later.
    planets = []

    fs = pd.read_table('filenames.log', delim_whitespace=True)
    for i in range(len(fs.Name)):
        # Don't read in the star
        if fs.Name[i] != 'Star.txt':
            planets.append(pd.read_table(fs.Name[i], delim_whitespace=True))


    plt.plot(sun.XS[0], sun.YS[0], '.r')
    i = 0
    while i < len(planets[0].XS):
        plt.plot([planets[0].XS[i], planets[1].XS[i]], [planets[0].YS[i], planets[1].YS[i]], color='cyan', alpha=0.07, linestyle='-')
        i += 100

        if saveFigs is True:
            plt.savefig(outname + str(i) + '.jpeg')

    if saveFigs is False:
        plt.show(block=False)


def makePics(fnames, gifYN):
    # Figure out how many timesteps we'll need
    # This is junky right now bc it assumes that every body has the same number of timesteps
    # This is fucking slow. plotTrajectories is way faster.
    # The only good time to use this is if run_BarnesHut didn't actually output pictures but you really want a gif.
    print fnames[0]
    ts = len(pd.read_table(fnames[0], delim_whitespace=True).XS)
    picnames = []

    # Plot only once every 100 timesteps
    for t in range(0, ts):
        print "Making pics for step", t
        # Set up the plot
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect = 'equal')
        ax.axis([-axlims, axlims, -axlims, axlims])
        bg = plt.Circle((0, 0), radius=np.sqrt(2)*axlims, color='blue', alpha=0.8)
        ax.add_artist(bg)

        # Grab the position of each body
        for f in fnames:
            f = pd.read_table(f, delim_whitespace=True)
            # Only do this if the data is there
            if t < len(f.XS):
                circle = plt.Circle((f.XS[t], f.YS[t]), radius=0.01*axlims, color='orange', alpha=1)
                ax.add_artist(circle)

        #plt.legend()
        plt.title('Orbital Paths')
        plt.xlabel('Distance (meters)')
        plt.ylabel('Distance (meters)')
        outname = 'out' + str(t) + '.png'
        plt.savefig(outname)
        #plt.show(block=False)

        # Add this picture's name to a list to feed to the gif maker
        picnames.append(outname)


    # Want a gif?
    if gifYN == 'y':
        print "Making GIF: ", gifOutName
        makeGif(picnames, gifOutName)
        print "Finished GIF:", gifOutName


def makeGif(nSteps):
    # This assumes that the filename log is called 'filenames.log'
    images = []

    for n in range(0,nSteps):
        filename = "graph_moment" + str(n) + ".jpeg"
        print "Adding: ", filename, "to gif", gifOutName
        images.append(imageio.imread(filename))
    imageio.mimsave(gifOutName, images)
    print "Gif created:", gifOutName


def plotRV(filename):
    # Why the fuck isn't this working
    star = pd.read_table(filename, delim_whitespace=True)
    plotVerticalRange = 1.5*rSol

    xs = np.array(star.XS)
    ys = np.array(star.YS)
    ts = np.arange(0, len(xs))
    print xs[2]
    print "Ts: ", ts[:10]
    print "Xs: ", xs[:10]
    print "Length:", len(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axis([-plotVerticalRange, plotVerticalRange, -plotVerticalRange, plotVerticalRange])


    plt.plot(xs, ys)
    """
    for t in range(len(star.XS)):
        #print star.XS[t]
        circle = plt.Circle((star.XS[t], star.YS[t]), radius=100, color='red', alpha=0.7)
        ax.add_artist(circle)
        #"""


    plt.show(block=False)
