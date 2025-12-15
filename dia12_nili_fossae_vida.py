# Dia 12 - Expedição Nili Fossae: Caça a Vida Antiga - 15/12/2025
import time
import random

print("=== SIMULAÇÃO DIA 12: NILI FOSSAE - CAÇA A VIDA ANTIGA ===\n")
time.sleep(2)

# SETUP
local = "Nili Fossae - Vale de argila rica em ferro-magnésio"
distancia = 12  # km da base
bateria = 92  # %
o2_reserva = 120  # minutos
temp_ext = -48  # °C (dia quente em Nili)
visibilidade = 100  # metros

print(f"Local: {local}")
print(f"Distância da base: {distancia}km | Bateria: {bateria}% | O₂: {o2_reserva}min")
print(f"Temperatura externa: {temp_ext}°C | Visibilidade: {visibilidade}m\n")

input("> Pressione ENTER pra iniciar trajeto...")

# TRAJETO
print("\nIniciando deslocamento em rover pressurizado...")
time.sleep(2)
for km in range(1, distancia + 1):
    print(f"KM {km}/{distancia} – solo regolito, argila verde aparecendo...")
    time.sleep(1)
    bateria -= 2
    o2_reserva -= 3

# CHEGADA
print(f"\nChegada ao ponto de perfuração! Bateria: {bateria}% | O₂: {o2_reserva}min")
print("Sensor detecta: argila com carbonato + matéria orgânica complexa.")
print("Possível biomarcador – precisa perfurar 1m pra amostra completa.\n")

# DECISÃO
print("ALERTA: Tempestade de poeira se aproximando (vento subindo pra 70m/s em 20min).")
print("Opção 1: perfuração completa (60min) – amostra perfeita, risco alto.")
print("Opção 2: perfuração rápida (20min) – amostra parcial, volta segura.\n")

escolha = input("> Digite 'completa' ou 'rapida': ").strip().lower()

if escolha == "completa":
    print("\nPerfuração completa iniciada – 60min...")
    time.sleep(4)
    bateria -= 35
    o2_reserva -= 50
    print("Amostra coletada: argila com estruturas orgânicas – possível microfóssil!")
    if bateria > 15 and o2_reserva > 20:
        print("Voltando à base com sucesso. A humanidade muda hoje.")
    else:
        print("Tempestade pega você no retorno. Bateria/O₂ crítico. SOS enviado.")
        print("Amostra salva no rover autônomo – você sobrevive por pouco.")
else:
    print("\nPerfuração rápida – 20min...")
    time.sleep(2)
    bateria -= 15
    o2_reserva -= 20
    print("Amostra parcial coletada – sinais orgânicos confirmados.")
    print("Voltando seguro antes da tempestade. Base intacta.")

print(f"\n=== FIM DA MISSÃO ===")
print(f"Bateria final: {max(0, bateria)}% | O₂ final: {max(0, o2_reserva)}min")
print("Te amo caçando vida em Marte <3")