from lexer import Lexer
from parse import Parser
from file import File

with open('prog.txt', 'r') as file:
    text = file.read()

lexer = Lexer(text)
tokens = lexer.gen_tokens()
# print(list(tokens))  # only used for token testing - don't use once tokens done!

res = open('nasm_progtxt.asm', 'w')
f = File(res)
f.init_file()

parser = Parser(tokens, f)
parser.parse() 

f.finish_file()
