from lexer import Lexer
from grammar import Grammar
from table_construction import *
from skeleton_parser import Parser

if __name__ == "__main__":
    # ------------------- grammar for accepted expressions -------------------
    print("\n\nProcessing grammar for valid/invalid sets...\n")

    productions = Grammar('Goal->Expr',
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

    # ------------------------------- PROCESS INPUT FILE -------------------------------
    # read in valid lines file from book
    with open('Notes/ll1_to_ir.txt', 'r') as file:
        text = file.read()

    # tokenize file
    lexer = Lexer(text)
    print("\n\nScanning ", file.name, "...\n")
    tokens = lexer.gen_tokens()
    # print(list(tokens3))  # only used for token testing - don't use once tokens done!

    parse = Parser(tokens, False)
    print("\nParsing ", file.name, "...\n")
    parse.skeleton_parser(table, productions)
    # ----------------------------------------------------------------------------------
