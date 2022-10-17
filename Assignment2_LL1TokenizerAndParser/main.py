from lexer import Lexer
from parse import Parser
from grammar import Grammar
from first_follow_firstP import *

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

    first['Expr'] = first.pop('A')
    first['Expr\''] = first.pop('B')
    first['Term'] = first.pop('C')
    first['Term\''] = first.pop('D')
    first['Factor'] = first.pop('E')
    follow['Expr'] = follow.pop('A')
    follow['Expr\''] = follow.pop('B')
    follow['Term'] = follow.pop('C')
    follow['Term\''] = follow.pop('D')
    follow['Factor'] = follow.pop('E')

    print('\nf = eof')
    print('! = epsilon')
    print('x = num')
    print('n = name')
    print("\nFIRST: ", first)
    print("\nFOLLOW: ", follow)
    print("\nFIRST+: ", first_plus, "\n")


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