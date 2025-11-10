from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = { }

    # Definimos la assignacion
    def visitAssign(self,ctx):
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value
    # Definimos la assignacion
    def visitPrint(self,ctx):
        value=self.visit(ctx.expr())
        print(value)