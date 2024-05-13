import pygame
from pygame.sprite import Sprite

class Inimigo(Sprite):
    def __init__(self, configuracaoDoJogo, tela):
        super(Inimigo, self).__init__()
        self.tela = tela
        self.configuracaoDoJogo = configuracaoDoJogo
        self.image = pygame.image.load('imagens/inimigo.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.retanguloDaTela = tela.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.tela.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.configuracaoDoJogo.fatorDeVelocidadeDoInimigo * self.configuracaoDoJogo.direcaoDoInimigo

    def olhaPosicaoDoInimigo(self):
        if self.retanguloDaTela.right <= self.rect.right:
            return True

        elif self.rect.left <= 0:
            return True

        else:
            return False
