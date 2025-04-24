#!/usr/bin/env python

import numpy as np
from numpy.polynomial.legendre import Legendre
from numpy import polynomial as P

TRAJECTORY_COEFF = {
    0: [1, 0, 0, 0, 0, 0, 0],
    1: [0, 1, 0, 0, 0, 0, 0],
    2: [0, 0, 1, 0, 0, 0, 0],
    3: [0, 0, 0, 1, 0, 0, 0],
    4: [0, 0, 0, 0, 1, 0, 0],
}

VN = 0.5 # velocity
H = 5 # duration of trajectory


TRAJECTORY_FILES = {
    0: "trajectories/phi0.csv",
    1: "trajectories/phi1.csv",
    2: "trajectories/phi2.csv",
    3: "trajectories/phi3.csv",
    4: "trajectories/phi4.csv"
}

columns = ['duration', 'x^0', 'x^1', 'x^2', 'x^3', 'x^4', 'x^5', 'x^6', 'x^7', 'y^0', 'y^1', 'y^2', 'y^3', 'y^4', 'y^5', 'y^6', 'y^7', 'z^0', 'z^1', 'z^2', 'z^3', 'z^4', 'z^5', 'z^6', 'z^7', 'yaw^0', 'yaw^1', 'yaw^2', 'yaw^3', 'yaw^4', 'yaw^5', 'yaw^6', 'yaw^7']
if __name__ == '__main__':    
    
    for traj_id in TRAJECTORY_COEFF.keys():
        task_coeffs = TRAJECTORY_COEFF[traj_id]

        legendre_poly = Legendre(task_coeffs, domain=[0, VN * H])
        poly_coeffs = np.pad(legendre_poly.convert(kind=P.Polynomial).coef, (0, 6 - traj_id)).reshape(1, 7)
        poly_coeffs[0, 0] = 0
        
        trajectory_defn = np.zeros((1, len(columns)))
        trajectory_defn[0, 1:8] = poly_coeffs
        trajectory_defn[0, 0] = H

        np.savetxt(TRAJECTORY_FILES[traj_id], trajectory_defn, delimiter=',', header=','.join(columns), comments='')
