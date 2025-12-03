import pygame
import sys

pygame.init()

# Configurações da janela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Boneco com braços e pernas (WASD)")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Posição inicial do boneco
x = 400
y = 300
velocidade = 5

clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimento WASD
    if teclas[pygame.K_w]:
        y -= velocidade
    if teclas[pygame.K_s]:
        y += velocidade
    if teclas[pygame.K_a]:
        x -= velocidade
    if teclas[pygame.K_d]:
        x += velocidade

    # Limpa tela
    tela.fill(BRANCO)

    # --- DESENHO DO BONECO ---
    # Cabeça
    pygame.draw.circle(tela, PRETO, (x, y - 40), 20, 3)

    # Corpo
    pygame.draw.line(tela, PRETO, (x, y - 20), (x, y + 40), 3)

    # Braço esquerdo
    pygame.draw.line(tela, PRETO, (x, y), (x - 30, y - 10), 3)

    # Braço direito
    pygame.draw.line(tela, PRETO, (x, y), (x + 30, y - 10), 3)

    # Perna esquerda
    pygame.draw.line(tela, PRETO, (x, y + 40), (x - 20, y + 80), 3)

    # Perna direita
    pygame.draw.line(tela, PRETO, (x, y + 40), (x + 20, y + 80), 3)

    # Atualiza tela
    pygame.display.flip()
    clock.tick(60)