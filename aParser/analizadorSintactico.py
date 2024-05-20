import ply.yacc as yacc  # Importa la biblioteca PLY para el análisis sintáctico
from lexer.analizadorLexico import tokens  # Importa los tokens definidos en el analizador léxico

# Definición de precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),   # La suma y la resta tienen la misma precedencia y se asocian a la izquierda
    ('left', 'TIMES', 'DIVIDE'), # La multiplicación y la división tienen la misma precedencia y se asocian a la izquierda
)

# Reglas de la gramática

# Regla para manejar múltiples declaraciones
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 2:  # Caso base: una única declaración
        p[0] = [p[1]]
    else:  # Caso recursivo: múltiples declaraciones
        p[0] = p[1] + [p[2]]

# Regla para manejar asignaciones
def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS expression'
    p[0] = ('assign', p[1], p[3])  # Devuelve una tupla que representa la asignación

# Regla para manejar expresiones sin asignaciones
def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]  # Devuelve la expresión

# Regla para manejar operaciones binarias (suma, resta, multiplicación, división, potencia)
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    p[0] = (p[2], p[1], p[3])  # Devuelve una tupla que representa la operación

# Regla para manejar operadores de comparación
def p_expression_ineq(p):
    '''expression : expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = (p[2], p[1], p[3])  # Devuelve una tupla que representa la comparación

# Regla para manejar la función sqrt (raíz cuadrada)
def p_expression_sqrt(p):
    'expression : SQRT LPAREN expression RPAREN'
    p[0] = ('sqrt', p[3])  # Devuelve una tupla que representa la raíz cuadrada

# Regla para manejar la función log (logaritmo)
def p_expression_log(p):
    'expression : LOG LPAREN expression RPAREN'
    p[0] = ('log', p[3])  # Devuelve una tupla que representa el logaritmo

# Regla para manejar expresiones agrupadas por paréntesis
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]  # Devuelve la expresión dentro de los paréntesis

# Regla para manejar identificadores
def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = p[1]  # Devuelve el identificador

# Regla para manejar números
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]  # Devuelve el número

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print("Error de sintaxis en '%s'" % p.value)  # Imprime el token que causó el error
    else:
        print("Error de sintaxis en EOF")  # Error al final del archivo

# Construcción del parser
parser = yacc.yacc()  # Crea una instancia del parser utilizando las definiciones anteriores
