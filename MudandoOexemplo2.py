import pygame
import random

pygame.init()

largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desvie do bloco!")

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (200, 0, 0)
azul = (0, 80, 200)

player_x = largura // 2
player_y = altura - 50
player_vel = 5
player_tam = 40

obs_x = random.randint(0, largura - 40)
obs_y = -50
obs_vel = 5
obs_tam = 40

pontos = 0
fonte = pygame.font.SysFont(None, 40)

relogio = pygame.time.Clock()
rodando = True

while rodando:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_ESCAPE]:
        rodando = False
    if teclas[pygame.K_a] and player_x > 0:
        player_x -= player_vel
    if teclas[pygame.K_d] and player_x < largura - player_tam:
        player_x += player_vel   
    if teclas[pygame.K_SPACE] and player_y > 0:
        player_y += player_vel

    # Movimento do obstáculo
    obs_y += obs_vel

    # Resetar obstáculo e aumentar pontuação
    if obs_y > altura:
        obs_y = - obs_tam
        obs_x = random.randint(0, largura - obs_tam)
        pontos += 1
        obs_vel += 0.2

    # Criar retângulos corretos
    jogador = pygame.Rect(player_x, player_y, player_tam, player_tam)
    obstaculo = pygame.Rect(obs_x, obs_y, obs_tam, obs_tam)

    # Colisão
    if jogador.colliderect(obstaculo):
        print("Game Over!")
        rodando = False

    # --- DESENHO ---
    tela.fill(branco)
    pygame.draw.rect(tela, azul, jogador)
    pygame.draw.rect(tela, vermelho, obstaculo)

    texto = fonte.render(f"Pontos: {pontos}", True, preto)
    tela.blit(texto, (10, 10))
    

    pygame.display.update()  

pygame.quit()