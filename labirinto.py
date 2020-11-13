import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    pygame.init()
    pygame.font.init() # lib para texto

    vezes = 0
    sair = True
    azul = (31,41,133)
    amarelo = (243, 254, 37)
    preto = (0,0,0)
    vermelho = (227, 57, 9)
    verde = (152, 231, 114)
    branco = (255,255,255)
    tela = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Labirinto, by Caio')
    relogio = pygame.time.Clock()

    fundo = pygame.Rect(0,0,800,600)
    tela_venceu = pygame.Surface((800,600))
    sup = pygame.Rect(0,0,800,5)
    sup2 = pygame.Rect(0,550,800,50)
    sup3 = pygame.Rect(2,0,100,600)
    sup4 = pygame.Rect(650,0,200,600)
    sup5 = pygame.Rect(100,500,500,30)
    sup6 = pygame.Rect(150,450,500, 30)
    sup7 = pygame.Rect(100,350,500, 30)
    sup8 = pygame.Rect(150,220,500, 30)
    sup9 = pygame.Rect(100,90,500, 30)
    final = pygame.Rect(102,530,20,20)

    jogador = pygame.Rect(10,10,10,10)
    menu = pygame.Surface((800,600))
    menu.fill(preto)
    tela_venceu.fill(branco)


    pygame.font.init()

    font = pygame.font.get_default_font()
    opcao = pygame.font.SysFont(font, 20)
    venceu = pygame.font.SysFont(font,100)


    pygame.mouse.set_pos(115, 40)

    while sair:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(600,530)
            comandos = pygame.key.get_pressed()
            if comandos[pygame.K_0]:
                sair = False
        pygame.draw.rect(tela,preto,fundo)
       # tela.blit(fundo, [0, 0])
        tela.fill(amarelo)
        pygame.draw.rect(tela, preto, sup)
        pygame.draw.rect(tela, preto, sup2)
        pygame.draw.rect(tela, preto, sup3)
        pygame.draw.rect(tela, preto, sup4)
        pygame.draw.rect(tela, preto, sup5)
        pygame.draw.rect(tela, preto, sup6)
        pygame.draw.rect(tela, preto, sup7)
        pygame.draw.rect(tela, preto, sup8)
        pygame.draw.rect(tela, preto, sup9)
        pygame.draw.rect(tela, vermelho, final)






        pygame.draw.rect(tela, azul, jogador)
        (xant, yant) = (jogador.left, jogador.top)
        (jogador.left, jogador.top) = pygame.mouse.get_pos()
        jogador.left -= jogador.width / 2
        jogador.top -= jogador.height / 2

        if jogador.colliderect(sup):

            pygame.mouse.set_pos(115, 40)
            vezes+=1
        if jogador.colliderect(sup2):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(sup3):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(sup4):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(sup5):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(sup6):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(sup7):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(sup8):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(sup9):
            pygame.mouse.set_pos(115, 40)
            vezes += 1
        if jogador.colliderect(final):

            tela.blit(tela_venceu,[0,0])
            (jogador.left, jogador.top) = (xant,yant)
            text = venceu.render('Voce conseguiu!!! ', 1, (preto))
            tela.blit(text, (140,200))
            text = opcao.render('Pressione 0 para sair ', 1, (preto))
            tela.blit(text, (140, 350))
            text = opcao.render('Muito obrigado por jogar ', 1, (preto))
            tela.blit(text, (140, 400))
            if comandos[pygame.K_0]:
                sair = False

        text = opcao.render('Pressione 0 para sair',1 , (255,255,255))
        tela.blit(text,(660,10))
        text = opcao.render('Labirinto!!!', 1, (255, 255, 255))
        tela.blit(text, (660, 30))
        text = opcao.render('Chegue ao ', 1, (255, 255, 255))
        tela.blit(text, (660, 50))
        text = opcao.render('final sem', 1, (255, 255, 255))
        tela.blit(text, (660, 70))
        text = opcao.render('encostar em', 1, (255, 255, 255))
        tela.blit(text, (660, 90))
        text = opcao.render('NADA', 1, (255, 255, 255))
        tela.blit(text, (660, 110))
        text = opcao.render('Voce encostou: ' + str(vezes)+' vezes', 1, (255, 255, 255))
        tela.blit(text, (655, 150))
        text = opcao.render('De: Caio ' , 1, (255, 255, 255))
        tela.blit(text, (655, 500))
        relogio.tick(40)

        pygame.display.update()

pygame.quit()
main()