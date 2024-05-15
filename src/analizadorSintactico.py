import ply.yacc as yacc
from analizadorLexico import tokens

# Reglas de la gramática
def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS expression'
    p[0] = ('assign', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    if p:
        print("Error de sintaxis en '%s'" % p.value)
    else:
        print("Error de sintaxis en EOF")

# Construcción del parser
parser = yacc.yacc()
'''
# Ejemplo de uso
data = "sum = (10 + 20) * 3"
result = parser.parse(data)
print(result)'''