# Dia 3 de mil - Simulação MOXIE - Lucas Motta - 13/12/2025
# Simula produção de O2 do MOXIE: CO2 -> O2 a 800°C
import random  # Pra "ruído" realista (poeira, falhas)

# Parâmetros reais do MOXIE (baseado em testes NASA 2025)
temp_min = 780  # °C mínimo pra funcionar
temp_max = 820  # °C ideal
eficiencia = 0.9  # 90% real em testes
co2_entrada = 10  # L/min de CO2 marciano (atmosfera 96%)
tempo_hora = 1  # Simula 1 hora

print("=== SIMULAÇÃO MOXIE - REATOR EM MARTE ===")
print(f"Iniciando: Temperatura alvo = {random.uniform(temp_min, temp_max):.1f}°C")
print(f"CO2 entrada: {co2_entrada} L/min")

o2_produzido = 0
for minuto in range(60):  # Loop de 1 hora (60 min)
    temp_atual = random.uniform(temp_min - 50, temp_max + 20)  # Variação "real" (falhas)
    if temp_atual >= temp_min:
        # Eletrólise: 2 CO2 -> 2 CO + O2 (simplificado)
        o2_minuto = co2_entrada * 0.5 * eficiencia * (temp_atual / 800)  # Fórmula básica
        o2_produzido += o2_minuto
        status = "Produzindo O2!"
    else:
        status = "FALHA: Temp baixa - verifique filtro poeira!"
        print(f"Min {minuto+1}: {status} Temp: {temp_atual:.1f}°C")
    
    if minuto % 10 == 0:  # Log a cada 10 min
        print(f"Min {minuto+1}: {status} Temp: {temp_atual:.1f}°C O2 acumulado: {o2_produzido:.2f}g")

print(f"\n=== FIM DA HORA ===")
print(f"O2 produzido: {o2_produzido:.2f}g (meta real: 100g/hora em MOXIE 2.0)")
print("Próximo: Adicionar script de troubleshooting (falha filtro).")
print("Te amo, Arazinha <3")