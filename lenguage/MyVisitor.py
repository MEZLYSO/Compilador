from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    # Definimos la memoria o el entorno
    def __init__(self):
        self.memory = { }

    # Definimos la asignacion
    def visitAssign(self,ctx):
        # Se obtiene el id o nombre de la variable
        name=ctx.ID().getText()
        # Se obtiene el valor, ya sea un valor numerico o una expresion
        value=self.visit(ctx.expr())
        # Se almacena en memoria a partir del nombre y el valor
        self.memory[name]=value

    # Definimos la impresion
    def visitPrint(self,ctx):
        # Definimos la expresion que se desea mostrar
        value=self.visit(ctx.expr())
        # Imprime el valor
        print(value)

    # 