"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Create a game removed bricks by a rolling ball.
change the ball direction by paddle moved with mouse
in order to remove the bricks
When all bricks are removed before 3 lives, you win!

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.set_initial_velocity()
        while graphics.switch and 0 < lives <= 3:
            graphics.ball_move()
            graphics.check_obj()
            if graphics.win():
                break
            elif graphics.ball_gameover():
                graphics.ball_reset()
                graphics.ball_move()
                lives -= 1
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
