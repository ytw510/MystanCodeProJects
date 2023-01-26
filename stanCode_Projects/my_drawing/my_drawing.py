"""
File:
Name: yiting wu
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    draw a picture named "no war" hoping world peace forever!
    """
    window = GWindow(width=550, height=660)
    label_1 = GLabel('NO', x=80, y=230)
    label_1.font = 'Dialog-230-bold'
    label_1.color = 'crimson'
    window.add(label_1)

    label_2 = GLabel('WAR!', x=30, y=690)
    label_2.font = 'Dialog-190-bold'
    label_2.color = 'crimson'
    window.add(label_2)

    # peace sign
    peace_1 = GOval(120, 120, x=380, y=180)
    peace_1.color = 'red'
    peace_1.filled = True
    peace_1.fill_color = 'red'
    window.add(peace_1)

    peace_2 = GOval(100, 100, x=390, y=190)
    peace_2.color = 'white'
    peace_2.filled = True
    peace_2.fill_color = 'white'
    window.add(peace_2)

    peace_3 = GRect(10, 110, x=435, y=180)
    peace_3.color = 'red'
    peace_3.filled = True
    peace_3.fill_color = 'red'
    window.add(peace_3)

    peace_4 = GPolygon()
    peace_4.add_vertex((440, 235))
    peace_4.add_vertex((395, 260))
    peace_4.add_vertex((395, 270))
    peace_4.color = 'red'
    peace_4.filled = True
    peace_4.fill_color = 'red'
    window.add(peace_4)

    peace_5 = GPolygon()
    peace_5.add_vertex((440, 235))
    peace_5.add_vertex((440, 245))
    peace_5.add_vertex((395, 270))
    peace_5.color = 'red'
    peace_5.filled = True
    peace_5.fill_color = 'red'
    window.add(peace_5)

    peace_6 = GPolygon()
    peace_6.add_vertex((440, 235))
    peace_6.add_vertex((485, 260))
    peace_6.add_vertex((485, 270))
    peace_6.color = 'red'
    peace_6.filled = True
    peace_6.fill_color = 'red'
    window.add(peace_6)

    peace_7 = GPolygon()
    peace_7.add_vertex((440, 235))
    peace_7.add_vertex((440, 245))
    peace_7.add_vertex((485, 270))
    peace_7.color = 'red'
    peace_7.filled = True
    peace_7.fill_color = 'red'
    window.add(peace_7)

    # minion
    minion_1 = GOval(130, 75, x=200, y=400)
    minion_1.color = 'slateblue'
    minion_1.filled = True
    minion_1.fill_color = 'slateblue'
    window.add(minion_1)

    minion_2 = GRect(5, 15, x=250, y=225)
    minion_2.color = 'black'
    minion_2.filled = True
    minion_2.fill_color = 'black'
    window.add(minion_2)

    minion_3 = GRect(5, 15, x=260, y=225)
    minion_3.color = 'black'
    minion_3.filled = True
    minion_3.fill_color = 'black'
    window.add(minion_3)

    minion_4 = GRect(5, 15, x=270, y=225)
    minion_4.color = 'black'
    minion_4.filled = True
    minion_4.fill_color = 'black'
    window.add(minion_4)

    minion_5 = GRect(130, 170, x=200, y=270)
    minion_5.color = 'yellow'
    minion_5.filled = True
    minion_5.fill_color = 'yellow'
    window.add(minion_5)

    minion_6 = GOval(130, 75, x=200, y=240)
    minion_6.color = 'yellow'
    minion_6.filled = True
    minion_6.fill_color = 'yellow'
    window.add(minion_6)

    minion_7 = GRect(135, 15, x=197, y=280)
    minion_7.color = 'black'
    minion_7.filled = True
    minion_7.fill_color = 'black'
    window.add(minion_7)

    minion_8 = GOval(80, 80, x=225, y=250)
    minion_8.color = 'black'
    minion_8.filled = True
    minion_8.fill_color = 'black'
    window.add(minion_8)

    minion_9 = GOval(60, 60, x=235, y=260)
    minion_9.color = 'white'
    minion_9.filled = True
    minion_9.fill_color = 'white'
    window.add(minion_9)

    minion_10 = GOval(30, 30, x=250, y=275)
    minion_10.color = 'black'
    minion_10.filled = True
    minion_10.fill_color = 'black'
    window.add(minion_10)

    minion_11 = GOval(15, 15, x=255, y=340)
    minion_11.color = 'black'
    minion_11.filled = True
    minion_11.fill_color = 'black'
    window.add(minion_11)

    minion_12 = GRect(130, 40, x=200, y=400)
    minion_12.color = 'slateblue'
    minion_12.filled = True
    minion_12.fill_color = 'slateblue'
    window.add(minion_12)

    minion_13 = GRect(80, 60, x=225, y=365)
    minion_13.color = 'slateblue'
    minion_13.filled = True
    minion_13.fill_color = 'slateblue'
    window.add(minion_13)

    minion_14 = GPolygon()
    minion_14.add_vertex((200, 350))
    minion_14.add_vertex((230, 365))
    minion_14.add_vertex((230, 380))
    minion_14.color = 'slateblue'
    minion_14.filled = True
    minion_14.fill_color = 'slateblue'
    window.add(minion_14)

    minion_15 = GPolygon()
    minion_15.add_vertex((200, 350))
    minion_15.add_vertex((200, 365))
    minion_15.add_vertex((230, 380))
    minion_15.color = 'slateblue'
    minion_15.filled = True
    minion_15.fill_color = 'slateblue'
    window.add(minion_15)

    minion_16 = GPolygon()
    minion_16.add_vertex((300, 365))
    minion_16.add_vertex((300, 380))
    minion_16.add_vertex((330, 350))
    minion_16.color = 'slateblue'
    minion_16.filled = True
    minion_16.fill_color = 'slateblue'
    window.add(minion_16)

    minion_17 = GPolygon()
    minion_17.add_vertex((300, 380))
    minion_17.add_vertex((330, 365))
    minion_17.add_vertex((330, 350))
    minion_17.color = 'slateblue'
    minion_17.filled = True
    minion_17.fill_color = 'slateblue'
    window.add(minion_17)

    minion_18 = GPolygon()
    minion_18.add_vertex((330, 365))
    minion_18.add_vertex((360, 390))
    minion_18.add_vertex((330, 415))
    minion_18.color = 'yellow'
    minion_18.filled = True
    minion_18.fill_color = 'yellow'
    window.add(minion_18)

    minion_19 = GPolygon()
    minion_19.add_vertex((330, 380))
    minion_19.add_vertex((345, 390))
    minion_19.add_vertex((330, 400))
    minion_19.color = 'white'
    minion_19.filled = True
    minion_19.fill_color = 'white'
    window.add(minion_19)

    minion_20 = GPolygon()
    minion_20.add_vertex((200, 330))
    minion_20.add_vertex((170, 355))
    minion_20.add_vertex((200, 380))
    minion_20.color = 'yellow'
    minion_20.filled = True
    minion_20.fill_color = 'yellow'
    window.add(minion_20)

    minion_21 = GPolygon()
    minion_21.add_vertex((200, 345))
    minion_21.add_vertex((185, 355))
    minion_21.add_vertex((200, 365))
    minion_21.color = 'white'
    minion_21.filled = True
    minion_21.fill_color = 'white'
    window.add(minion_21)

    minion_22 = GRect(30, 25, x=230, y=460)
    minion_22.color = 'slateblue'
    minion_22.filled = True
    minion_22.fill_color = 'slateblue'
    window.add(minion_22)

    minion_23 = GRect(30, 25, x=270, y=460)
    minion_23.color = 'slateblue'
    minion_23.filled = True
    minion_23.fill_color = 'slateblue'
    window.add(minion_23)

    minion_24 = GRect(30, 15, x=230, y=485)
    minion_24.color = 'black'
    minion_24.filled = True
    minion_24.fill_color = 'black'
    window.add(minion_24)

    minion_25 = GRect(30, 15, x=270, y=485)
    minion_25.color = 'black'
    minion_25.filled = True
    minion_25.fill_color = 'black'
    window.add(minion_25)

    minion_26 = GArc(55, 55, 90, 90, x=217, y=486)
    minion_26.color = 'black'
    minion_26.filled = True
    minion_26.fill_color = 'black'
    window.add(minion_26)

    minion_27 = GArc(55, 55, 0, 90, x=285, y=486)
    minion_27.color = 'black'
    minion_27.filled = True
    minion_27.fill_color = 'black'
    window.add(minion_27)


if __name__ == '__main__':
    main()
