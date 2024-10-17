import pygame
import sys
#jogo pond
#contador de tempo
#feito IA - ChatGPT
#11-10-24
# Inicializa o Pygame
pygame.init()

# Define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Define as dimensões da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Configura as raquetes e a bola
raquete_largura = 15
raquete_altura = 100
raquete_velocidade = 7

bola_diametro = 15
bola_velocidade_x = 5
bola_velocidade_y = 5

# Posições iniciais
raquete_esquerda_y = (ALTURA - raquete_altura) // 2
raquete_direita_y = (ALTURA - raquete_altura) // 2
bola_x = LARGURA // 2
bola_y = ALTURA // 2

# Inicializa o cronômetro
tempo_inicial = pygame.time.get_ticks()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete_esquerda_y > 0:
        raquete_esquerda_y -= raquete_velocidade
    if teclas[pygame.K_s] and raquete_esquerda_y < ALTURA - raquete_altura:
        raquete_esquerda_y += raquete_velocidade
    if teclas[pygame.K_UP] and raquete_direita_y > 0:
        raquete_direita_y -= raquete_velocidade
    if teclas[pygame.K_DOWN] and raquete_direita_y < ALTURA - raquete_altura:
        raquete_direita_y += raquete_velocidade

    # Movimento da bola
    bola_x += bola_velocidade_x
    bola_y += bola_velocidade_y

    # Verifica colisões com as paredes
    if bola_y <= 0 or bola_y >= ALTURA - bola_diametro:
        bola_velocidade_y *= -1

    # Verifica colisões com as raquetes
    if (bola_x <= raquete_largura and raquete_esquerda_y < bola_y < raquete_esquerda_y + raquete_altura) or \
            (
                    bola_x >= LARGURA - raquete_largura - bola_diametro and raquete_direita_y < bola_y < raquete_direita_y + raquete_altura):
        bola_velocidade_x *= -1

    # Reinicia a bola se sair da tela
    if bola_x < 0 or bola_x > LARGURA:
        bola_x = LARGURA // 2
        bola_y = ALTURA // 2
        bola_velocidade_x *= -1

    # Desenha tudo
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, (0, raquete_esquerda_y, raquete_largura, raquete_altura))
    pygame.draw.rect(tela, BRANCO, (LARGURA - raquete_largura, raquete_direita_y, raquete_largura, raquete_altura))
    pygame.draw.ellipse(tela, BRANCO, (bola_x, bola_y, bola_diametro, bola_diametro))

    # Atualiza o cronômetro
    tempo_passado = (pygame.time.get_ticks() - tempo_inicial) // 1000  # Tempo em segundos
    fonte = pygame.font.Font(None, 36)
    texto_tempo = fonte.render(f'Tempo: {tempo_passado} s', True, BRANCO)
    tela.blit(texto_tempo, (10, 10))  # Desenha o texto na tela

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limita a 60 frames por segundo
