import random
from datetime import datetime

class MoxieMonitor:
    def __init__(self):
        self.horas_op = 0
        self.temperatura = 800
        self.crossover = 80  # multiplicado por 100 pra evitar decimal
        self.producao = 1000  # multiplicado por 100 pra evitar decimal
        self.status = "OK"
        self.manutenções = 0
        self.estoque_celulas = 10

    def atualiza(self, dt=1):
        self.horas_op += dt
        self.temperatura += random.randint(-1, 3)
        self.crossover += random.randint(1, 3)
        self.producao = self.producao - (self.horas_op // 50)  # perda aproximada

        if self.temperatura > 850 or self.crossover > 100:
            self.emergencia()

    def emergencia(self):
        if self.estoque_celulas > 0:
            self.manutenções += 1
            self.estoque_celulas -= 1
            self.temperatura = 800
            self.crossover = 70
            self.producao = 950
            self.status = "OK apos manutencao"
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Manutencao automatica feita - celula {self.manutenções}")
        else:
            self.status = "SEM CELULAS - FIM"

    def mostra(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}]")
        print(f"temp: {self.temperatura} | cross: {self.crossover/100:.2f}% | prod: {self.producao/100:.1f} g/h")
        print(f"status: {self.status}\n")

    def roda(self, dias=5):
        for d in range(dias):
            for h in range(12):
                self.atualiza()
            print(f"--- DIA {d+1} ---")
            self.mostra()

monitor = MoxieMonitor()
monitor.roda()