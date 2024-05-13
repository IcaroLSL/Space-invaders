class configuracao1():

    def __init__(self):
        self.velocidadeDoJogo = 2.5

        #configuracoes da tela do jogo
        self.larguraDaTela = 1200
        self.alturaDaTela = 600
        self.corDoCenario = (255, 255, 255)
        self.corDeFundoDaTelaInicial = (6.7, 7.5, 15.7)
        #configuracao da bala
        self.velocidadeDoTiro = 0.5 * self.velocidadeDoJogo
        self.larguraDoTiro = 3
        self.alturaDoTiro = 15
        self.corDoTiro = (255, 0, 0)

        #cofiguracao do inimigo
        self.velocidadeQueOInimigoCai = 5 * self.velocidadeDoJogo
        #direcao x do inimigo positivo = direita, negativo = esquerda
        self.direcaoDoInimigo = 1
        self.fatorDeVelocidadeDoInimigo = 0.4 * self.velocidadeDoJogo
        self.linhasDosInimigosNaTela = 1

        self.visibilidadeDoMouse = False