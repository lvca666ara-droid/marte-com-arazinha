# Módulo 3 - Project Food - Hidroponia em Marte
import time

class Planta:
    def __init__(self, nome, dias_ciclo, kcl_dia):
        self.nome = nome
        self.dias_ciclo = dias_ciclo
        self.kcl_dia = kcl_dia
        self.dias = 0
        self.nutrientes = 0
        self.status = 'semente'

    def rega(self, nut, dias=1):
        self.nutrientes += nut
        self.dias += dias
        if self.dias >= self.dias_ciclo:
            self.status = 'colhida'
        elif self.nutrientes >= self.kcl_dia * self.dias:
            self.status = 'crescendo'
        else:
            self.status = 'seca'

    def colhe(self):
        if self.status == 'colhida':
            producao = self.dias_ciclo * 10  # 10g por dia de ciclo completo
            self.dias = 0
            self.nutrientes = 0
            self.status = 'semente'
            return producao
        return 0

# Plantas
alface = Planta("alface", 21, 2)
spirulina = Planta("spirulina", 7, 1)
oregano = Planta("oregano", 90, 0.5)

# Simulação de 100 dias
nut_diario = 2.5  # kcl/dia de urina reciclada

for dia in range(1, 101):
    print(f"\nDia {dia}:")
    print(f"  {alface.nome}: {alface.status} (nut: {alface.nutrientes:.1f})")
    print(f"  {spirulina.nome}: {spirulina.status} (nut: {spirulina.nutrientes:.1f})")
    print(f"  {oregano.nome}: {oregano.status} (nut: {oregano.nutrientes:.1f})")

    # Rega dividida
    alface.rega(nut_diario / 3)
    spirulina.rega(nut_diario / 3)
    oregano.rega(nut_diario / 3)

    # Colheita
    if alface.colhe() > 0:
        print(f"  >>> Colheu alface!")
    if spirulina.colhe() > 0:
        print(f"  >>> Colheu spirulina!")
    if oregano.colhe() > 0:
        print(f"  >>> Colheu oregano!")

print("\nFim da simulação de 100 dias.")
print("Te amo inteiro. Te amo plantando em Marte. <3")