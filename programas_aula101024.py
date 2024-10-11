#LÓGICA DE PROGRAMAÇÃO
# COM PYTHON   -   Aula 10-10-24
#          www.programiz.com/
#Variável de memória 
nome = "Maria "   # Variável tipo String (texto)
idade =16          # varíavel tipo inteiro
valor = 23.89      # variável tipo FLOAT (Double ou ponto flutuante)
ativo = True       # vaiável do tipo Lógica 
#Comando print , mostra conteúdo de memória
#print("Bom dia!")
valor1=20
valor2=2
resultado=valor1+valor2
#print(resultado)

-----------------------------------
Exmeplo 2
nome="Carlos"
idade=15
valor=20.5
e=True
print("O valor da variavel idade vezes 2 é ",idade*2)
print("A variavel nome e do tipo",type(nome))
print("A variavel idade e do tipo,,, ",type(idade))
print("A variavel valor e do tipo, ",type(valor))
print("A variavel 'e' , e do tipo ",type(e))

-----------------------------------
Exemplo 3
jogador="Lima"
nivel=5
credito=10
vida=2       # Armazena o numero de vidas do personagem principal
if vida>0:
    print("continua no Jogo")
else:
    print("Voce ta fora do jogo")
print("Fim do jogo")  
print("--------------------")
if nivel==1:
    print("codigos do nivel 1")
elif nivel==2:
    print("codigos do nivel 2")
elif nivel==3:
    print("codigos do nivel 3")
elif nivel==4:
    print("codigo do nivel 4")
else:
    print("Nivel Não liberado!")
print("fim de jogo")    
    
-------------------------------------
Exemplo 4
print("----- Digite os dados -------")
nome=input("Digite nome Jogador: ")
nivel=int(input("Digite o nivel:"))
if nivel==1:
    print("Nesse nivel você terá que passar pela ponte sul, cuidado com os espinhos")
elif nivel==2:
    print("Você terá que sobreviver por 2 dias sem dormir, cuidado não passe pela gruta")
elif nivel ==3:    
    print("Nível não disponivel")
else:
    print("Nivel invalido, escolha entre os niveis 1 a 3, tente novamente")

----------------------------------
Exemplo 5
n=10
while n<5:
    print("ETEC - Curso Jogos Digitais")
    n=n+1
-----------------------
