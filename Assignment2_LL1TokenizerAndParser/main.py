from lexer import Lexer
from grammar import Grammar
from table_construction import *
from skeleton_parser import Parser

if __name__ == "__main__":
    # grammar from textbook
    productions = Grammar('Goal->Expr',
                          'Expr->Term Expr\'',
                          'Expr\'->+ Term Expr\'',
                          'Expr\'->- Term Expr\'',
                          'Expr\'->eps',
                          'Term->Factor Term\'',
                          'Term\'->* Factor Term\'',
                          'Term\'->/ Factor Term\'',
                          'Term\'->eps',
                          'Factor->( Expr )',
                          'Factor->num',
                          'Factor->name'
                         )

    # find and print the sets
    first = find_first(productions)
    follow = find_follow(productions, first)
    first_plus = find_first_plus(first, follow, productions)
    table = construct_table(first_plus, productions)

    print("\nFIRST: ", first)
    print("\nFOLLOW: ", follow)
    print("\nFIRST+: ", first_plus, "\n")

    # print the LL1 table
    print("LL1 Table: \n")
    print(end = "      ")
    prods = deepcopy(productions.terminals)
    prods.remove('eps')
    for i in prods:
        print('{:>5}'.format(i), end = "")
    print("\n")
    
    print('{:<6}'.format(productions.nonterminals[-1]), end = "")
    count = 0
    count2 = 0
    for i, j in table:
        print('{:>5}'.format(table[(i, j)]), end = "")

        count = count + 1
        if count % 9 == 0:
            if count2 == 5:
                break
            count = 0
            print("\n")
            print('{:<5}'.format(productions.nonterminals[count2]), end = " ")
            count2 = count2 + 1
    print("\n")

    # ----------------------------- VALID FILE FROM BOOK -----------------------------
    # read in valid lines file from book
    with open('Notes/ll1_valid_book.txt', 'r') as file1:
        text1 = file1.read()

    # tokenize file
    lexer1 = Lexer(text1)
    print("\n\nScanning ", file1.name, "...\n")
    tokens1 = lexer1.gen_tokens()
    # print(list(tokens1))  # only used for token testing - don't use once tokens done!

    parse1 = Parser(tokens1)
    print("\nParsing ", file1.name, "...\n")
    parse1.skeleton_parser(table, productions)
    # ----------------------------------------------------------------------------------

    # ----------------------------- INVALID FILE FROM BOOK -----------------------------
    # read in invalid lines file from book
    with open('Notes/ll1_invalid_book.txt', 'r') as file2:
        text2 = file2.read()

    # tokenize file
    lexer2 = Lexer(text2)
    print("\n\nScanning ", file2.name, "...\n")
    tokens2 = lexer2.gen_tokens()
    # print(list(tokens2))  # only used for token testing - don't use once tokens done!

    parse2 = Parser(tokens2)
    print("\nParsing ", file2.name, "...\n")
    parse2.skeleton_parser(table, productions)
    # ----------------------------------------------------------------------------------



# with open('Notes/ll1_valid_class.txt', 'r') as file2:
#     text2 = file2.read()

# lexer2 = Lexer(text2)
# tokens2 = lexer2.gen_tokens()
# print(list(tokens2))  # only used for token testing - don't use once tokens done!

