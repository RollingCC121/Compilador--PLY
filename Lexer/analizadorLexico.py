import ply.lex as lex  # Importa la biblioteca PLY para el análisis léxico

# Lista de tokens que el lexer reconocerá
tokens = [
    'IDENTIFIER',  # Identificadores de variables
    'NUMBER',      # Números enteros
    'PLUS',        # Operador suma (+)
    'MINUS',       # Operador resta (-)
    'TIMES',       # Operador multiplicación (*)
    'DIVIDE',      # Operador división (/)
    'LPAREN',      # Paréntesis izquierdo
    'RPAREN',      # Paréntesis derecho
    'EQUALS',      # Operador asignación (=)
    'POWER',       # Operador potencia (^)
    'LT',          # Operador menor que (<)
    'GT',          # Operador mayor que (>)
    'LE',          # Operador menor o igual que (<=)
    'GE',          # Operador mayor o igual que (>=)
    'EQ',          # Operador igualdad (==)
    'NE',          # Operador desigualdad (!=)
    'SQRT',        # Función raíz cuadrada (sqrt)
    'LOG',         # Función logaritmo (log)
]

# Definición de tokens simples usando expresiones regulares
t_PLUS = r'\+'         # Token para el operador suma
t_MINUS = r'-'         # Token para el operador resta
t_TIMES = r'\*'        # Token para el operador multiplicación
t_DIVIDE = r'/'        # Token para el operador división
t_LPAREN = r'\('       # Token para el paréntesis izquierdo
t_RPAREN = r'\)'       # Token para el paréntesis derecho
t_EQUALS = r'='        # Token para el operador asignación
t_POWER = r'\^'        # Token para el operador potencia
t_LT = r'<'            # Token para el operador menor que
t_GT = r'>'            # Token para el operador mayor que
t_LE = r'<='           # Token para el operador menor o igual que
t_GE = r'>='           # Token para el operador mayor o igual que
t_EQ = r'=='           # Token para el operador igualdad
t_NE = r'!='           # Token para el operador desigualdad

# Ignorar espacios en blanco, tabulaciones y saltos de línea
t_ignore = ' \t\n'

# Definición de funciones para tokens más complejos
def t_SQRT(t):
    r'sqrt'   # Expresión regular para reconocer la función sqrt
    return t  # Devuelve el token identificado como SQRT

def t_LOG(t):
    r'log'    # Expresión regular para reconocer la función log
    return t  # Devuelve el token identificado como LOG

def t_NUMBER(t):
    r'\d+'    # Expresión regular para reconocer números enteros
    t.value = int(t.value)  # Convierte el valor del token a un entero
    return t  # Devuelve el token identificado como NUMBER

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'  # Expresión regular para reconocer identificadores
    return t  # Devuelve el token identificado como IDENTIFIER

# Manejo de errores léxicos
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])  # Imprime un mensaje de error
    t.lexer.skip(1)  # Salta al siguiente carácter

# Construcción del lexer
lexer = lex.lex()  # Crea una instancia del lexer utilizando las definiciones anteriores
