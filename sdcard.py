#!/usr/bin/env python3


'''
@module  sdcard
@version <укажите версию>
@date    2020.08.02
@author  Alexander
@email   zhevak@mail.ru

@brief   <вставьте сюда краткое описание модуля>
'''

import time


SPI_NCS_0  = b'\x00\x10'
SPI_NCS_1  = b'\x00\x20'

CMD0 = b'\x40\x00\x00\x00\x00\x95'
CMD8 = b'\x48\x00\x00\x01\xAA\x87'


DEBUG = False


class Sdcard:
    """."""
    
    def __init__(self, uart):
        """."""
        self.uart = uart
        
    
    def preInit(self):
        """Выдаёт 80 импульсов SCK."""
        self.unselect()
        for i in range(10):
            self.uart.rw(b'\xFF')
            
            
    def select(self):
        """Переводит сигнал NCS в активное состояние."""
        self.uart.sendCmdToPeriph(SPI_NCS_0)


    def unselect(self):
        """Дезактивирует сигнал NCS."""
        self.uart.sendCmdToPeriph(SPI_NCS_1)


    def cmd0(self):
        """Отправляет SD-карте команду CMD0."""
        self.uart.sendCmdToCard(CMD0)
        
        # Организуем цикл ожидания ответа
        for i in range(10):
            result, ans = self.uart.rw(b'\xFF')
            if DEBUG:
                print('{}. {}'.format(i, ans))
            if result == True:
                if DEBUG:
                    print('Принят байт 0x{:02X}'.format(ord(ans)))
                if ord(ans) == 0x01:
                    if DEBUG:
                        print('Карта на месте, карта отвечает')
                    return True, ans
        else:
            if DEBUG:
                print('Либо нет карты, либо карта не отвечает.')
            return False, None


    def cmd8(self):
        """Отправляет SD-карте команду CMD8."""
        self.uart.sendCmdToCard(CMD8)

        # Организуем цикл ожидания ответа
        for i in range(10):
            result, ans = self.uart.rw(b'\xFF')
            if DEBUG:
                print('{}. {}'.format(i, ans))        
            if result == True:
                if DEBUG:
                    print('Принят байт 0x{:02X}'.format(ord(ans)))
                if ord(ans) == 0x01:
                    if DEBUG:
                       print('Карта на месте, карта отвечает')

                    answer = []
                    answer.append(ans)

                    for j in range(5):
                        result, ans = self.uart.rw(b'\xFF')
                        if DEBUG:
                            print('{}. {}'.format(i, ans))        
                        if result == True:
                            if DEBUG:
                                print('Принят байт 0x{:02X}'.format(ord(ans)))
                            answer.append(ans)
                    
                    return True, answer
        else:
            if DEBUG:
                print('Либо нет карты, либо карта не отвечает.')
            return False, None


if __name__ == "__main__":

    pass
