from tokens import TokenType, Token

# assign all operators precedence
operator_prec = {
    'UMINUS': 0, # unary minus operator
    'POW':    1,
    'MUL':    2,
    'DIV':    2,
    'PLUS':   3,
    'MINUS':  3
}

def higher_precedence(op1, op2):
    return operator_prec[op1.type.name] <= operator_prec[op2.type.name]

def peek_ops(stack):
    return stack[-1] if stack else None

# calculate if operator has two numerical operands
def optimize_expr(ops, vals):
    op = ops.pop()
    r = vals.pop()

    # check for divide-by-zero error
    if op == '/' and r == 0:
        vals.append('error')
        return

    l = vals.pop()
    vals.append(eval("{0}{1}{2}".format(l, op, r)))

def shunting_yard(tokens):
    op_stack = []    
    out_queue = []        # final output queue for whole file
    line_queue = []       # result queue for each line of file
    prev_tok = 'f'        # used to distinguish between unary and binary minus...
                          #   minus is unary if it immediately follows an operand 
                          #   or right parens, or occurs at the beginning of input

    for tok in tokens:
        # each line ends with newline 'eof' character
        if tok.type.value != 'eof':
            # keep going until file is completely processed
            if tok.type.name == 'EOF':
                print("Shunting Yard algorithm done processing.\n")
            
            elif tok.type.value == 'name' or tok.type.value == 'num': 
                # add token to back of queue if it is a value or variable
                line_queue.append(tok.value)
                prev_tok = '#'
            
            elif tok.type.name in operator_prec.keys():
                # if token is an operator, one-by-one remove all operators
                #   of higher or equal precedence in the stack and move
                #   each to back of queue, then add this operator to stack
                if tok.type.value == '-' and prev_tok in ['f', 'op', '(']:
                    tok = Token(TokenType.UMINUS)
                
                top = peek_ops(op_stack)
                while top is not None and top.type.value not in "()" and higher_precedence(top, tok):
                    line_queue.append(op_stack.pop().type.value)
                    top = peek_ops(op_stack)
                
                prev_tok = 'op'
                op_stack.append(tok)
            
            # opening parens behaves like beginning of an expression
            elif tok.type.value == '(':
                op_stack.append(tok)
                prev_tok = '('
            
            # behaves like end of expression, so pop off all remaining operators
            elif tok.type.value == ')':
                top = peek_ops(op_stack)
                prev_tok = ')'
                
                # go until opening parens is found
                while top is not None and top.type.value != '(':
                    line_queue.append(op_stack.pop().type.value)
                    top = peek_ops(op_stack)
                
                # discard '(' as it is not used in post-fix notation
                if top.type.value == '(':
                    op_stack.pop()

        # line is done processing, so add post-order traversal results to main output queue
        else:
            while peek_ops(op_stack) is not None:
                # add remaining operators on stack to output
                line_queue.append(op_stack.pop().type.value)
            out_queue.append(line_queue)
            line_queue = []
            prev_tok = 'f'

    return out_queue