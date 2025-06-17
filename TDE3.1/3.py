Pais_A = 80000
Pais_B = 200000
anos = 0
while Pais_A < Pais_B:
    Pais_A = Pais_A + Pais_A * 0.03
    Pais_B = Pais_B + Pais_B * 0.015
    anos += 1
print(f"população: Pais_A = {Pais_A}, Pais_B = {Pais_B}, anos até o pais A ultrapassar o Pais B em habitantes = {anos}")