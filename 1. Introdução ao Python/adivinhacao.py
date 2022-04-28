# -*- coding: utf-8 -*-
"""

Criado por: Everton dos Santos

Código criado durante a trilha de aprendizado Python na Alura.
Curso: Python 3 parte 1: Introdução à nova versão da linguagem

"""
def jogar():

    import random as rd
    
    
    print("*********************************")
    print("Bem vindo ao jogo da Adivinhação!")
    print("*********************************")
    
    numero_secreto = round(rd.randrange(1,101))
    tentativas = 0
    pontos = 1000
    
    print("Qual nível de dificuldade?")
    print("(1) Fácil  (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível para jogar: "))
    
    if(nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5
    
    
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))    
        palpite = int(input("Digite um número entre 1 e 100: "))
    
        
        
        if(palpite < 1 or palpite > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue
        
        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto
        
        
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else: 
            if(maior): 
                print("O seu chute foi maior que o número secreto")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
                
            elif(menor):
                print("O seu chute foi menor que o número secreto")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        
          
            pontos_perdidos = abs(palpite - numero_secreto)
            pontos = pontos - pontos_perdidos
        
                
    print("Acabou o jogo!")
    
if(__name__ == "__main__"):
    jogar()