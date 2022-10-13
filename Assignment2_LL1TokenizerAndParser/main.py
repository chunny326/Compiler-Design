from lexer import Lexer
from parse import Parser
from file import File
from grammar import Grammar
from copy import deepcopy

def find_follow(grammar, _first):
    follow = {i: [] for i in grammar.nonterminals}
    # print("follow: ", follow)
    pass

def find_first(grammar):
    # first set initialized for nonterminals and terminals
    first = {i: [] for i in grammar.nonterminals}
    first.update((i, [i]) for i in grammar.terminals)
    print("first: ", first)

    while True:
        updated = False
        
        # FIRST set
        for nt, expression in grammar.rules:
            if '!' not in expression and 'eof' not in expression:
                if '!' in first[expression[0]]:
                    rhs = deepcopy(first[expression[0]].remove('!'))
                else:
                    rhs = deepcopy(first[expression[0]])

                i = 0
                k = len(expression)

                while ('!' in expression[i] and i <= k - 1):
                    union(rhs, expression[i + 1].remove('!'))
                    i = i + 1

            if i == len(expression) - 1 and '!' in first[expression[-1]]:
                if '!' not in rhs:
                    rhs.append('!')
            
            updated |= union(first[nt], rhs)
                
        if not updated:
            return first

def union(first, add_this):
    n = len(first)
    if len(add_this) != 0:
        for i in add_this:
            if i not in first:
                first.append(i)
    return len(first) != n

# list of productions
# 0  Goal   -> Expr
# 1  Expr   -> Term Expr'
# 2  Expr'  -> + Term Expr'
# 3         -> - Term Expr'
# 4         -> e
# 5  Term   -> Factor Term'
# 6  Term'  -> * Factor Term'
# 7         -> / Factor Term'
# 8         -> e
# 9  Factor -> ( Expr )
# 10        -> num
# 11        -> name
# ----------------------------------------------------
# Goal = ^, Expr = A, Expr' = B, Term = C, Term' = D, 
# Factor = E, num = x, name = n, empty = !
prods = Grammar('A -> CB',
                'B -> +CB',
                'B -> -CB',
                'B -> !',
                'C -> ED',
                'D -> *ED',
                'D -> /ED',
                'D -> !',
                'E -> (A)',
                'E -> x',
                'E -> n')

# print(prods)
first = find_first(prods)
# first['Expr'] = first.pop('A')
# first['Expr\''] = first.pop('B')
# first['Term'] = first.pop('C')
# first['Term\''] = first.pop('D')
# first['Factor'] = first.pop('E')
print("\nfirst: ", first)

# with open('Notes/ll1_valid_book.txt', 'r') as file1:
#     text1 = file1.read()

# lexer1 = Lexer(text1)
# tokens1 = lexer1.gen_tokens()
# print(list(tokens1))  # only used for token testing - don't use once tokens done!

# with open('Notes/ll1_valid_class.txt', 'r') as file2:
#     text2 = file2.read()

# lexer2 = Lexer(text2)
# tokens2 = lexer2.gen_tokens()
# print(list(tokens2))  # only used for token testing - don't use once tokens done!

# with open('Notes/ll1_invalid_book.txt', 'r') as file3:
#     text3 = file3.read()

# lexer3 = Lexer(text3)
# tokens3 = lexer3.gen_tokens()
# print(list(tokens3))  # only used for token testing - don't use once tokens done!