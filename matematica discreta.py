class lista():
    def __init__(self):
        self.lista = ['a','b','c']
        self.quant = 3

    def inserir(self,valor):
        a = 0
        i = 0
        while i < self.quant:
            if self.lista[i] != valor:
                a += 1
            else:
                a = 0
            i+=1
        if a != 0:
            self.lista.append(valor)
            self.quant += 1
        else:
            print("Já existe!")
            

    def imprimir(self):
        return self.lista

    def tamanho(self):
        return self.quant
