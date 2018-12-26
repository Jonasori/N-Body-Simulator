"""Creates a body object to be used in the simulator."""

import numpy as np
from constants import G



class body:
    """
    Initializes a body.

    Given a body's mass, radius, position, and velocity, create an object to be
    used in the simulator.
    """

    def __init__(self, name, mass, radius, xy, velocity, color):
        """Init the body."""
        self.name = name
        self.mass = mass                      # kg (str)
        self.radius = radius                  # m (float)
        self.xs = [xy[0]]                     # m (floats)
        self.ys = [xy[1]]                     # m (floats)
        self.velocity = velocity              # [x,y] [m/s, m/s] (floats)
        self.acceleration = [0, 0]            # [x,y] [m s-2, m s-2] (floats)
        self.color = color                    # plot color (str)
        self.hostNode = None                  # Useful for gridding stuff later
        self.fname = name + '.txt'

    def isEqual(self, otherBody):
        """Check if two bodies are actually the same."""
        if self.name == otherBody.name:
            return True
        return False

    def aGrav(self, otherBody):
        """Calculate the grav. accel. on a body due to a different body."""
        # Zero this out elsewhere and add on.
        #self.acceleration = [0,0]
        if self.name != otherBody.name:
            # Update gravitational acceleration (a = f/m) -> self.m cancels
            # take x or y projections with x/y hats
            x = (self.xs[-1] - otherBody.xs[-1])
            y = (self.ys[-1] - otherBody.ys[-1])
            d = (np.sqrt(x**2 + y**2))
            xhat = x/d
            yhat = y/d
            self.acceleration[0] += xhat * G * otherBody.mass * d**-2
            self.acceleration[1] += yhat * G * otherBody.mass * d**-2

    def positionAndVelocityUpdater(self, dt):
        """Update a body's position and velocity over a timestep."""
        self.velocity[0] += self.acceleration[0] * dt           # x component
        self.velocity[1] += self.acceleration[1] * dt           # y component

        self.xs.append(self.xs[-1]
                       + self.velocity[0] * dt
                       + 0.5*self.acceleration[0] * (dt**2)
                       )

        self.ys.append(self.ys[-1]
                       + self.velocity[1] * dt
                       + 0.5*self.acceleration[1] * (dt**2)
                       )

        # Now write this position change to the body's file.
        # Maybe change this to a DF and pickle it?
        g = open(self.fname, 'a')
        outstr = str(self.xs[-1]) + " " + str(self.ys[-1]) + '\n'
        g.write(outstr)
        g.close()

    def hill_radius(self, otherBody):
        """Calculate the Hill Radius of a body.

        From Wiki: An astronomical body's Hill sphere is the region in which it
        dominates the attraction of satellites. The outer shell of that region
        constitutes a zero-velocity surface.

        Note that this is set up for circular orbits, which is probably a bad
        assumption for this orbits, but finding a real eccentricity would be
        brutal.
        """
        e = 0
        a = np.sqrt((self.xs[-1] - otherBody.xs[-1])**2
                    + (self.ys[-1] - otherBody.ys[-1])**2)
        r_hill = a * (1 - e) * (otherBody.mass / (3*self.mass))**(1/3)
        return r_hill
