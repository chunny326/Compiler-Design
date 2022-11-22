from lexer import Lexer
from grammar import Grammar
from table_construction import *
from skeleton_parser import Parser
from tokens import TokenType
from ir import shunting_yard, optimize_post_order

def print_next_post_order(post_ord_line):
    for val in post_ord_line:
        print(val, " ", sep = "", end = "")
    # print(" ..... ", sep = "", end = "")
    print("\n")

def print_optimizations(optimized_line):
    for val in optimized_line:
        print(val, " ", sep = "", end = "")
    print("\n")

if __name__ == "__main__":
    # ------------------- grammar for accepted expressions -------------------
    print("\nProcessing grammar sets...")

    # productions to handle input language
    productions = Grammar('Goal->Statement',
                          'Statement->Decl Assign',
                          'Statement->name Assign',
                          'Statement->print ( name )',
                          'Decl->type name',
                          'Assign->= Expr',
                          'Assign->eps',
                          'Expr->Term Expr\'',
                          'Expr\'->+ Term Expr\'',
                          'Expr\'->- Term Expr\'',
                          'Expr\'->eps',
                          'Term->Factor Term\'',
                          'Term\'->* Factor Term\'',
                          'Term\'->/ Factor Term\'',
                          'Term\'->eps',
                          'Factor->Base Power',
                          'Power->^ Base Power',
                          'Power->eps',
                          'Base->( Expr )',
                          'Base->Base\'',
                          'Base->- Base\'',
                          'Base\'->number',
                          'Base\'->name',
                         )

    # find the sets and table
    first = find_first(productions)
    follow = find_follow(productions, first)
    first_plus = find_first_plus(first, follow, productions)
    table = construct_table(first_plus, productions)
    # ----------------------------------------------------------------------------------

    # ---------------------------- PROCESS VALID INPUT FILE --------------------S--------
    # read in valid lines file from book
    with open('Notes/accept.txt', 'r') as file:
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
    # optimized_post_order = optimize_post_order(post_order)
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
            if tok.type.value == 'name' or tok.type.value == 'number':
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
            # print_optimizations(optimized_post_order[index - 1])

            # print next line result
            print(parse_results[index], ": ", end = "", sep = "")
            if parse_results[index] == 'Invalid':
                valid = False
            else:
                valid = True
            index = index + 1
    # ----------------------------------------------------------------------------------

    # ------------------------------ PROCESS INVALID INPUT FILE ------------------------------
    # read in valid lines file from book
    with open('Notes/reject.txt', 'r') as file1:
        text1 = file1.read()

    # tokenize file
    lexer1 = Lexer(text1)
    print("\nScanning ", file1.name, "...", sep = "")
    tokens1 = lexer1.gen_tokens()

    parse1 = Parser(tokens1, False)
    print("\nParsing ", file1.name, "...", sep = "")
    parse_results1 = parse1.skeleton_parser(table, productions)

    # get another copy of the set of tokens from file to pass to Shunting Yard algorithm
    lexer2 = Lexer(text1)
    tokens2 = lexer2.gen_tokens()
    toks1 = list(tokens2)

    # run the Shunting Yard algorithm to get queue with post-order traversal
    # print("\nRunning Shunting Yard algorithm to create post-order traversal...\n", sep = "")
    # post_order1 = shunting_yard(toks1)
    # -------------------------------------------------------------------------------------

    # ------------------------------- PRINT INVALID RESULTS -------------------------------
    print("Printing results:\n")
    index1 = 0
    
    print(parse_results1[index1], ": ", end = "", sep = "")
    valid1 = True
    if parse_results1[index1] == 'Invalid':
        valid1 = False
    index1 = index1 + 1

    for tok1 in toks1:
        if tok1.type.value != TokenType.NEWLINE.value:
            if tok1.type.value == 'name' or tok1.type.value == 'number':
                print(tok1.value, " ", end = "")
            elif tok1.type.name == 'EOF':
                print("End of file. Done processing.\n")
            else:
                print(tok1.type.value, " ", end = "")
        else:
            # for all invalid lines of code, only display "Invalid"
            if valid1 == False:
                continue

            # print post-order and optimized post-order
            print(".....  ", end = "")
            # print_next_post_order(post_order1[index1 - 1])

            # print next line result
            print(parse_results1[index1], ": ", end = "", sep = "")
            if parse_results1[index1] == 'Invalid':
                valid1 = False
            else:
                valid1 = True
            index1 = index1 + 1
    # ----------------------------------------------------------------------------------

