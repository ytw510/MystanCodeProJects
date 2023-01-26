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

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window.width-paddle_width)/2,
                            y=self.window.height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.window.width/2-ball_radius,
                     y=self.window.height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball

        # Initialize our mouse listeners
        self.__dx = 0
        self.__dy = 0
        self.switch = False
        onmouseclicked(self.turn_on_switch)
        onmousemoved(self.paddle_move)

        # Draw bricks
        brick_x = 0
        brick_y = brick_offset
        self.num_bricks = brick_rows * brick_cols
        for i in range(brick_rows):
            # 兩排同個顏色 形成一組
            if i == 0 or i % 10 == 0:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'red'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0
            elif i == 1 or i % 10 == 1:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'red'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0
            # 第二組
            elif i == 2 or i % 10 == 2:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'orange'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0
            elif i == 3 or i % 10 == 3:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'orange'
                    self.window.add(brick)

                brick_y += brick_spacing + brick_height
                brick_x = 0
            # 第三組
            elif i == 4 or i % 10 == 4:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'yellow'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0
            elif i == 5 or i % 10 == 5:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'yellow'
                    self.window.add(brick)

                brick_y += brick_spacing + brick_height
                brick_x = 0
            # 第四組
            elif i == 6 or i % 10 == 6:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'green'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0
            elif i == 7 or i % 10 == 7:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'green'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0
            # 第五組
            elif i == 8 or i % 10 == 8:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'blue'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0
            elif i == 9 or i % 10 == 9:
                for j in range(brick_cols):
                    brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                    brick_x += brick_spacing + brick_width
                    brick.filled = True
                    brick.fill_color = 'blue'
                    self.window.add(brick)
                brick_y += brick_spacing + brick_height
                brick_x = 0

    def paddle_move(self, mouse):
        if self.num_bricks == 0:
            self.window.add(self.paddle, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset)
        elif mouse.x < 0 + self.paddle.width/2:
            self.window.add(self.paddle, x=0, y=self.paddle.y)
        elif 0 <= mouse.x <= self.window.width - self.paddle.width / 2:
            self.window.add(self.paddle, x=mouse.x - self.paddle.width / 2, y=self.paddle.y)
        elif mouse.x > self.window.width + self.paddle.width:
            self.window.add(self.paddle, x=self.window.width - self.paddle.width, y=self.paddle.y)

    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)
        if self.ball.y < 0:
            self.__dy = self.__dy * -1
        if self.ball.x < 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = self.__dx * -1

    def ball_gameover(self):
        is_ball_gameover = self.ball.y + self.ball.height >= self.window.height
        return is_ball_gameover

    def ball_reset(self):
        self.window.add(self.ball, x=self.window.width/2-self.ball.width/2, y=self.window.height/2-self.ball.height/2)
        self.switch = False

    def set_initial_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def turn_on_switch(self, mouse):
        self.switch = True

    def check_obj(self):
        for i in range(0, 2):
            for j in range(0, 2):
                self.maybe_obj = self.window.get_object_at(self.ball.x + i * self.ball.width,
                                                           self.ball.y + j * self.ball.height)
                if self.maybe_obj is not None:
                    #遇到物體反彈：改變y的方向
                    self.__dy = self.__dy * -1
                    if self.maybe_obj is not self.paddle:
                        self.window.remove(self.maybe_obj)
                        self.num_bricks -= 1
                    #遇到paddle往上反彈 速度固定為負
                    elif self.maybe_obj is self.paddle:
                        if self.__dy > 0:
                            self.__dy = self.__dy * -1
                    #四個邊角逐一檢查，如果有消除磚塊就return結束迴圈
                    return

    def win(self):
        if self.num_bricks == 0:
            self.__dx = 0
            self.__dy = 0
            self.switch = False
            self.window.add(self.ball, x=self.window.width / 2 - self.ball.width / 2,
                            y=self.window.height / 2 - self.ball.height / 2)
            self.label = GLabel('CLEAR!', x=self.window.width/3, y=self.window.height/3)
            self.window.add(self.label)
