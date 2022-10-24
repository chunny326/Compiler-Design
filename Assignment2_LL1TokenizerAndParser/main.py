from lexer import Lexer
from grammar import Grammar
from table_construction import *
from skeleton_parser import Parser

if __name__ == "__main__":
    # -----------------------------  grammar from textbook -----------------------------
    print("Processing grammar for book valid/invalid sets...\n")

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
    
    count = 0
    count2 = 0
    for i, j in table:
        if count % (len(productions.terminals) - 1) == 0:
            if count2 == len(productions.nonterminals):
                break
            count = 0
            print("\n")
            print('{:<5}'.format(productions.nonterminals[count2]), end = " ")
            count2 = count2 + 1

        count = count + 1
        print('{:>5}'.format(table[(i, j)]), end = "")
    print("\n")
    # ----------------------------------------------------------------------------------

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
    # ----------------------------------------------------------------------------------
    
    # ------------------- modified grammar to accept new expressions -------------------
    print("\n\nProcessing grammar for class valid/invalid sets...\n")

    productions2 = Grammar('Goal->Expr',
                           'Expr->Term Expr\'',
                           'Expr\'->+ Term Expr\'',
                           'Expr\'->- Term Expr\'',
                           'Expr\'->eps',
                           'Term->Ex Term\'',
                           'Term\'->* Ex Term\'',
                           'Term\'->/ Ex Term\'',
                           'Term\'->eps',
                           'Ex->Factor Ex\'',
                           'Ex\'->^ Factor Ex\'',
                           'Ex\'->eps',
                           'Factor->( Expr )',
                           'Factor->- Neg',
                           'Factor->num',
                           'Factor->name',
                           'Neg->num',
                           'Neg->name'
                          )

    # find and print the sets
    first2 = find_first(productions2)
    follow2 = find_follow(productions2, first2)
    first_plus2 = find_first_plus(first2, follow2, productions2)
    table2 = construct_table(first_plus2, productions2)

    print("\nFIRST: ", first2)
    print("\nFOLLOW: ", follow2)
    print("\nFIRST+: ", first_plus2, "\n")

    # print the LL1 table
    print("LL1 Table: \n")
    print(end = "      ")
    prods2 = deepcopy(productions2.terminals)
    prods2.remove('eps')
    for i in prods2:
        print('{:>5}'.format(i), end = "")
    
    count = 0
    count2 = 0
    for i, j in table2:
        if count % (len(productions2.terminals) - 1) == 0:
            if count2 == len(productions2.nonterminals):
                break
            count = 0
            print("\n")
            print('{:<5}'.format(productions2.nonterminals[count2]), end = " ")
            count2 = count2 + 1

        count = count + 1
        print('{:>5}'.format(table2[(i, j)]), end = "")
    print("\n")
    # ----------------------------------------------------------------------------------

    # ----------------------------- VALID FILE FROM Class -----------------------------
    # read in valid lines file from book
    with open('Notes/ll1_valid_class.txt', 'r') as file3:
        text3 = file3.read()

    # tokenize file
    lexer3 = Lexer(text3)
    print("\n\nScanning ", file3.name, "...\n")
    tokens3 = lexer3.gen_tokens()
    # print(list(tokens3))  # only used for token testing - don't use once tokens done!

    parse3 = Parser(tokens3, False)
    print("\nParsing ", file3.name, "...\n")
    parse3.skeleton_parser(table2, productions2)
    # ----------------------------------------------------------------------------------

    # ----------------------------- INVALID FILE FROM BOOK -----------------------------
    # read in invalid lines file from book
    with open('Notes/ll1_invalid_book.txt', 'r') as file4:
        text4 = file4.read()

    # tokenize file
    lexer4 = Lexer(text4)
    print("\n\nScanning ", file4.name, "...\n")
    tokens4 = lexer4.gen_tokens()
    # print(list(tokens4))  # only used for token testing - don't use once tokens done!

    parse4 = Parser(tokens4, False)
    print("\nParsing ", file4.name, "...\n")
    parse4.skeleton_parser(table2, productions2)
    # ----------------------------------------------------------------------------------