import ply.yacc as yacc
from lexer import tokens

# Precedence rules for the arithmetic operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Grammar rules
def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement(p):
    '''statement : for_statement
                 | expression SEMICOLON
                 | function_call SEMICOLON'''
    p[0] = p[1]

def p_for_statement(p):
    '''for_statement : FOR LPAREN declaration SEMICOLON expression SEMICOLON assignment RPAREN LBRACE statements RBRACE'''
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_declaration(p):
    '''declaration : INT ID EQUAL expression'''
    p[0] = ('declare', p[2], p[4])

def p_assignment(p):
    '''assignment : ID EQUAL expression'''
    p[0] = ('=', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LE expression
                  | expression LT expression
                  | expression GE expression
                  | expression GT expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_id(p):
    '''expression : ID'''
    p[0] = p[1]

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = p[1]

def p_function_call(p):
    '''function_call : ID DOT ID LPAREN RPAREN'''
    p[0] = ('func_call', p[1], p[3])

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        raise SyntaxError("Syntax error at EOF")

parser = yacc.yacc()
