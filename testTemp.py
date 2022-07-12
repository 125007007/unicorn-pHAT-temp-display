import unicornhat as uh
import time


uh.set_layout(uh.PHAT)
uh.brightness(0.5)

sampleFreq = 0.5 # time in seconds


def setColor(temp):
    if temp <= 10:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 0, 221, 255)
        uh.clear()
        uh.show()

    elif temp <= 15:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 0, 140, 255)
        uh.clear()
        uh.show()

    elif temp <= 20:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 240, 201, 26)
        uh.clear()
        uh.show()
    
    elif temp <= 25:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 242, 138, 27)
        uh.clear()
        uh.show()

    elif temp <= 30:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 242, 120, 27)
        uh.clear()
        uh.show()

    elif temp <= 35:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 242, 99, 27)
        uh.clear()
        uh.show()

    elif temp <= 40:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 242, 77, 27)
        uh.clear()
        uh.show()

    elif temp <= 45:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 242, 70, 27)
        uh.clear()
        uh.show()

    elif temp <= 50:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 242, 38, 27)
        uh.clear()
        uh.show()

for x in range(0, 50):
    setColor(x)