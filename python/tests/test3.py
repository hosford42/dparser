from dparser import Parser
import os


def d_add1(t):
    '''add : add '+' mul'''
    return t[0] + t[2]


def d_add2(t, nodes):
    '''add : mul'''
    del t
    return nodes[0].user.t


def d_mul1(t):
    '''mul : mul '*' exp'''
    return t[0]*t[2]


def d_mul2(t):
    '''mul : exp'''
    return t[0]


def d_exp1(t):
    '''exp : "[0-9]+"'''
    return int(t[0])


def d_exp2(t):
    '''exp : '(' add ')' '''
    return t[1]


if Parser().parse('''3*(3+4)''').getStructure() != 21:
    print('fail')

# python3 and/or swig have a problem cleaning up and will SEGV in this case.
os._exit(0)
