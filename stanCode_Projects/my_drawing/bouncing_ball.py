"""
File: 
Name: yiting wu
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

oval = GOval(SIZE, SIZE)
oval.filled = True
oval.fill_color = 'black'
window.add(oval, START_X, START_Y)

# make a switch to use mouse click to control whether the ball fall or not
count = 0

# use vy variable to make vertical speed changeable
vy = 0

# use a switch to distinguish whether mouse click effects or not
switch = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global oval, window, count, vy, switch
    if switch:
        return
    if count < 3:
        while True:
            switch = True
            if oval.x < window.width:
                vy += GRAVITY
                oval.move(VX, vy)
                if oval.y >= window.height:
                    vy = -1 * vy * REDUCE
                    oval.move(VX, vy)
                pause(DELAY)
            else:
                switch = False
                window.add(oval, START_X, START_Y)
                vy = 0
                count += 1
                break


if __name__ == "__main__":
    main()
