print("Bem-vindo à criação de histórias interativas!")
cenario = input("Onde se passa a história? ")
personagem = input("Quem é o protagonista? ")
descoberta = input("O que o protagonista encontrou? ")
local = input("Onde o protagonista encontrou isso? ")

historia = (
    f"Em {cenario}, {personagem} estava explorando quando inesperadamente se deparou com {descoberta} "
    f"localizado em {local}. Assim começou uma aventura inesquecível!"
)

print(historia)
