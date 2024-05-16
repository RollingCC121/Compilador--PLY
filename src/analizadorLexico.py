import ply.lex as lex 

# Lista de tokens
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
]


# Definición de tokens usando expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='

# Ignorar caracteres como espacios y saltos de línea
t_ignore = ' \t\n'


# Definición de funciones para tokens más complejos
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Manejo de errores
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
'''
# Ejemplo de uso
data = """
x = 5
y = 10
z = x + y * 2
"""
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break  # No hay más tokens
    print(tok)
'''
