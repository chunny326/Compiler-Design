from lexer import Lexer
from grammar import Grammar
from table_construction import *
from skeleton_parser import Parser
from tokens import TokenType
from ir import shunting_yard, optimize_post_order

def print_next_post_order(post_ord_line):
    for val in post_ord_line:
        print(val, " ", sep = "", end = "")
    print(" ..... ", sep = "", end = "")

def print_optimizations(optimized_line):
    for val in optimized_line:
        print(val, " ", sep = "", end = "")
    print("\n")

if __name__ == "__main__":
    # ------------------- grammar for accepted expressions -------------------
    print("\nProcessing grammar for valid/invalid sets...")

    # productions to handle input language
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

    # find the sets and table
    first = find_first(productions)
    follow = find_follow(productions, first)
    first_plus = find_first_plus(first, follow, productions)
    table = construct_table(first_plus, productions)
    # ----------------------------------------------------------------------------------

    # ------------------------------- PROCESS INPUT FILE -------------------------------
    # read in valid lines file from book
    with open('Notes/ll1_to_ir.txt', 'r') as file:
        text = file.read()

    # tokenize file
    lexer = Lexer(text)
    print("\nScanning ", file.name, "...", sep = "")
    tokens = lexer.gen_tokens()

    parse = Parser(tokens, False)
    print("\nParsing ", file.name, "...", sep = "")
    parse_results = parse.skeleton_parser(table, productions)

    # get another copy of the set of tokens from file to pass to Shunting Yard algorithm
    lexer2 = Lexer(text)
    tokens2 = lexer2.gen_tokens()
    toks = list(tokens2)

    # run the Shunting Yard algorithm to get queue with post-order traversal
    print("\nRunning Shunting Yard algorithm to create post-order traversal...\n", sep = "")
    post_order = shunting_yard(toks)

    # run optimizations
    optimized_post_order = optimize_post_order(post_order)
    # -------------------------------------------------------------------------------------

    # ----------------------------------- print results -----------------------------------
    print("Printing results:\n")
    index = 0
    
    print(parse_results[index], ": ", end = "", sep = "")
    valid = True
    if parse_results[index] == 'Invalid':
        valid = False
    index = index + 1

    for tok in toks:
        if tok.type.value != TokenType.NEWLINE.value:
            if tok.type.value == 'name' or tok.type.value == 'num':
                print(tok.value, " ", end = "")
            elif tok.type.name == 'EOF':
                print("End of file. Done processing.\n")
            else:
                print(tok.type.value, " ", end = "")
        else:
            # for all invalid lines of code, only display "Invalid"
            if valid == False:
                continue

            # print post-order and optimized post-order
            print(".....  ", end = "")
            print_next_post_order(post_order[index - 1])
            print_optimizations(optimized_post_order[index - 1])

            # print next line result
            print(parse_results[index], ": ", end = "", sep = "")
            if parse_results[index] == 'Invalid':
                valid = False
            else:
                valid = True
            index = index + 1
    # ----------------------------------------------------------------------------------
