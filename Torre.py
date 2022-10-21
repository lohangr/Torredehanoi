from Disco import Disco
import sys

disco = Disco()

class Torre:

    def __init__(self):
        self.torre1 = []
        self.torre2 = []
        self.torre3 = []

    def init(self):
        for i in range(0, int(disco.numdiscos)):
            self.torre1.append(int(disco.numdiscos) - i)
        return True

    def printTorre(self, arrayTorre, torre):
        print('{:>{}}'.format("\nTorre ", (disco.numdiscos)) + torre)
      
    def verificarMovimento(self, str):
        strView = ""
        if str == "1":
            strView = "2 ou 3"
        elif (str == "2"):
            strView = "1 ou 3"
        elif (str == "3"):
            strView = "1 ou 2"
        return strView


    def movimentar(self, torre, operacao, valorMove):
        movimento = ""

        if (torre == "1" ) and operacao == 1:
            if self.validaAlocacao(self.torre1, operacao, valorMove):
                movimento = self.torre1.pop()
        elif (torre == "2") and operacao == 1:
            if self.validaAlocacao(self.torre2, operacao, valorMove):
                movimento = self.torre2.pop()
        elif (torre == "3") and operacao == 1:
            if self.validaAlocacao(self.torre3, operacao, valorMove):
                movimento = self.torre3.pop()
        elif (torre == "1") and operacao == 2:
            if self.validaAlocacao(self.torre1, operacao, valorMove):
                self.torre1.append(valorMove)
                movimento = valorMove
        elif (torre == "2") and operacao == 2:
            if self.validaAlocacao(self.torre2, operacao, valorMove):
                self.torre2.append(valorMove)
                movimento = valorMove
        elif (torre == "3") and operacao == 2:
            if self.validaAlocacao(self.torre3, operacao, valorMove):
                self.torre3.append(valorMove)
                movimento = valorMove
        return movimento


    def inputValue(self):
        saida = ""
        movSaida = ""
        entrada = ""
        movEntrada = ""
        disco.controle = False
        reiniciar = False
        novaPartida = False

        while saida == "":

            if movSaida == "" and disco.controle != False:
                print("Torre incorreta, digite novamente.")
                disco.controle = False
            else:
                print("\nPara reiniciar a jogada digite [ reiniciar ] ")
                print("Para iniciar novamente a partida digite [ iniciar ] ")
                print("Para exibir o resultado anterior digite [ exibir ]\n")
                saida = input("Informe a Torre de Saida: ")

                if saida == "reiniciar":
                    reiniciar = True
                elif saida == "exibir":
                    self.printResult()
                    reiniciar = True
                elif saida == "iniciar":
                    novaPartida = True
                else:
                    movSaida = self.verificarMovimento(saida)
                    disco.controle = True

            if not reiniciar and not novaPartida:
                saida = self.movimentar(saida, 1, "")

        disco.controle = False

        while entrada == "" and (not reiniciar and not novaPartida):

            if movEntrada == "" and disco.controle != False:
                print("A Torre informada esta errada, por favor informe uma torre valida.")
                disco.controle = False
            else:
                entrada = input("Informe a Torre de Entrada " + movSaida + ": ")

                if entrada == "reiniciar":
                    self.reiniciar = True
                elif entrada == "exibir":
                    self.printResult()
                    reiniciar = True
                elif entrada == "iniciar":
                    self.novaPartida = True
                else:
                    movEntrada = self.verificarMovimento(entrada)

                    if movSaida == movEntrada:
                        print("Esse movimento é inválido. Tente outro movimento.")
                        disco.controle = False
                    else:
                        disco.controle = True

            if disco.controle:
                entrada = self.movimentar(entrada, 2, saida)
            else:
                entrada = ""

        if reiniciar:
            self.inputValue()
        elif novaPartida:
            self.iniciar()


    def validaAlocacao(self, torre, operacao, valorMove):
        length = torre.__len__()

        if length == 0 and operacao == 1:
            print("Esta torre esta vazia. Mude sua jogada.")
            return False
        elif length > 0 and operacao == 2:
            if valorMove < torre[length - 1]:
                return True
            else:
                print("O ultimo disco que esta na torre è menor que o disco [", valorMove, "]. Mude sua jogada!")
                return False
        else:
            return True


    def validaResultado(self):
        vencedor = False

        if int(self.torre1.__len__()) == 0 and int(self.torre2.__len__()) == 0 and int(self.torre3.__len__()) == int(self.numdiscos):
            vencedor = True
        elif int(self.torre1.__len__()) == 0 and int(self.torre2.__len__()) == int(self.numdiscos) and int(self.torre3.__len__()) == 0:
            vencedor = True

        return vencedor


    def fimJogo(self):
        print("Fim de jogo!")

        if input("Para uma nova partida digite [ iniciar ], se quiser digite qualquer tecla!:  ") == "iniciar":
            self.iniciar()
        else:
            print("Obrigado por jogar!\n")
            sys.exit(0)


    def move(self):
        resultado = False

        while not resultado:
            self.inputValue()
            self.mover += 1
            self.printResult()
            resultado = self.validaResultado()
        else:
            self.fimJogo()


    def printResult(self):
        print("\n")
        print("Torre 1: ", self.torre1)
        print("Torre 2: ", self.torre2)
        print("Torre 3: ", self.torre3)
        print("mover: ", self.mover)

        self.printTorre(self.torre1, "1")
        self.printTorre(self.torre2, "2")
        self.printTorre(self.torre3, "3")
        print("\n")


    def iniciar(self):
        self.numdiscos = 0
        self.comecar = False
        self.mover = 0
        self.torre1 = []
        self.torre2 = []
        self.torre3 = []

        disco.quantDisco()
        self.init()

        print("\n------JOGO INICIANDO------\n")
        self.printResult()
        self.move()