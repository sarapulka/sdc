#!/usr/bin/env python3


'''
@module  leds
@version <укажите версию>
@date    2020.08.09
@author  Alexander
@email   zhevak@mail.ru

@brief   <вставьте сюда краткое описание модуля>
'''


YLED_ON    = b'\x00\x11'
YLED_OFF   = b'\x00\x21'
BUZZER_ON  = b'\x00\x12'
BUZZER_OFF = b'\x00\x22'

RLED1_ON    = b'\x00\x30'
RLED1_OFF   = b'\x00\x40'
GLED1_ON    = b'\x00\x31'
GLED1_OFF   = b'\x00\x41'
YLED1_ON    = b'\x00\x32'
YLED1_OFF   = b'\x00\x42'
RLED2_ON    = b'\x00\x33'
RLED2_OFF   = b'\x00\x43'
GLED2_ON    = b'\x00\x34'
GLED2_OFF   = b'\x00\x44'
YLED2_ON    = b'\x00\x35'
YLED2_OFF   = b'\x00\x45'
RLED3_ON    = b'\x00\x36'
RLED3_OFF   = b'\x00\x46'
RLED4_ON    = b'\x00\x37'
RLED4_OFF   = b'\x00\x47'


import time

class Leds():
    """."""
    
    def __init__(self, uart):
        """."""
        self.uart = uart

    def rled1_on(self):
        self.uart.sendCmdToPeriph(RLED1_ON)

    def rled1_off(self):
        self.uart.sendCmdToPeriph(RLED1_OFF)

    def gled1_on(self):
        self.uart.sendCmdToPeriph(GLED1_ON)

    def gled1_off(self):
        self.uart.sendCmdToPeriph(GLED1_OFF)

    def yled1_on(self):
        self.uart.sendCmdToPeriph(YLED1_ON)

    def yled1_off(self):
        self.uart.sendCmdToPeriph(YLED1_OFF)

    def rled2_on(self):
        self.uart.sendCmdToPeriph(RLED2_ON)

    def rled2_off(self):
        self.uart.sendCmdToPeriph(RLED2_OFF)

    def gled2_on(self):
        self.uart.sendCmdToPeriph(GLED2_ON)

    def gled2_off(self):
        self.uart.sendCmdToPeriph(GLED2_OFF)

    def yled2_on(self):
        self.uart.sendCmdToPeriph(YLED2_ON)

    def yled2_off(self):
        self.uart.sendCmdToPeriph(YLED2_OFF)

    def rled3_on(self):
        self.uart.sendCmdToPeriph(RLED3_ON)

    def rled3_off(self):
        self.uart.sendCmdToPeriph(RLED3_OFF)

    def rled4_on(self):
        self.uart.sendCmdToPeriph(RLED4_ON)

    def rled4_off(self):
        self.uart.sendCmdToPeriph(RLED4_OFF)

    def buzzer_on(self):
        self.uart.sendCmdToPeriph(BUZZER_ON)

    def buzzer_off(self):
        self.uart.sendCmdToPeriph(BUZZER_OFF)

    def yled_on(self):
        self.uart.sendCmdToPeriph(YLED_ON)

    def yled_off(self):
        self.uart.sendCmdToPeriph(YLED_OFF)

    def test(self):
        """Тестирование светодиолдов и пищалки."""
        
        print('Тестирование светодиодов')
        self.rled1_on()
        time.sleep(0.1)
        self.rled1_off()
        time.sleep(0.1)

        self.gled1_on()
        time.sleep(0.1)
        self.gled1_off()
        time.sleep(0.1)

        self.yled1_on()
        time.sleep(0.1)
        self.yled1_off()
        time.sleep(0.1)

        self.rled2_on()
        time.sleep(0.1)
        self.rled2_off()
        time.sleep(0.1)

        self.gled2_on()
        time.sleep(0.1)
        self.gled2_off()
        time.sleep(0.1)

        self.yled2_on()
        time.sleep(0.1)
        self.yled2_off()
        time.sleep(0.1)

        self.rled3_on()
        time.sleep(0.1)
        self.rled3_off()
        time.sleep(0.1)

        self.rled4_on()
        time.sleep(0.1)
        self.rled4_off()
        time.sleep(0.1)

        self.buzzer_on()
        time.sleep(0.1)
        self.buzzer_off()
        time.sleep(0.1)

        self.yled_on()
        time.sleep(0.1)
        self.yled_off()
        time.sleep(0.1)


if __name__ == "__main__":

    pass
