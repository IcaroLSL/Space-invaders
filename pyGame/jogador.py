import pygame

class nave():
    def __init__(self, configuracaoDoJogo, tela):
        self.tela = tela
        self.configuracaoDoJogo = configuracaoDoJogo
        self.imagem = pygame.image.load('imagens/jogador.png')
        self.imagem = pygame.transform.scale(self.imagem, (40, 60))
        self.retangulo = self.imagem.get_rect()
        self.retanguloDaTela = tela.get_rect()
        self.retangulo.centerx = self.retanguloDaTela.centerx
        self.retangulo.bottom = self.retanguloDaTela.bottom

    def blitme(self):
        self.tela.blit(self.imagem, self.retangulo)