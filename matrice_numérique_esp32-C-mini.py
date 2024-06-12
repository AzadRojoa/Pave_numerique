from pave_numerique import Pave
from time import sleep
from blink import blink
pave = Pave()

code = "123A"
userInput = ""

blink("white")
while True:
    userInput+=pave.getkey()
    print(userInput)
    blink("blue")
    if len(userInput)==len(code):
        if code == userInput:
            blink("green")
            print("good")
        else:
            blink("red")
            print("error code")
        userInput = ""
    sleep(0.5)
