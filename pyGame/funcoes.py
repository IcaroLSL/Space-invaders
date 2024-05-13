import sys
import pygame
from inimigo import Inimigo
from tiro import bala
def olharEventosAtuais(configuracoesDoJogo, tela, nave, tiros):
    pygame.mouse.set_visible(configuracoesDoJogo.visibilidadeDoMouse)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d and nave.retangulo.right<1100:
                nave.retangulo.centerx += 10*configuracoesDoJogo.velocidadeDoJogo
            elif evento.key == pygame.K_a and nave.retangulo.left>100:
                nave.retangulo.centerx -= 10*configuracoesDoJogo.velocidadeDoJogo
        if evento.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pressed(5) == (1,0,0,0,0):

                novoProjetil = bala(configuracaoDoJogo=configuracoesDoJogo, tela=tela, nave=nave)
                tiros.add(novoProjetil)

        elif pygame.mouse.get_focused():
            nave.retangulo.centerx = pygame.mouse.get_pos()[0]

def atualizarTela(configuracoesDoJogo, tela, nave, inimigos, tiros):
    tela.fill(configuracoesDoJogo.corDoCenario)
    for tiro in tiros.sprites():
        tiro.desenhaABala()
    nave.blitme()
    inimigos.draw(tela)
    pygame.display.flip()

def createFleet(configuracaoDoJogo, tela, inimigos):
    inimigo = Inimigo(configuracaoDoJogo, tela)
    inimigoLargura = inimigo.rect.width
    espacoDisponivel = inimigo.rect.height
    numeroDeInimigos = 11

    for linha in range(configuracaoDoJogo.linhasDosInimigosNaTela):
        for numero in range(numeroDeInimigos):
            inimigo = Inimigo(configuracaoDoJogo, tela)
            inimigo.x = inimigoLargura + 1.5 * inimigoLargura * numero
            inimigo.rect.x = inimigo.rect.x + inimigo.x
            inimigo.rect.y = espacoDisponivel + 1 * espacoDisponivel * linha
            inimigos.add(inimigo)

def fleetPositionChek(configuracaoDoJogo, inimigos):
    for inimigo in inimigos.sprites():
        if inimigo.olhaPosicaoDoInimigo() == True:
            fleetDirectionChange(configuracaoDoJogo, inimigos)
            break

def fleetDirectionChange(configuracaoDoJogo, inimigos):
    for inimigo in inimigos.sprites():
        inimigo.rect.y += configuracaoDoJogo.velocidadeQueOInimigoCai
    configuracaoDoJogo.direcaoDoInimigo *= -1

def updateFleet(configuracaoDoJogo, inimigos):
    fleetPositionChek(configuracaoDoJogo, inimigos)
    inimigos.update()

def verificarSePerdeu(tela, inimigos):
    retanguloDaTela = tela.get_rect()
    for inimigo in inimigos.sprites():
        if inimigo.rect.bottom >= retanguloDaTela.bottom:
            return False
    return True

def initial_screen_draw(configuracaoDoJogo, tela, playButton, telaInicial):
    tela.fill(configuracaoDoJogo.corDeFundoDaTelaInicial)
    telaInicial.blitme()
    playButton.desenharBotao()
    pygame.display.flip()

def chek_play_button(botaoInicial, configuracoesDoJogo):
    configuracoesDoJogo.visibilidadeDoMouse = True

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            if botaoInicial.rect.collidepoint(mousex, mousey):
                configuracoesDoJogo.visibilidadeDoMouse = False
                return True
        return False