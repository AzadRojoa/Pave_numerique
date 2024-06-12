from machine import Pin
import utime


class Pave:
    def __init__(self, row: tuple = (1, 2, 3, 4), col: tuple = (5, 6, 7, 9)):
        self.row_pins = [Pin(i, Pin.OUT) for i in row] 
        self.col_pins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in col]  
        self.key_map = [
            ['1', '4', '7', '*'],
            ['2', '5', '8', '0'],
            ['3', '6', '9', '#'],
            ['A', 'B', 'C', 'D']
        ]
        self.debounce_time = 20

    # read pressed key
    def read_keypad(self) -> str | None:
        for i, row_pin in enumerate(self.row_pins):
            row_pin.value(0)
            for j, col_pin in enumerate(self.col_pins):
                if col_pin.value() == 0:
                    utime.sleep_ms(self.debounce_time)
                    if col_pin.value() == 0:
                        row_pin.value(1)
                        return self.key_map[i][j]
            row_pin.value(1)
        return None

    def getkey(self) -> str:
        while True:
            key = self.read_keypad()
            if key is not None:
                return key
            utime.sleep_ms(150)
