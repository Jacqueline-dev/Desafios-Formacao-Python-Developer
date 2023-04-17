from abc import ABC, abstractmethod, abstractproperty


class ControlRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControlRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligada!")
    
    @property
    def marca(self):
        return "Philco"

    def desligar(self):
        print("Desligar a TV...")
        print("Desligando")


class ControleArcondicionado(ControlRemoto):
    def ligar(self):
        print("Ligando o Ar condicionado...")
        print("Ligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
