alturas = []
generos = []

for i in range(3):
    
    while True:
        entrada = input("Altura: ").replace(",", ".")
        try:
            altura = float(entrada)
            if 0.5 <= altura <= 3.0:
                break
            else:
                print("⚠️ Digite uma altura entre 0,50 m e 3,00 m.")
        except ValueError:
            print("⚠️ Digite um valor numérico válido (ex: 1.75 ou 1,75).")

    
    while True:
        genero = input("Gênero (M/F): ").upper()
        if genero in ["M", "F"]:
            break
        else:
            print("⚠️ Digite apenas M ou F.")

    alturas.append(altura)
    generos.append(genero)


soma_homens = 0
qtd_homens = 0

for i in range(3):
    if generos[i] == "M":
        soma_homens += alturas[i]
        qtd_homens += 1

media_homens = soma_homens / qtd_homens if qtd_homens > 0 else 0

print("\n--- Dados armazenados ---")
for i in range(3):
    print(f"Pessoa {i+1}: Altura = {alturas[i]} | Gênero = {generos[i]}")

print(f"\nMédia da altura dos homens: {media_homens:.2f} m")




