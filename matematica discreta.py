class Conjuntos():
    def __init__(self):
        self.lista = []
        self.nome=""
        self.quant = 0

    def nome(self,valor1):
        self.nome=valor1

    def inserir(self,valor):
        if valor in self.lista:
            return False
        else:
            self.lista.append(valor)
            self.quant+=1
            return self.lista
        
    def imprimir(self):
            print("Nome: ",self.nome,", Conjunto: ","{",*self.lista,"}.", sep="")
         
    def tamanho(self):
        return self.quant
    def pertence(self,valor):
        return valor in self.lista
                

    
teste=Conjuntos()

teste.inserir("a")
print(teste.inserir("a"))
teste.inserir("b")


teste.imprimir()

print(teste.pertence("abc"))







