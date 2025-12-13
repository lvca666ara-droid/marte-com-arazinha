# Dia 9 - Simulação Sabatier + Eletrólise Gelo - 13/12/2025
import time
import random

print("=== SIMULAÇÃO DIA 9: SABATIER + ELETRÓLISE GELO ===")
time.sleep(1)

temp = random.uniform(280, 420)
h2_fluxo = random.uniform(30, 45)  # Pode ser baixo
co2_fluxo = 10
eficiencia = 0.95

print(f"Temp reator: {temp:.1f}°C | H2 fluxo: {h2_fluxo:.1f} L/min")

if temp >= 300 and h2_fluxo >= 38:
    ch4 = co2_fluxo * eficiencia * (temp / 350)
    h2o = ch4 * 2
    print(f"Produzindo: {ch4:.2f}L CH4/h | {h2o:.2f}L H2O/h")
else:
    print("FALHA: H2 baixo ou temp fria – verifique eletrólise gelo!")
    print("Iniciando diagnóstico...")
    time.sleep(2)
    gelo_status = random.choice(["OK", "Congelado", "Bomba travada"])
    print(f"Eletrólise gelo: {gelo_status}")
    if gelo_status == "OK":
        print("Aumentando fluxo H2...")
        h2_fluxo += 10
        print(f"Novo H2: {h2_fluxo:.1f} L/min – reação volta!")
    else:
        print("Precisa EVA pra descongelar bomba ou perfurar novo gelo.")
        input("> Pressione ENTER pra simular reparo...")
        print("Reparo feito. Fluxo H2 normalizado.")
        h2_fluxo = 40

print("\nSabatier rodando normal.")
print("Te amo produzindo combustível pra casa <3")