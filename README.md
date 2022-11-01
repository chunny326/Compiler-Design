# Compiler Design - CS 6820

## Assignment 1 - Initial End-to-End Compiler

Instructions for running:
  
Enter the following into the terminal from within the Assignment 1 directory:
```
python3 main.py
nasm -felf64 nasm_progtxt.asm; gcc -no-pie nasm_progtxt.o -o nasm_progtxt; ./nasm_progtxt
```
  
The file nasm_progtxt.asm will be generated and the output of running this file will be printed to the console.
  
-------------------------------------------------------------------------------------------------

## Assignment 2 - LL(1) Tokenization and Parsing

Instructions for running:
  
Enter the following into the terminal from within the Assignment 2 directory:
```
rm assignment2_parse_results.txt; python3 main.py | tee assignment2_parse_results.txt
```
  
This will delete the old results output file assignment2_parse_results.txt. 
It will then run the LL1 tokenization and parsing of the input files. 
The results will be copied to both the terminal and the output file assignment2_parse_results.txt.

The results of parsing ```ll1_valid_book.txt``` and ```ll1_invalid_book.txt``` will be output using the grammar specified in the textbook.
The results of parsing ```ll1_valid_class.txt``` and ```ll1_invalid_book.txt``` will then be output using the grammar with my added productions. 

-------------------------------------------------------------------------------------------------

## Assignment 3 - LL(1) to IR

Instructions for running:
  
Enter the following into the terminal from within the Assignment 3 directory:
```
rm assignment3_parse_results.txt; python3 main.py | tee assignment3_parse_results.txt
```
  
This will delete the old results output file assignment3_parse_results.txt. 
It will then run the LL1 tokenization and parsing of the input file ll1_to_ir.txt. 
The results will be copied to both the terminal and the output file assignment3_parse_results.txt.
