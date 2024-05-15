from analizadorSintactico import parser
from analizadorSemantico import check_semantics

# Ejemplo de uso
data = "sum = (10 + 20) * 3"
ast = parser.parse(data)
check_semantics(ast)

