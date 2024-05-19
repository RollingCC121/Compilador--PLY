import ply.yacc as yacc
from lexer.analizadorLexico import tokens,lexer
from aParser.analizadorSintactico import parser as syntactic_parser
from aSemantic.analizadorSemantico import SemanticAnalyzer
from generator.middleCode import IntermediateCodeGenerator
from generator.binaryGenerator import BinaryCodeGenerator 

file_path = "texto.txt"
try:
    with open(file_path, "r") as file:
        source_code = file.read()
except FileNotFoundError:
    print(f"No se encontró el archivo: {file_path}")
    exit()

# Imprimir tokens generados por el analizador léxico
lexer.input(source_code)
print("Tokens generados por el analizador léxico:")
for token in lexer:
    print(token)

# Análisis sintáctico
parsed_tree = syntactic_parser.parse(source_code)
# Impresión de resultados
print("\nResultado del análisis sintáctico:")
print(parsed_tree)

# Análisis semántico
semantic_analyzer = SemanticAnalyzer()
try:
    semantic_analyzer.analyze(parsed_tree)
    print("\nAnálisis semántico completado sin errores.")
except Exception as e:
    print("\nError durante el análisis semántico:")
    print(e)

code_generator = IntermediateCodeGenerator()
code_generator.generate_code(parsed_tree)
code_generator.print_code()

# Generación de código binario con validación
binary_generator = BinaryCodeGenerator()
try:
    binary_generator.validate_and_generate_code(code_generator.intermediate_code)
    # Impresión del código binario
    binary_code = binary_generator.get_binary_code()
    print("\nCódigo binario generado:")
    print(binary_code.hex())
except ValueError as e:
    print("\nError durante la generación del código binario:")
    print(e)# Generación de código binario con validación
binary_generator = BinaryCodeGenerator()
try:
    binary_generator.validate_and_generate_code(code_generator.intermediate_code)
    # Impresión del código binario
    binary_code = binary_generator.get_binary_code()

except ValueError as e:
    print("\nError durante la generación del código binario:")
    print(e)
