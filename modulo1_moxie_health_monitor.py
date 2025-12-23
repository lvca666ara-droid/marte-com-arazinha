# MOXIE Health Monitor - versão 1.0 (sem decimal pra evitar erro)
import random
from datetime import datetime

class MoxieMonitor:
    def __init__(self):
        self.horas_op = 0
        self.temperatura = 800
        self.crossover = 0.8
        self.producao = 10
        self.status = "OK"

    def atualiza(self, dt=1):
        self.horas_op += dt
        self.temperatura += random.uniform(-1, 3)
        self.crossover += random.uniform(0.01, 0.03)
        # Degradação: 0.02 por 1000 horas → usa fração
        self.producao = 10 * (1 - (2 / 100) * self.horas_op / 1000)
        if self.temperatura > 850:
            self.status = "CRITICO troca celula"
        elif self.crossover > 1.0:
            self.status = "ALTA parar 12h"
        else:
            self.status = "OK"

    def mostra(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}]")
        print(f"temp: {self.temperatura:.1f} | cross: {self.crossover:.2f}% | prod: {self.producao:.1f} g/h")
        print(f"status: {self.status}\n")

    def roda(self, dias=3):
        for d in range(dias):
            for h in range(12):
                self.atualiza()
            print(f"dia {d+1}")
            self.mostra()

monitor = MoxieMonitor()
monitor.roda()