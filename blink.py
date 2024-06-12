from machine import Pin
from time import sleep
from neopixel import NeoPixel
pine = Pin(8, Pin.OUT)                          # Pin number for v1 of the above DevKitC, use pin 38 for v1.1
np = NeoPixel(pine, 1)                          # "1" = one RGB led on the "led bus"
def blink(str):
    if str == "blue" :
        np[0] = (0,0,1)
    elif str == "red" :
        np[0] = (1,0,0)
    elif str == "green" :
        np[0] = (0,1,0)
    elif str == "white" :
        np[0] = (1,1,1)
    else:
        np[0] = (0,0,0)
    np.write()
    sleep(0.5)
    np[0] = (0,0,0)
    np.write()

