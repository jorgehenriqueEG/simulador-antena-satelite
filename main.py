import math

potencia_tx = 100
distancia_km = 36000
ganho_antena = 30

potencia_dbm = 10 * math.log10(potencia_tx * 1000)
distancia_m = distancia_km * 1000
perda_db = 20 * math.log10(distancia_m) + 20 * math.log10(4 * math.pi * 1.2 * 10**9 / 3e8)

potencia_rx = potencia_dbm - perda_db + ganho_antena
limiar = -70

if potencia_rx > limiar:
    print(f"Sinal recebido: {potencia_rx:.2f} dBm. Decodificação possível.")
else:
    print(f"Sinal recebido: {potencia_rx:.2f} dBm. Sinal insuficiente.")