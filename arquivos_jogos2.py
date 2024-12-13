
#https://www.hashtagtreinamentos.com/jogo-snake-em-python?gad_source=1&gclid=EAIaIQobChMIwL2ZgYiiigMVb2FIAB1RoRwaEAAYASAAEgJlQvD_BwE

# configurações iniciais

import pygame

import random

pygame.init()

pygame.display.set_caption("Jogo Snake Python")

largura, altura = 1200, 800

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

# cores RGB

preta = (0, 0, 0)

branca = (255, 255, 255)

vermelha = (255, 0, 0)

verde = (0, 255, 0)

# parametros da cobrinha

tamanho_quadrado = 20

velocidade_jogo = 15

def gerar_comida():

    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):

    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):

    for pixel in pixels:

        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):

    fonte = pygame.font.SysFont("Helvetica", 35)

    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)

    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):

    if tecla == pygame.K_DOWN:

        velocidade_x = 0

        velocidade_y = tamanho_quadrado

    elif tecla == pygame.K_UP:

        velocidade_x = 0

        velocidade_y = -tamanho_quadrado

    elif tecla == pygame.K_RIGHT:

        velocidade_x = tamanho_quadrado

        velocidade_y = 0

    elif tecla == pygame.K_LEFT:

        velocidade_x = -tamanho_quadrado

        velocidade_y = 0

    return velocidade_x, velocidade_y

def rodar_jogo():

    fim_jogo = False

    x = largura / 2

    y = altura / 2

    velocidade_x = 0

    velocidade_y = 0

    tamanho_cobra = 1

    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:

        tela.fill(preta)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                fim_jogo = True

            elif evento.type == pygame.KEYDOWN:

                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar_comida

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posicao da cobra

        if x < 0 or x >= largura or y < 0 or y >= altura:

            fim_jogo = True

        x += velocidade_x

        y += velocidade_y

        # desenhar_cobra

        pixels.append([x, y])

        if len(pixels) > tamanho_cobra:

            del pixels[0]

        # se a cobrinha bateu no proprio corpo

        for pixel in pixels[:-1]:

            if pixel == [x, y]:

                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        # desenhar_pontos

        desenhar_pontuacao(tamanho_cobra - 1)

        # atualizacao da tela

        pygame.display.update()

        # criar uma nova comida

        if x == comida_x and y == comida_y:

            tamanho_cobra += 1

            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

rodar_jogo()




#https://cursos.alura.com.br/forum/topico-jogo-da-cobrinha-usando-apenas-while-e-if-else-77405
def jogar():

    print("Bem vindo ao jogo da Cobrinha")

    nlinhas  = int((input("Digite o número de linhas: ")))
    ncolunas = int((input("Digite o número de colunas: ")))
    x0       = int((input("Digite a posicao x inicial: ")))
    y0       = int((input("Digite a posicao y inicial: ")))
    x        = x0 + 1
    y        = y0
    borda    = 2

    tabuleiro(nlinhas, ncolunas, x0, y0, x, y)
    mover_direita  = False
    mover_esquerda = False
    mover_cima     = False
    mover_baixo    = False

    while x < (ncolunas + borda) and y < (nlinhas + borda):

        mover = int(input("Digite os números para mover a cobra: 1 para cima, 2 para baixo, 3 para esquerda ou 4 para direita: "))

        if(mover == 1):
            mover_direita  = False
            mover_esquerda = False
            mover_cima     = True
            mover_baixo    = False
        if(mover == 2):
            mover_direita  = False
            mover_esquerda = False
            mover_cima     = False
            mover_baixo    = True
        if(mover == 3):
            mover_direita  = False
            mover_esquerda = True
            mover_cima     = False
            mover_baixo    = False
        if(mover == 4):
            mover_direita  = True
            mover_esquerda = False
            mover_cima     = False
            mover_baixo    = False

        if mover_direita:
            x  = x + 1

            tabuleiro(nlinhas, ncolunas, x0, y0, x, y)

        if mover_esquerda:
            x  = x - 1
            if x0 == y or x0 == x:
                print("Fim do Jogo")
            else:
                tabuleiro(nlinhas, ncolunas, x0, y0, x, y)

        if mover_baixo:
            y = y + 1

            tabuleiro(nlinhas, ncolunas, x0, y0, x, y)

        if mover_cima:
            y = y - 1

            tabuleiro(nlinhas, ncolunas, x0, y0, x, y)


        if(x == ncolunas + borda - 1) or (y == nlinhas + borda - 1) or x == 1 or y == 1:
            print("Fim do jogo")


def tabuleiro(nlinhas, ncolunas, x0, y0, x, y):

    borda     = 2

    contador_y = 1
    contador_x = 1
    contador = 1

#Borda

    while contador_x < (ncolunas + borda):
        contador_x = contador_x + 1
        print(" # ", end="")

        if contador_x == (ncolunas + borda):
            print(" # ")


#Tabuleiro

    contador_x = 1

    while contador_y <= (nlinhas + borda):
        contador_y = contador_y + 1
        contador_x = 1

        while contador_x <= (ncolunas + borda):
            contador_x = contador_x + 1

            if contador_x == 2:
                print(" # ", end="")
                contador_x = contador_x + 1

            if x0 == contador_x and y0 == contador_y:
                while x > contador_x:
                    print(" x ", end="")
                    contador_x = contador_x + 1

            if (x == contador_x and (y) == contador_y):
                print(" C ", end="")
                contador_x = contador_x + 1 

            print(" . ", end="")

            if contador_x == ncolunas + borda:
                print(" # ")
                contador_x = contador_x + 1        

#Borda

    contador_x = 1

    while contador_x < (ncolunas + borda):
       contador_x = contador_x + 1
       print(" # ", end="")

       if contador_x == (ncolunas + borda):
           print(" # ")


jogar()




#https://www.hashtagtreinamentos.com/jogo-snake-em-python?gad_source=1&gclid=EAIaIQobChMIwL2ZgYiiigMVb2FIAB1RoRwaEAMYASAAEgKcr_D_BwE
#Terceiro exemplo
# configurações iniciais

import pygame
import random
pygame.init()
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
# parametros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 15
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1
    pixels = []
    comida_x, comida_y = gerar_comida()
    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
        # desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        # atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        x += velocidade_x
        y += velocidade_y
        # desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        # se a cobrinha bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels)
        # desenhar_pontos
        desenhar_pontuacao(tamanho_cobra - 1)
        # atualizacao da tela
        pygame.display.update()
        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        relogio.tick(velocidade_jogo)
rodar_jogo()

