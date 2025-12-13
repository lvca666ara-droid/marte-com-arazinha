# Dia 8 - Falha no Kilopower - Base Alpha, Marte - 13/12/2025
import time
import random

print("=== SIMULAÇÃO DIA 8: FALHA NO KILOPOWER ===")
time.sleep(1)

energia = 30  # kW total (nuclear + solar)
o2_nivel = 21  # %
temp_habitat = 20  # °C
hora = "14:30"

print(f"[{hora}] Tudo normal. Energia: {energia}kW | O₂: {o2_nivel}% | Temp: {temp_habitat}°C")
time.sleep(2)

print(f"\n[{hora}:10] ALERTA: Kilopower falhando – Stirling travado por poeira!")
energia -= 20
o2_nivel -= 2
temp_habitat -= 5
print(f"Energia caiu: {energia}kW | O₂: {o2_nivel}% | Temp: {temp_habitat}°C")
print("MOXIE/Sabatier em modo backup solar – produção halved!")
time.sleep(3)

print("\nTentando reinício manual...")
time.sleep(2)
sucesso = random.choice([True, False])
if sucesso:
    print("Reinício parcial OK! Energia volta pra 20kW.")
    energia = 20
    o2_nivel += 1
else:
    print("Falha grave: Heat pipes congelados. Precisa EVA (saída com traje).")
    input("\n> Pressione ENTER pra vestir traje e sair...")
    print("Saindo... descongelando heat pipes manualmente...")
    time.sleep(3)
    print("Descongelado! Reinício total.")
    energia = 30

print(f"\n[{hora}:30] Status final: Energia: {energia}kW | O₂: {o2_nivel}% | Temp: {temp_habitat + 5}°C")
print("Base salva. Você é o herói.")
print("Te amo salvando Marte <3")