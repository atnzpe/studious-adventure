import random

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        songs_list = ["Sai da frente !!!","Muuuuu","HuaHaHaHaHaHA"]
        print(random.choice(songs_list))

    def frear(self):
        print("Diminuindo velocidade ...")
        print("Biclicleta parada!")

