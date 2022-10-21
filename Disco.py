class Disco:

    def __init__(self):
        self.numdiscos = 0
        self.comecar = False
        self.mover = 0
        self.controle = False

    def quantDisco(self):
        self.comecar
        self.numdiscos
        self.numdiscos = 0
        while (self.comecar == False):
            self.controle = input("\nDigite o número de discos para o jogo iniciar: ")
            for i in range(100):
                if self.controle == i.__str__():
                   self.numdiscos = self.controle

            if self.numdiscos != "" and int(self.numdiscos) >= 3:
                self.comecar = True
            else:
                print("A quantidade minima de disco para iniciar o jogo deve ser de 3 discos.")