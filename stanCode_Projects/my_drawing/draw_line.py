"""
File: 
Name: yiting wu
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the circle
SIZE = 10

window = GWindow()
circle = GOval(SIZE, SIZE)
count = 1

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(dot_line)


def dot_line(mouse):
    """
    draw a dot when mouse click in odd times and draw a line connecting with (x, y) of previous click when
    mouse click in even times
    """
    global circle, count
    if count % 2 == 1:
        window.add(circle, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        count += 1
    elif count % 2 == 0:
        straight_line = GLine(circle.x, circle.y, mouse.x, mouse.y)
        window.remove(circle)
        window.add(straight_line)
        count += 1


if __name__ == "__main__":
    main()
