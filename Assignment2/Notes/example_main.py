
###########################################################################
# use this to test each line
# while True:
#     try:
#         text = input("calc > ")
#         lexer = Lexer(text)
#         tokens = lexer.gen_tokens()
#         # print(list(tokens))  # only used for intermediate checking, don't use after tokens complete
#         parser = Parser(tokens)
#         tree = parser.parse()
#         print(tree)
#         if not tree: continue
#         interpreter = Interpreter()
#         value = interpreter.visit(tree)
#         print(value)
#     except Exception as e:
#         print(e)

# # use this to test each line
# while True:
#     try:
#         text = input("calc > ")
#         lexer = Lexer(text)
#         tokens = lexer.gen_tokens()
#         # print(list(tokens))  # only used for intermediate checking, don't use after tokens complete
#         parser = Parser(tokens)
#         tree = parser.parse()
#         # print(tree)
#         if not tree: continue
#         interpreter = Interpreter()
#         value = interpreter.visit(tree)
#         print(value)
#     except Exception as e:
#         print(e)
