#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *
import uav_trajectory


traj_id = 0

TRAJECTORY_COEFF = {
    0: [0, 0, 0, 0, 0, 0, 0]
}

TRAJECTORY_FILES = {
    0: "trajectories/phi0.csv"
}

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    traj = uav_trajectory.Trajectory()
    traj.loadcsv(TRAJECTORY_FILES[traj_id])

    TRIALS = 1
    TIMESCALE = 1.0
    for i in range(TRIALS):
        for cf in allcfs.crazyflies:
            cf.uploadTrajectory(0, 0, traj)

        allcfs.takeoff(targetHeight=1.0, duration=2.0)
        timeHelper.sleep(2.5)
        for cf in allcfs.crazyflies:
            print(cf.initialPosition)
            pos = np.array(cf.initialPosition) + np.array([-0.4, -1.0, 1.0])
            cf.goTo(pos, 0, 2.0)
        timeHelper.sleep(2.5)

        allcfs.startTrajectory(0, timescale=TIMESCALE)
        timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)

        for cf in allcfs.crazyflies:
            print(cf.initialPosition)
            pos = np.array(cf.initialPosition)+ np.array([0.0, 0, 1.0])
            cf.goTo(pos, 0, 2.0)
        timeHelper.sleep(2.5)

        allcfs.land(targetHeight=0.05, duration=2.5)
        timeHelper.sleep(3.0)
