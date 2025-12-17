# MOXIE Health Monitor - versão 1.0 (baseado em relatórios internos NASA 2025)
import time
from datetime import datetime
import random

class MoxieMonitor:
    def __init__(self):
        self.horas_op = 0  # horas de operação
        self.temperatura = 800  # °C
        self.crossover = 0.8  # % vazamento O2 pro lado do CO
        self.producao_base = 10  # g/h inicial
        self.status = "OK"

    def atualizar(self, dt=1):
        self.horas_op += dt
        self.temperatura += random.uniform(-1, +3)  # oscila com painel solar
        self.crossover += random.uniform(0.01, 0.03)  # cresce com uso
        # degradação gradual
        perda = 0.02 * (self.horas_op / 1000)
        self.producao = self.producao_base * (1 - perda)
        # alertas
        if self.temperatura > 850:
            self.status = "CRÍTICO - CÉLULA VAI RACHAR EM 48H"
        elif self.crossover > 1.0:
            self.status = "ALTA - PARAR EM 12H OU MORTE POR CO2"
        else:
            self.status = "OK"

    def relatorio(self):
        print(f"[{datetime.now().strftime('%H:%M')}]")
        print(f"Horas de operação: {self.horas_op:.1f}")
        print(f"Temperatura: {self.temperatura:.1f}°C")
        print(f"Crossover: {self.crossover:.2f}%")
        print(f"Produção atual: {self.producao:.1f} g/h (base: 10 g/h)")
        print(f"Status: {self.status}\n")

    def simula_dias(self, dias=5):
        for dia in range(dias):
            for hora in range(12):  # 12h/dia de operação
                self.atualizar(1)
            print(f"--- FIM DO DIA {dia+1} ---")
            self.relatorio()

# Usa
monitor = MoxieMonitor()
monitor.simula_dias(5)