import pygame
import socket
import threading
import sys



SERVER_IP = "192.168.206.1"   # <-- COLOQUE O IP DO SERVIDOR
PORT = 5000

nome = input("Seu nome: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((SERVER_IP, PORT))
except:
    print("Não foi possível conectar ao servidor.")
    sys.exit()

pygame.init()


LARGURA = 600
ALTURA = 500
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Chat em Rede - Pygame")

# CORES
FUNDO = (240, 240, 240)
CHAT_BG = (220, 220, 220)
INPUT_BG = (180, 200, 255)
PRETO = (0, 0, 0)

fonte = pygame.font.Font(None, 28)
fonte_chat = pygame.font.Font(None, 24)

mensagens = []
texto_digitado = ""
limite_mensagens = 14



def receber():
    while True:
        try:
            msg = cliente.recv(1024).decode()
            if msg:
                mensagens.append(msg)
        except:
            break


thread_recv = threading.Thread(target=receber, daemon=True)
thread_recv.start()



def desenhar_chat():
    TELA.fill(FUNDO)

    # Caixa grande do chat
    pygame.draw.rect(TELA, CHAT_BG, (20, 20, 560, 380), border_radius=10)

    # Mostrar mensagens
    y = 35
    for msg in mensagens[-limite_mensagens:]:
        texto_msg = fonte_chat.render(msg, True, PRETO)
        TELA.blit(texto_msg, (30, y))
        y += 25

    # Caixa de digitação
    pygame.draw.rect(TELA, INPUT_BG, (20, 420, 560, 60), border_radius=10)
    txt_input = fonte.render(texto_digitado, True, PRETO)
    TELA.blit(txt_input, (30, 440))


def main():
    global texto_digitado

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cliente.close()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # Enviar ao apertar ENTER
                if event.key == pygame.K_RETURN:
                    if texto_digitado.strip() != "":
                        mensagem_final = f"{nome}: {texto_digitado}"
                        cliente.send(mensagem_final.encode())
                        mensagens.append(mensagem_final)  
                        texto_digitado = ""

                # Apagar com BACKSPACE
                elif event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]

                else:
                    texto_digitado += event.unicode

        desenhar_chat()
        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
