from pave_numerique import Pave
from time import sleep
from blink import blink
pave = Pave()

code = "123A"
userInput = ""


def iscode(entry: str) -> bool:
    return code == entry

print("ok")
while True:
    userInput+=pave.getkey()
    print(userInput)
    blink("blue")
    if len(userInput)==len(code):
        if code == userInput:
            blink("green")
            print("gg")
        else:
            blink("red")
            print("nul")
        userInput = ""
    sleep(0.5)
