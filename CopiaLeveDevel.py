import pygame
import sys

pygame.init()

# --- CONFIGURAÇÕES ---
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Level Devil - Versão Simples")

clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 0, 0)
AZUL = (50, 120, 255)
VERDE = (0, 200, 0)
CINZA = (150, 150, 150)

# Player
player = pygame.Rect(100, 450, 40, 60)
vel_x = 0
vel_y = 0
gravidade = 0.8
no_chao = False

# Plataformas normais
plataformas = [
    pygame.Rect(0, 520, 800, 80),
    pygame.Rect(300, 420, 150, 20),
    pygame.Rect(550, 350, 150, 20),
]

# --- ARMADILHAS TIPO LEVEL DEVIL ---

# Espinho invisível (aparece só quando o jogador encosta)
espinho_invisivel = pygame.Rect(430, 500, 40, 20)
espinho_visivel = False

# Bloco surpresa que se move rapidamente
bloco_movel = pygame.Rect(200, 480, 80, 20)
bloco_ativado = False

# Chão falso
chao_falso = pygame.Rect(600, 520, 120, 20)
chao_desaba = False
chao_vel_y = 0


# ======================================================
# LOOP DO JOGO
# ======================================================
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimento lateral
    vel_x = 0
    if teclas[pygame.K_a]:
        vel_x = -5
    if teclas[pygame.K_d]:
        vel_x = 5

    # Pulo
    if teclas[pygame.K_SPACE] and no_chao:
        vel_y = -15
        no_chao = False

    # Gravidade
    vel_y += gravidade

    # Movimento do player
    player.x += vel_x
    player.y += vel_y

    # Colisões com plataformas
    no_chao = False
    for p in plataformas:
        if player.colliderect(p):
            if vel_y > 0:  # caindo
                player.bottom = p.top
                vel_y = 0
                no_chao = True

    # --- ARMADILHA: ESPINHO INVISÍVEL ---
    if player.colliderect(espinho_invisivel):
        espinho_visivel = True  # aparece!
        player.x, player.y = 100, 450  # reset
        vel_y = 0

    # --- ARMADILHA: BLOCO QUE DISPARA ---
    if abs(player.x - bloco_movel.x) < 120:
        bloco_ativado = True

    if bloco_ativado:
        bloco_movel.x += 10
        if bloco_movel.x > 900:  # some da tela
            bloco_movel.x = -200

    if player.colliderect(bloco_movel):
        player.x, player.y = 100, 450
        vel_y = 0

    # --- ARMADILHA: CHÃO FALSO ---
    if player.colliderect(chao_falso):
        chao_desaba = True

    if chao_desaba:
        chao_vel_y += 1
        chao_falso.y += chao_vel_y

    # Se cair no buraco → reinicia
    if player.y > 700:
        player.x, player.y = 100, 450
        vel_y = 0
        chao_falso.y = 520
        chao_vel_y = 0
        chao_desaba = False
        bloco_ativado = False
        espinho_visivel = False

    # --- DESENHO ---
    tela.fill(BRANCO)

    # Player
    pygame.draw.rect(tela, AZUL, player)

    # Plataformas
    for p in plataformas:
        pygame.draw.rect(tela, CINZA, p)

    # Chão falso
    pygame.draw.rect(tela, VERDE, chao_falso)

    # Bloco surpresa
    pygame.draw.rect(tela, PRETO, bloco_movel)

    # Espinho invisível (vermelho só quando aparece)
    if espinho_visivel:
        pygame.draw.rect(tela, VERMELHO, espinho_invisivel)

    pygame.display.flip()
    clock.tick(60)