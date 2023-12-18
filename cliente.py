from rsa import RSAsystem
from comunicador import MQTTCommunicator
import logging
import keyboard
import time

class Cliente(RSAsystem):

    def __init__(self, nome):
        super().__init__()
        self.comunicador = MQTTCommunicator(nome, 'broker.hivemq.com')
        self.clients = {}
        self.current_e = 0
        self.current_n = 0

logging.basicConfig(level=logging.INFO)

cliente1 = Cliente('bob')

cliente1.comunicador.start()
cliente1.comunicador.subscribe('amigos')

while True:
    if keyboard.is_pressed('/'):
        time.sleep(0.5)
        client_input = input()
        if client_input == 'publickey':
            cliente1.comunicador.publish('amigos', 'publickey' + ' ' + str(cliente1.e) + ' ' + str(cliente1.n))
        else:
            cliente1.comunicador.publish('amigos', client_input)
        time.sleep(0.5)

    if 'publickey' in cliente1.comunicador.info:
        e_sender, n_sender = cliente1.comunicador.info.split(' ')[1], cliente1.comunicador.info.split(' ')[2]
        if(e_sender != str(cliente1.e) or n_sender != str(cliente1.n)):
            cliente1.current_e, cliente1.current_n = e_sender, n_sender
    print(cliente1.current_e, cliente1.current_n)

