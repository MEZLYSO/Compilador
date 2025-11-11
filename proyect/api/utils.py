from antlr4 import *
import lenguage.GrammarLexer as GrammarLexer
import lenguage.GrammarParser as GrammarParser
import  io
import sys
import lenguage.MyVisitor as MyVisitor

def run_code(code:str):
    input_stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.program()

    # Capturan la salida 
    old_stdout=sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf

    #Creamo un objeto de nuestro visitor
    visitor = MyVisitor()
    #Visitamos el arbol con nuestro visitor
    visitor.visit(tree)
    # Capturamos la salida
    output=buf.getvalue()

    return output

