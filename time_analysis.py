"""Some utils that involve doing full runs."""


from run_driver import bh, bf


def calcTime(meth):
    """Do a bunch of runs of a method to profile the time.

    Args:
        meth (str): which method (bh or bf)
    """
    outname = 'timesteps-' + meth + '.txt'
    outstr = 'nBodies, Time' + '\n'

    g = open(outname, 'w')
    g.write(outstr)
    g.close()

    nt = 1500
    max_nBods = 6766

    if meth == 'bh':
        nBods = 1
        nBodsLast = 1
        while nBods <= max_nBods:
            g = open(outname, 'a')
            outs = bh.run_BarnesHut(nt, nBods)
            nBods = outs[0]
            dt = outs[1]
            g.write(str(nBods) + ", " +  str(dt) + '\n')
            g.close()

            # Use Golden ratio to step; see plotSpacing.py for a comparison
            # of how it grows compared to exponential
            nBods += nBodsLast
            nBodsLast = nBods - nBodsLast


    if meth == 'bf':
        nBods = 1
        nBodsLast = 1
        while nBods < max_nBods:
            g = open(outname, 'a')
            outs = bf.run_BruteForce(nt, nBods)
            nBods = outs[0]
            dt = outs[1]
            g.write(str(nBods) + " " +  str(dt) + '\n')
            g.close()
            nBods += nBodsLast
            nBodsLast = nBods - nBodsLast

    else:
        print "Choose your method better (bh or bf)"


def plot_full_time_comparison():
    """Make a full plot."""
    # Gather the time data.
    calcTime('bh')
    calcTime('bf')

    # Plot it out.
    # This is untested but seems reasonable.
    df_bh = pd.read_csv('timesteps-bh.txt')
    df_bf = pd.read_csv('timesteps-bf.txt')

    # This is kinda gross and could be improved by merging dfs.
    # Relies on each df to have the same 'Time' col.
    plt.plot(df_bh['nBodies'], df_bh['Time'], 'ob', label='Barnes-Hut')
    plt.plot(df_bh['nBodies'], df_bh['Time'], '-b')

    plt.plot(df_bf['nBodies'], df_bf['Time'], 'or', label='Brute Force')
    plt.plot(df_bf['nBodies'], df_bf['Time'], '-r')

    plt.xlabel('Number of Bodies')
    plt.ylabel('Time (Seconds)')
    plt.legend()
    plt.savefig('timecost.pdf')
