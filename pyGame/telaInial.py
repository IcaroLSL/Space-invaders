import pygame

class telaDoInicio():
    def __init__(self, tela):
        self.imagem = pygame.image.load('imagens/abduzindo vaca.jpg')
        self.tela = tela
        self.rect = self.imagem.get_rect()
        self.rectTela = self.tela.get_rect()

        self.rect.centerx = self.rectTela.centerx
        self.rect.center = self.rectTela.center

    def blitme(self):
        self.tela.blit(self.imagem, self.rect)