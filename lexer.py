import ply.lex as lex

reserved = {
    'programa': 'PROGRAMA',
    'int': 'INT',
    'suma': 'SUMA',
    'resta': 'RESTA',
    'read': 'READ',
    'printf': 'PRINTF',
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'end': 'END',
}

tokens = [
    'ID', 'NUMBER', 'PLUS', 'SEMI', 'LPAREN', 'RPAREN', 'CADENA','EQUAL','LBRACE', 'RBRACE',
] + list(reserved.values())

t_PLUS = r'\+'
t_SEMI = r';'
t_EQUAL = r'='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'\".*?\"'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
