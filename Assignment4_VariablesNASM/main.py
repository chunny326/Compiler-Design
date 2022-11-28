from lexer import Lexer
from grammar import Grammar
from table_construction import *
from skeleton_parser import Parser
from tokens import TokenType
from ir import shunting_yard, optimize_post_order
from write_nasm import File

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
                          'Base\'->name'
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
    symbol_table = {}
    lexer = Lexer(text)
    print("\nScanning ", file.name, "...", sep = "")
    tokens = lexer.gen_tokens(symbol_table)

    parse = Parser(tokens, False)
    print("\nParsing ", file.name, "...", sep = "")
    parse_results = parse.skeleton_parser(table, productions)

    # get another copy of the set of tokens from file to pass to Shunting Yard algorithm
    symbol_table2 = {}
    lexer2 = Lexer(text)
    tokens2 = lexer2.gen_tokens(symbol_table2)
    toks = list(tokens2)

    # run the Shunting Yard algorithm to get queue with post-order traversal
    print("\nRunning Shunting Yard algorithm to create post-order traversal...\n", sep = "")
    post_order = shunting_yard(toks)

    # convert post-order trees to NASM if all lines are valid in file
    if 'Invalid' not in parse_results:
        results = open('Results/nasm_output.asm', 'w')
        nasm = File(results)
        nasm.init_file()
        nasm.convert_post_order(post_order, symbol_table)
        nasm.finish_file()

    print('NASM assembly file created and ready to execute.\n')
    print("\nEnd of file. Done processing.\n")
    # -------------------------------------------------------------------------------------

    # ----------------------------------- print results -----------------------------------
    # print("Printing parse results and post-order trees...\n\n")
    # index = 0
    
    # print(parse_results[index], ": ", end = "", sep = "")
    # valid = True
    # if parse_results[index] == 'Invalid':
    #     valid = False
    # index = index + 1

    # for tok in toks:
    #     if tok.type.value != TokenType.NEWLINE.value:
    #         if tok.type.value == 'name' or tok.type.value == 'number':
    #             print(tok.value, " ", end = "")
    #         elif tok.type.name == 'EOF':
    #             print("End of file. Done processing.\n")
    #         else:
    #             print(tok.type.value, " ", end = "")
    #     else:
    #         # for all invalid lines of code, only display "Invalid"
    #         if valid == False:
    #             continue

    #         # print post-order and optimized post-order
    #         print(".....  ", end = "")
    #         print_next_post_order(post_order[index - 1])
    #         # print_optimizations(optimized_post_order[index - 1])

    #         # print next line result
    #         print(parse_results[index], ": ", end = "", sep = "")
    #         if parse_results[index] == 'Invalid':
    #             valid = False
    #         else:
    #             valid = True
    #         index = index + 1
    # ----------------------------------------------------------------------------------

    # ------------------------------ PROCESS INVALID INPUT FILE ------------------------------
    # read in valid lines file from book
    with open('Notes/reject.txt', 'r') as file1:
        text1 = file1.read()

    # tokenize file
    symbol_table3 = {}
    lexer1 = Lexer(text1)
    print("\n\nScanning ", file1.name, "...", sep = "")
    tokens1 = lexer1.gen_tokens(symbol_table3)

    parse1 = Parser(tokens1, False)
    print("\nParsing ", file1.name, "...\n", sep = "")
    parse_results1 = parse1.skeleton_parser(table, productions)

    # get another copy of the set of tokens from file to pass to Shunting Yard algorithm
    symbol_table4 = {}
    lexer2 = Lexer(text1)
    tokens2 = lexer2.gen_tokens(symbol_table4)
    toks1 = list(tokens2)

    print("\nEnd of file. Done processing.\n")
    # ----------------------------------------------------------------------------------

