from analizadorSintactico import parser
from analizadorSemantico import SemanticAnalyzer

# Ejemplo de uso
#"sum = (10 + 20) * 3"

data = """
x = 5
y = 10
z = x + y * 2"""
result = parser.parse(data)
semantic_analyzer = SemanticAnalyzer()
semantic_analyzer.analyze(result)


