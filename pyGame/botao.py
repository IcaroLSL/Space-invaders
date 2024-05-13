import pygame

class botaoInicial():
    def __init__(self, tela, menssagem, botaoWidth = 200, botaoHeight = 50, corDoBotao = (152, 0, 0),
                 corDoTexto = (225,225,225), tamanhoDaFonte = 48):

        self.tela = tela
        self.rectTela = tela.get_rect()
        self.menssagem = menssagem
        self.botaoWidth = botaoWidth
        self.botaoHeight = botaoHeight
        self.corDoBotao = corDoBotao
        self.corDoTexto = corDoTexto
        self.fonte = pygame.font.SysFont(None, tamanhoDaFonte)

        rectTela = self.tela.get_rect()
        centerxDaTela = rectTela.centerx
        centeryDaTela = rectTela.centery

        self.rect = pygame.Rect(centerxDaTela, centeryDaTela, self.botaoWidth, self.botaoHeight)
        self.rect.center = self.rectTela.center

        self.prepararMenssagem(self.menssagem)

    def prepararMenssagem(self, menssagem):
        self.message_image = self.fonte.render(menssagem, True, self.corDoTexto,
                                              self.corDoBotao)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def desenharBotao(self):
        self.tela.fill(color =self.corDoBotao, rect = self.rect)
        self.tela.blit(source = self.message_image, dest = self.message_image_rect)