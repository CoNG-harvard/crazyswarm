"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm


TAKEOFF_DURATION = 3.0
HOVER_DURATION = 5.0


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]
    # cf.setParam('usd/logging', 1)
    # cf.setParam('ctrlMel/kp_xy', 0.8)
    # cf.setParam('ctrlMel/kR_xy', 70000)
    timeHelper.sleep(0.5)
    cf.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION)
    print("press button to switch")
    swarm.input.waitUntilButtonPressed()
    cf.setParm('stabilizer/controller', 5)
    # timeHelper.sleep(7)
    cf.land(targetHeight=0.05, duration=TAKEOFF_DURATION)
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
