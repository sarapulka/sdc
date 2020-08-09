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

    # leds1.test()
    time.sleep(1)
    
    
    print('''
Step 1
    Set DI and CS high and apply 74 or more clock pulses to SCLK. Without this
    step under certain circumstances SD-card will not work. For instance, when
    multiple SPI devices are sharing the same bus (i.e. MISO, MOSI, CS).''')
    card.preInit()

    print()
    print('Переводим сигнал NCS у SD-карты в состояние лог.0')
    card.select()
    print()


    print('''
Step 2   
    Send CMD0 (GO_IDLE_STATE): Reset the SD card.''')
    result, answer = card.cmd0()
    if not result:
        print('Похоже, что SD-карточка дохлая')
        exit()
    else:
        print('CMD0 --> 0x{:02X}'.format(ord(answer)))
    print()


    print('''
Step 3
    After the card enters idle state with a CMD0, send a CMD8 with argument of
    0x000001AA and correct CRC prior to initialization process. If the CMD8 is
    rejected with illigal command error (0x05), the card is SDC version 1 or
    MMC version 3. If accepted, R7 response (R1(0x01) + 32-bit return value)
    will be returned. The lower 12 bits in the return value 0x1AA means that
    the card is SDC version 2 and it can work at voltage range of 2.7 to 3.6
    volts. If not the case, the card should be rejected.''')
    result, answer = card.cmd8()
    if not result:
        print('Похоже, что SD-карточка дохлая')
        exit()
    else:
        print('CMD8 -->', end='')
        for byte in answer:
            print(' 0x{:02X}'.format(ord(byte)), end='')
        print()

    
    print('''
Step 4.
    And then initiate initialization with ACMD41 with HCS flag (bit 30).''')
    for i in range(100):
        print("  итерация {}:".format(i))

        result, answer = card.cmd55()
        if not result:
            print('Похоже, что SD-карточка дохлая')
            exit()
        else:
            print('CMD55 --> 0x{:02X}'.format(ord(answer)))
            if ord(answer) != 0x01:
                print("Карта плохая")
                exit()

        result, answer = card.cmd41()
        if not result:
            print('Похоже, что SD-карточка дохлая')
            exit()
        else:
            if ord(answer) != 0x01:
                print("Ошибка при обращении к карте\n");
            else:
                print('OK')
                break

        time.sleep(0.01)
    
  
    print('''
Step 5.
    After the initialization completed, read OCR register with CMD58 and check
    CCS flag (bit 30). When it is set, the card is a high-capacity card known
    as SDHC/SDXC.''')

    result, answer = card.cmd58()
    if not result:
        print('Похоже, что SD-карточка дохлая')
        exit()
    else:
        print('CMD58 -->', end='')
        for byte in answer:
            print(' 0x{:02X}'.format(ord(byte)), end='')
        print()

    
    
    
    print()
    print('Переводим сигнал NCS у SD-карты в состояние лог.1')
    card.unselect()
    
    time.sleep(1)

    
