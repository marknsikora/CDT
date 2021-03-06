# ALL PARAMETERS EXCEPT theta MUST BE STRINGS, theta IS A FLOAT
import numpy as np
import os
from pathlib import Path
module_dir = Path(__file__).parents[0]

def const(theta, F):
    return float(F)
    
def linear(theta, F0, theta0, k):
    return (theta-float(theta0))*float(k) + float(F0)
    
def interpolate(theta, fname, delimiter):
    # loads from a text file with two columns (theta, tau) separated by delimiter
    # newlines MUST BE \n
    fpath = os.path.abspath(os.path.join(module_dir, fname))
    data = np.loadtxt(fpath, delimiter=delimiter)
    thetad = data[:,0]
    Fd = data[:,1]
    return np.interp(theta, thetad, Fd)
