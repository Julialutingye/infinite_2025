from pybricks.parameters import Color
from pybricks.tools import run_task, wait,multitask
from pybricks.parameters import Axis, Direction, Port
from robot_config import HUB, CENTER_ATTACHMENT,BACK_ATTACHMENT, DRIVE_BASE
from library import set_drivebase

from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Direction, Port
#CENTER_ATTACHMENT = Motor(Port.D, Direction.COUNTERCLOCKWISE, gears=[20,40])


async def demo_center_attachment():
    await HUB.speaker.beep()
    await set_drivebase()
    await wait(1000)
    DRIVE_BASE.settings(straight_speed=400, straight_acceleration=1000, turn_rate=200, turn_acceleration=1000)
    await DRIVE_BASE.straight(750)
    await DRIVE_BASE.turn(180)
    await DRIVE_BASE.straight(-167)
    await DRIVE_BASE.turn(-102)
    await wait(1000) 
    CENTER_ATTACHMENT.reset_angle(0)
    BACK_ATTACHMENT.reset_angle(0) 
    DRIVE_BASE.settings(straight_speed=60, straight_acceleration=1000, turn_rate=200, turn_acceleration=1000)
    await DRIVE_BASE.straight(142) 
    await wait(1000) 
    await CENTER_ATTACHMENT.run_angle(800, 400)
    await BACK_ATTACHMENT.run_angle(800, 50)
    await wait(1000)
    await DRIVE_BASE.straight(-100)
    DRIVE_BASE.settings(straight_speed=200, straight_acceleration=1000, turn_rate=200, turn_acceleration=1000)
    await DRIVE_BASE.turn(54)
    await CENTER_ATTACHMENT.run_angle(800, -350)
    await DRIVE_BASE.straight(290)
    await DRIVE_BASE.turn(-17)
    await DRIVE_BASE.straight(70)
    await multitask(CENTER_ATTACHMENT.run_angle(700, 500),DRIVE_BASE.turn(-5))
    #await CENTER_ATTACHMENT.run_angle(800, 400)
    await DRIVE_BASE.straight(-100)
    await DRIVE_BASE.turn(35)
    await DRIVE_BASE.straight(76)
    await BACK_ATTACHMENT.run_angle(800, -100)

if __name__ == "__main__":
    run_task(demo_center_attachment())