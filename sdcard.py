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

CMD0  = b'\x40\x00\x00\x00\x00\x95'
CMD8  = b'\x48\x00\x00\x01\xAA\x87'
CMD16 = b'\x50\x00\x00\x02\x00\x15'
CMD17 = b'\x51\x00\x00\x00\x00\x55'
CMD41 = b'\x69\x40\x00\x00\x00\x77'
CMD55 = b'\x77\x00\x00\x00\x00\x65'
CMD58 = b'\x7A\x00\x00\x00\x00\xFD'

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


    def getAnswer1(self):
        """Получить однобайтовый ответ."""

        # Цикл ожидания ответа
        for i in range(10):  # Даём 10 попыток получить ответ
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
        

    def getAnswer6(self):
        """Получить 6-байтовый ответ."""
        result, ans = self.getAnswer1()
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


    def cmd0(self):
        """Отправляет SD-карте команду CMD0."""
        self.uart.sendCmdToCard(CMD0)        
        return self.getAnswer1()


    def cmd8(self):
        """Отправляет SD-карте команду CMD8."""
        self.uart.sendCmdToCard(CMD8)
        return self.getAnswer6()


    def cmd41(self):
        """Отправляет SD-карте команду CMD41."""
        self.uart.sendCmdToCard(CMD41)
        return self.getAnswer1()
    

    def cmd55(self):
        """Отправляет SD-карте команду CMD55."""
        self.uart.sendCmdToCard(CMD55)
        return self.getAnswer1()
    


if __name__ == "__main__":

    pass
