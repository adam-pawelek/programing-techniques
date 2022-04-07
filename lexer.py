tokens = (
 'NAME','RPAREN','LPAREN','COMA','OPT', 'ALL', 'ONEOF','MOREOF', "COLON"
 )
literals = "(),"
def t_OPT(t):
    r'opt'
    return t
def t_NAME(t):
    r'[a-zA-Z0-9-]+'
    return t

def t_ALL(t):
    r'all'
    return t

def t_ONEOF(t):
    r'one-of'
    return t

def t_MOREOF(t):
    r'more-of'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMA = r'\,'
t_COLON = r'\:'
# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
import ply.lex as lex
lexer = lex.lex()


graph = {}

def p_def_relations(t):
    '''relations : yourEnd
                | relations yourEnd'''



def p_def_your_end(t):
    '''yourEnd : NAME COLON NAME relation'''
    global graph
    ingredients = t[4].split(',')
    for i in ingredients:
        if t[1] not  in graph:
            graph[t[1]] = []
        graph[t[1]].append([i,t[3]])

    
    print (graph)




#def p_def_def(t):
#    'def : relations'


#def p_def_relations(t):
#    '''relations : relation
#                | relations relation'''

def p_def_relation(t):
    '''relation : LPAREN items RPAREN
                | LPAREN optional RPAREN
                | LPAREN optional COMA items RPAREN
                | LPAREN items COMA optional RPAREN
                | LPAREN items COMA optional COMA items RPAREN'''
    if len(t) == 4:
        print (4)
        t[0] = t[2]
    if len(t) == 6:
        t[0] = t[2] + ',' + t[4]
        print (6)
        print (t[1],"->",t[5])
    if len(t) == 8:
        t[0] = t[2] + ',' + t[4] + ',' + t[6]
    print (f"t[0] = {t[0]}")
    #print(t[3].split(','))
    print ("tutaj")
    return t[0]





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




import sys
if len(sys.argv) < 2 :
 sys.exit("Usage: %s <filename>" % sys.argv[0])
fp = open(sys.argv[1])
contents=fp.read()
parser.parse(contents) 

result = "digraph { \n"

for key, item_list in graph.items():
    for value in item_list: 
        print (f"moj {key} -> {value}")
        if value[1] == "all":
            if value[0][0] == '*':
                result += f'{key} -> {value[0][1:]} [arrowhead = curve label="opt", color=yellow] \n'
            else:
                result += f"{key} -> {value[0]} [arrowhead = dot, color=red] \n"
        elif value[1] == "one-of":
            result += f"{key} -> {value[0]} [arrowhead = dot, color=blue] \n"
        elif value[1] == "more-of":
            result += f"{key} -> {value[0]} [arrowhead = dot, color=black] \n"
        print (result)

result += "}"
f = open("result.txt", "a")
f.write(result)
f.close()


'''
while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
    for key, item_list in graph.items():
        for value in item_list: 
            print (f"moj {key} -> {value}")
            if value[1] == "all":
                if value[0][0] == '*':
                    result += f'{key} -> {value[0][1:]} [arrowhead = curve label="opt", color=yellow] \n'
                else:
                    result += f"{key} -> {value[0]} [arrowhead = dot, color=red] \n"
            elif value[1] == "one-of":
                result += f"{key} -> {value[0]} [arrowhead = dot, color=blue] \n"
            elif value[1] == "one-of":
                result += f"{key} -> {value[0]} [arrowhead = dot, color=black] \n"
            print (result)

'''
