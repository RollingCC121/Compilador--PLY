from aParser.analizadorSintactico import parser
from aSemantic.analizadorSemantico import SemanticAnalyzer
from middleCode import IntermediateCodeGenerator

def __init__(self):

    # Ejemplo de uso
    #"sum = (10 + 20) * 3"
    data = """
    x = 5
    y = 10
    z = x + y * 2"""
    
    result = parser.parse(data)
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze(result)

    # Generador de código intermedio
    code_generator = IntermediateCodeGenerator()
    code_generator.generate_code(result)

    # Imprimir código intermedio generado
    print("Código Intermedio:")
    for line in code_generator.intermediate_code:
        print(line)


