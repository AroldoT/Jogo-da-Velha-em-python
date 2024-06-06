# Jogo da velha

jogo = ["_","|","_","|","_","\n","_","|","_","|","_","\n"," ","|"," ","|"," "]
# Index do jogo
# 0, 2, 4
# 6, 8, 10
# 12, 14, 16
print("""
Vamos jogar o jogo da velha,
o jogador deve informar
qual é a linha e a coluna sem
pontuação. O jogador 1 será o "X" e
o jogador 2 será "O"

       coluna 1 2 3
linha 1       _|_|_
linha 2       _|_|_
linha 3        | | 
""")
count1 = 0
count2 = 0

while True:
    if "_" not in jogo and " "not in jogo:
        print("O jogo deu em empate. :(")
        break
    jogador1 = int(input("Escolha o local para marcar o X: "))
    if jogador1 == 11 and jogo[0] != "X" and jogo[0] != "O":
        jogo[0] = "X"
    elif jogador1 == 12 and jogo[2] != "X" and jogo[2] != "O":
        jogo[2] = "X"
    elif jogador1 == 13 and jogo[4] != "X" and jogo[4] != "O":
        jogo[4] = "X"
    elif jogador1 == 21 and jogo[6] != "X" and jogo[6] != "O":
        jogo[6] = "X"
    elif jogador1 == 22 and jogo[8] != "X" and jogo[8] != "O":
        jogo[8] = "X"
    elif jogador1 == 23 and jogo[10] != "X" and jogo[10] != "O":
        jogo[10] = "X"
    elif jogador1 == 31 and jogo[12] != "X" and jogo[12] != "O":
        jogo[12] = "X"
    elif jogador1 == 32 and jogo[14] != "X" and jogo[14] != "O":
        jogo[14] = "X"
    elif jogador1 == 33 and jogo[16] != "X" and jogo[16] != "O":
        jogo[16] = "X"
    else:
        print("Você escolheu um valor não válido.")
        continue
    jogoView = "".join(jogo)
    print(jogoView)
    if jogo[0] == jogo[2] == jogo[4] == "X" or jogo[0] == jogo[8] == jogo[16] == "X" or jogo[0] == jogo[6] == jogo[12] == "X" or jogo[12] == jogo[8] == jogo[4] == "X" or jogo[16] == jogo[10] == jogo[4] == "X" or jogo[12] == jogo[14] == jogo[16] == "X" or jogo[14] == jogo[8] == jogo[4] == "X" or jogo[6] == jogo[8] == jogo[10] == "X":
        print("Parabens o jogador 1 venceu.")
        count1 += 1
        break

    jogador2 = int(input("Escolha o local para marcar o O: "))
    if jogador2 == 11 and jogo[0] != "X" and jogo[0] != "O":
        jogo[0] = "O"
    elif jogador2 == 12 and jogo[2] != "X" and jogo[2] != "O":
        jogo[2] = "O"
    elif jogador2 == 13 and jogo[4] != "X" and jogo[4] != "O":
        jogo[4] = "O"
    elif jogador2 == 21 and jogo[6] != "X" and jogo[6] != "O":
        jogo[6] = "O"
    elif jogador2 == 22 and jogo[8] != "X" and jogo[8] != "O":
        jogo[8] = "O"
    elif jogador2 == 23 and jogo[10] != "X" and jogo[10] != "O":
        jogo[10] = "O"
    elif jogador2 == 31 and jogo[12] != "X" and jogo[12] != "O":
        jogo[12] = "O"
    elif jogador2 == 32 and jogo[14] != "X" and jogo[14] != "O":
        jogo[14] = "O"
    elif jogador2 == 33 and jogo[16] != "X" and jogo[16] != "O":
        jogo[16] = "O"
    else:
        print("Você escolheu um valor não válido.")
        continue
    jogoView = "".join(jogo)
    print(jogoView)
    if jogo[0] == jogo[2] == jogo[4] == "O" or jogo[0] == jogo[8] == jogo[16] == "O" or jogo[0] == jogo[6] == jogo[12] == "O" or jogo[12] == jogo[8] == jogo[4] == "O" or jogo[16] == jogo[10] == jogo[4] == "O" or jogo[12] == jogo[14] == jogo[16] == "O" or jogo[14] == jogo[8] == jogo[4] == "O" or jogo[6] == jogo[8] == jogo[10] == "O":
        print("Parabens o jogador 2 venceu.")
        count2 += 1
        break

# print(f"O placar esta assim:\n jogador 1 - {count1} e jogador 2 - {count2}")
