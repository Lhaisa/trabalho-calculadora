#Calculadoramde aprovação Escolar

nome = input("Lhaisa Rafaela dos Santos Macedo")

soma_notas = 0
quantidade_trimstre = 3
meta_provacao = 180

#Coleta as notas do 3 períodos
for i in range(1, quantidade_trimstre + 1):
    nota = float(input("Informe a nota{i}º período: "))
soma_notas +=nota

print("-"* 30)
print(f"Estudante: {nome}")
print(f"Ponyuação Total: {soma_notas}")

#Verfica o Status de aprovação
if soma_notas >= meta_provacao:
    print("Status: APROVADÃO! PARABÉNS! FINALMENTE!")
else:
    pontos_falantes = meta_provacao - soma_notas
    print("Status: TENTE OUTR VEZ!!!")
    print(f"Faltaram {pontos_falantes} pontos para atingir o mínimo de {meta_provacao}.")
