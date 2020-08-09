#!/usr/bin/env python3


'''
@module  sdc
@version <укажите версию>
@date    2020.08.01
@author  Alexander
@email   zhevak@mail.ru

@brief   <вставьте сюда краткое описание модуля>
'''

import time

from uart import Uart
from sdcard import Sdcard
from leds import Leds

if __name__ == "__main__":

    uart1 = Uart()
     
    card = Sdcard(uart1)
    leds1 = Leds(uart1)

    leds1.test()
    time.sleep(1)
    print()
    
    card.preInit()
    time.sleep(1)
    print()

    card.select()
    time.sleep(1)
    print()

    if not card.cmd0():
        print('Пхоже, что SD-карточка дохлая')
        exit()

    time.sleep(1)
    print()

    card.unselect()
    
    time.sleep(1)

    
