"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm


TAKEOFF_DURATION = 2.5
HOVER_DURATION = 5.0


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]
    cf.setParam('usd/logging', 1)
    # a = cf.getParam('quadSysId/pwmToThrustA')
    # b = cf.getParam('quadSysId/pwmToThrustB')
    # cf.setParam('quadSysId/pwmToThrustA', 1.1 * a)
    # cf.setParam('quadSysId/pwmToThrustB', 1.1 * b)
    # cf.setParam('ctrlNN/freq', 240)
    cf.setParam('nnForward/hover_ratio', 0.686)
    cf.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    # allcfs = swarm.allcfs
    # allcfs.takeoff(targetHeight=1.0, duration=2.0)
    # timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    print("press button to switch controller")
    swarm.input.waitUntilButtonPressed()
    cf.setParam('stabilizer/controller', 5)
    print("press button to land")
    swarm.input.waitUntilButtonPressed()
    cf.setParam('stabilizer/controller', 2)
    cf.land(targetHeight=0.04, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION)
    cf.setParam('usd/logging', 0)

def debug():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]
    while True:
        try:
            print(cf.position())
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
