#!/usr/bin/env python3


'''
@module  uart
@version <укажите версию>
@date    2020.08.09
@author  Alexander
@email   zhevak@mail.ru

@brief   Модуль связи с микроконтрллером по USB/UART
'''


PORT = '/dev/ttyUSB0'
BAUD = 115200
TIMEOUT = 0.1

import serial


class Uart(serial.Serial):
    """."""

    def __init__(self):
        """Конструктор."""
        serial.Serial.__init__(self, PORT)
        
        self.baudrate = BAUD
        self.bytesize = serial.EIGHTBITS
        self.parity = serial.PARITY_NONE
        self.stopbits = serial.STOPBITS_ONE


    def sendCmdToPeriph(self, command):
        """Послать команду периферии."""
        print('Передаём команду периферии: ', end='')
        for byte in range(len(command)):
            print(' {:02X}'.format(command[byte]), end='')
        print()
        
        # Побайтная передача без байт-стаффинга
        for byte in command:
            self.write(byte.to_bytes(1, byteorder='little'))


    def sendCmdToCard(self, command):
        """Послать команду SD-карточке и получить ответ."""        
        print('Передаём команду карте: ', end='')
        for byte in range(len(command)):
            print(' {:02X}'.format(command[byte]), end='')
        print()

        # Побайтная передача с байт-стаффингом
        for byte in command:
            if byte == 0:
                self.write(b'\x00\x00')  # Байт со значением 0x00 пересылаем с байт-стаффингом
            else:
                self.write(byte.to_bytes(1, byteorder='little'))
        

    def sendByte(self, byte):
        """Передаёт один байт без байт-стаффигна."""
        print('Передаём один байт: 0x{:02X}'.format(ord(byte)))

        self.write(byte)
        

    def rw(self, byte):
        """Производит передачу и приём одного байта."""        
        print('Производим передачу одного байта 0x{:02X} и затем сразу принимаем ответный байт'.format(ord(byte)))

        # Передача с байт-стаффингом
        if byte == 0:
            self.write(b'\x00\x00')  # Байт со значением 0x00 пересылаем с байт-стаффингом
        else:
            # self.write(byte.to_bytes(1, byteorder='little'))
            self.write(byte)
        
        self.reset_input_buffer()  # Очистим входной буфер от случайных байтов

        answer = self.read()
        if len(answer) == 1:
            # Был принят какой-то байт
            print('  ---> 0x{:02X} '.format(ord(answer)))
            return True, answer
        else:
            # Время ожидания вышло, ничего не было принято
            return False, None



if __name__ == "__main__":
    pass
