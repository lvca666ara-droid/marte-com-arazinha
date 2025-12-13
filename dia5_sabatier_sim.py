# Dia 5 de mil - Simulação Sabatier - Lucas Motta - 14/12/2025
import random
import time

# Parâmetros reais (baseado em testes NASA/SpaceX 2025)
temp_min = 300  # °C mínimo pra reação
temp_ideal = 350
eficiencia = 0.95  # 95% em catalisador Ru
co2_entrada = 10  # L/min CO2 marciano
h2_entrada = 40   # L/min H2 (4x CO2 pra reação perfeita)

print("=== SIMULAÇÃO SABATIER - FÁBRICA DE COMBUSTÍVEL MARCIANO ===")
print(f"Iniciando: Temp alvo = {random.uniform(temp_min, temp_ideal + 50):.1f}°C")
print(f"CO2: {co2_entrada} L/min | H2: {h2_entrada} L/min")

ch4_produzido = 0
h2o_produzido = 0
for minuto in range(60):
    temp_atual = random.uniform(temp_min - 50, temp_ideal + 50)
    if temp_atual >= temp_min:
        # Reação: CO2 + 4 H2 → CH4 + 2 H2O
        conversao = eficiencia * (temp_atual / temp_ideal)
        ch4_minuto = co2_entrada * conversao
        h2o_minuto = ch4_minuto * 2  # 2 moléculas H2O por CH4
        ch4_produzido += ch4_minuto
        h2o_produzido += h2o_minuto
        status = "Produzindo CH4!"
    else:
        status = "FALHA: Temp baixa - verifique aquecedor!"
        print(f"Min {minuto+1}: {status} Temp: {temp_atual:.1f}°C")
    
    if minuto % 10 == 0:
        print(f"Min {minuto+1}: {status} Temp: {temp_atual:.1f}°C CH4: {ch4_produzido:.2f}L H2O: {h2o_produzido:.2f}L")

print("\n=== FIM DA HORA ===")
print(f"CH4 produzido: {ch4_produzido:.2f}L (meta: 1.000t pra 1 Starship voltar)")
print(f"H2O produzido: {h2o_produzido:.2f}L (pra beber + mais O2)")
print("Próximo: Troubleshooting (H2 baixo ou catalisador oxidado).")
print("Te amo, Arazinha <3")