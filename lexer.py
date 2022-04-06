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
                | NAME LPAREN optional RPAREN
                | NAME LPAREN optional COMA items RPAREN
                | NAME LPAREN items COMA optional RPAREN'''
    if len(t) == 5:
        print (t[1],"->",t[3])
    if len(t) == 7:
        print (t[1],"->",t[3])
        print (t[1],"->",t[5])
    #print(t[3].split(','))





def p_def_optional(t):
    '''optional : OPT LPAREN items RPAREN'''
    optional_items = t[3].split(',')
    for i in range (len(optional_items)):
        optional_items[i] = '*' + optional_items[i]
    
    print (optional_items)
    result = ""
    for i in optional_items:
        result += i
        result += ','
    result = result[0:-1]
        
    t[0] = result
    print (t[0])
    return t[0]


def p_def_items(t):
    '''items : NAME
             | items COMA NAME'''
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 3:
        t[0] = t[1] + t[2] + t[3]
    else:
        t[0] = t[1] + t[2] + t[3]
    
    #print (t[1],"->",t[3])
    print (t[0])
    return t[0]





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
