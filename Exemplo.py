import pygame
import sys

# Inicializa o pygame
pygame.init()


#Define tamanho da janela
largura, altura = 1440, 900
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo Pygame - Movendo um Quadrado")


#Define propriedade do jogador
x = 300
y = 200
velocidade = 1
tamanho = 40

#Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#Teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        x -= velocidade
    if teclas[pygame.K_d]:
        x += velocidade
    if teclas[pygame.K_w]:
        y -= velocidade
    if teclas[pygame.K_s]:
        y += velocidade


# Preenche a tela com preto
    janela.fill((0,0,0))


#Desenha o quadrado(vemelho)
    pygame.draw.rect(janela, (0, 255, 255), (x, y, tamanho, tamanho))


# Atualiza a tela
    pygame.display.update()