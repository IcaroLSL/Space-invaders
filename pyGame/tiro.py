import pygame
from pygame.sprite import Sprite

class bala(Sprite):

    def __init__(self, configuracaoDoJogo, tela, nave):

        super(bala, self).__init__()

        self.tela = tela
        self.rect = pygame.Rect(nave.retangulo.centerx, nave.retangulo.top, configuracaoDoJogo.larguraDoTiro,
                                configuracaoDoJogo.alturaDoTiro)
        self.y = float(self.rect.y)
        self.configuracao = configuracaoDoJogo

    def update(self):

        self.rect.y -= self.configuracao.velocidadeDoTiro

        if self.rect.y < 0:
            self.kill()

    def desenhaABala(self):

        pygame.draw.rect(self.tela, self.configuracao.corDoTiro, self.rect)