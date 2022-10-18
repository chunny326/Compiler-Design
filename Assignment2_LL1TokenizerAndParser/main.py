from lexer import Lexer
from parse import Parser
from grammar import Grammar
from table_construction import *

if __name__ == "__main__":
    # see grammar.txt for explanation of productions
    productions = Grammar('^ -> A',
                    'A -> CB',
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

    first = find_first(productions)
    follow = find_follow(productions, first)
    first_plus = find_first_plus(first, follow, productions)
    table = construct_table(first_plus, productions)

    first['Goal'] = first.pop('^')
    first['Expr'] = first.pop('A')
    first['Expr\''] = first.pop('B')
    first['Term'] = first.pop('C')
    first['Term\''] = first.pop('D')
    first['Factor'] = first.pop('E')
    follow['Goal'] = follow.pop('^')
    follow['Expr'] = follow.pop('A')
    follow['Expr\''] = follow.pop('B')
    follow['Term'] = follow.pop('C')
    follow['Term\''] = follow.pop('D')
    follow['Factor'] = follow.pop('E')
    # table['Goal'] = table.pop('^')
    # table['Expr'] = table.pop('A')
    # table['Expr\''] = table.pop('B')
    # table['Term'] = table.pop('C')
    # table['Term\''] = table.pop('D')
    # table['Factor'] = table.pop('E')

    print('\nf = eof')
    print('! = epsilon')
    print('x = num')
    print('n = name')
    print("\nFIRST: ", first)
    print("\nFOLLOW: ", follow)
    print("\nFIRST+: ", first_plus, "\n")

    print("LL1 Table: \n")
    print(end = "  ")
    prods = deepcopy(productions.terminals)
    prods.remove('!')
    for i in prods:
        print('{:>4}'.format(i), end = "")
    print("\n")
    
    print(productions.nonterminals[-1], end = " ")
    count = 0
    count2 = 0
    for i, j in table:
        print('{:>4}'.format(table[(i, j)]), end = "")

        count = count + 1
        if count % 9 == 0:
            if count2 == 5:
                break
            count = 0
            print("\n")
            print(productions.nonterminals[count2], end = " ")
            count2 = count2 + 1
    print("\n")

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