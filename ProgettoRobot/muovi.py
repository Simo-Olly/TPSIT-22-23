#from classeRobotAlpha import AlphaBot
from classeRobotDebug import AlphaBotDebug
import time


def muovi(ab):
    ab.forward()
    time.sleep(3)
    ab.stop()
    ab.right()
    time.sleep(3)
    ab.stop()

    
if __name__ == "__main__":
    ab = AlphaBotDebug()
    muovi(ab)
