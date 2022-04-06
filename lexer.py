tokens = (
 'NAME','RPAREN','LPAREN','COMA','OPT'
 )
literals = "(),"
def t_OPT(t):
    r'opt'
    return t
def t_NAME(t):
    r'[a-zA-Z]+'
    return t
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMA = r'\,'
# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
import ply.lex as lex
lexer = lex.lex()




def p_def_def(t):
    'def : relations'






def p_def_relations(t):
    '''relations : relation
                | relations relation'''
def p_def_relation(t):
    '''relation : NAME LPAREN items RPAREN
                | NAME LPAREN optionals RPAREN'''
    print (t[1],"->",t[3])
    #print(t[3].split(','))


def p_def_optionals(t):
    '''optionals : optional
                | optionals optional'''
    
    if len(t) == 2:
        t[0] = t[1]
    if len(t) == 3:
        t[0] = t[1] + t[2]
    return t[0]


def p_def_optional(t):
    'optional : OPT LPAREN items RPAREN'
    t[0] = t[1] + t[2] + t[3] + t[4]
    print (t[0])
    return t[0]


def p_def_items(t):
    '''items : NAME COMA NAME 
                | items COMA NAME'''
    if len(t) == 2:
        t[0] = t[1] + t[2] + t[3]
    else:
        t[0] = t[1] + t[2] + t[3]
    
    print (t[1],"->",t[3])
    return t[0]

'''
def p_def_optional(t):
    'optional : OPT LPAREN items RPAREN'
    t[0] = t[1] + t[2] + t[3] + t[4]
    print (t[0])
    return t[0]
'''



def p_error(t):
    print("Syntax error at '%s'" % t.value)
    
import ply.yacc as yacc
parser = yacc.yacc() 


while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
