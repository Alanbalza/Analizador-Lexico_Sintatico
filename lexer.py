import ply.lex as lex

tokens = [
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 
    'LBRACE', 'RBRACE', 'SEMICOLON', 'EQUAL', 'LE', 'LT', 'GE', 'GT', 'FOR', 'INT', 'STRING', 'DOT', 'COMMA'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_EQUAL = r'='
t_LE = r'<='
t_LT = r'<'
t_GE = r'>='
t_GT = r'>'
t_DOT = r'\.'
t_COMMA = r','
t_FOR = r'for'
t_INT = r'int'
t_STRING = r'"[^"]*"'
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
