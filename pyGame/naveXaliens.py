import pygame
from pygame.sprite import Group
import funcoes
from configuracao import configuracao1
import funcoes as f
from jogador import nave
from inimigo import Inimigo
from telaInial import *
from botao import *
def run_game():
    pygame.init()
    configuracaoDoJogo = configuracao1()
    tela = pygame.display.set_mode((configuracaoDoJogo.larguraDaTela, configuracaoDoJogo.alturaDaTela))
    pygame.display.set_caption('navesXaliens')
    nave1 = nave(configuracaoDoJogo, tela)
    inimigos = Group()
    tiros = Group()
    funcoes.createFleet(configuracaoDoJogo, inimigos=inimigos, tela=tela)
    playButton = botaoInicial(tela, "play")
    while True:
        f.olharEventosAtuais(configuracoesDoJogo=configuracaoDoJogo, tela=tela, nave=nave1, tiros=tiros)

        game_active = funcoes.verificarSePerdeu(tela=tela, inimigos=inimigos)
        if game_active and len(inimigos.sprites()) > 0:
            f.atualizarTela(configuracoesDoJogo=configuracaoDoJogo, tela=tela, nave=nave1, inimigos=inimigos, tiros=tiros)
            pygame.sprite.groupcollide(tiros, inimigos, True, True)
            tiros.update()
            funcoes.updateFleet(configuracaoDoJogo, inimigos)

        elif len(inimigos) == 0:
            tiros.empty()
            pygame.time.wait(1000)

            if configuracaoDoJogo.linhasDosInimigosNaTela < 6:
                configuracaoDoJogo.linhasDosInimigosNaTela += 1
            funcoes.createFleet(configuracaoDoJogo, inimigos=inimigos, tela=tela)

        elif not pygame.mouse.get_focused():
            continue
        else:
            screenImage = telaDoInicio(tela=tela)

            funcoes.initial_screen_draw(configuracaoDoJogo, tela, playButton, screenImage)
            pygame.display.flip()

            if funcoes.chek_play_button(playButton, configuracaoDoJogo):
                inimigos.empty()
                tiros.empty()
                funcoes.createFleet(configuracaoDoJogo, inimigos=inimigos, tela=tela)

            pygame.time.Clock().tick(60)


if __name__ == '__main__':
    run_game()
