import gsd.hoomd
import gsd.fl
import gsd.pygsd
import argparse, gsd
import numpy as np
from gsd.fl import GSDFile
import freud
import sys
 
f = gsd.pygsd.GSDFile(open('/Users/yufu/hoomd-2.9.4/langevinT.gsd', 'rb'))

trajectory = gsd.hoomd.HOOMDTrajectory(f)

print(trajectory[0].particles.position)

print(len(trajectory))


frames_to_take = [0,1,2,3]

# typical user-input arguments, loading hoomd trajectories, etc.
bins = 10
rmax = 1.0

rdf = freud.density.RDF(bins=bins, r_max= rmax)
 
for f in frames_to_take:
    sys.stdout.write("Processing frame {}... ".format(f))
    frame = trajectory[int(f)]
    points = frame.particles.position
    box = frame.configuration.box
    rdf.compute(system=(box, points), reset=False)
    sys.stdout.write("Done\n")
 

np.savetxt("test.out", np.c_[rdf.bin_centers,rdf.rdf],header="# bin, RDF")

