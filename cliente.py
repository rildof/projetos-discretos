from rsa import RSAsystem, get_primes
from comunicador import MQTTCommunicator
import logging
import keyboard
import time

class Cliente(RSAsystem):

    def __init__(self, nome):
        p, q = get_primes()
        super().__init__(p, q)
        self.comunicador = MQTTCommunicator(nome, 'localhost')
        self.clients = {}
        self.currentPK = 0

logging.basicConfig(level=logging.INFO)

cliente1 = Cliente('alice')

cliente1.comunicador.start()
cliente1.comunicador.subscribe('amigos')

while True:
    if keyboard.is_pressed('enter'):
        time.sleep(0.5)
        client_input = input()
        cliente1.comunicador.publish('amigos', client_input)
        time.sleep(0.5)

    if 'publickey' in cliente1.comunicador.info:
        cliente1.currentPK = cliente1.comunicador.info.split(' ')[1]
    print(cliente1.currentPK)

