class File():
    def __init__(self, f):
        self.f = f
        self.type_flag = ''
        self.temp_var_counter = 1
        self.stack_offset = 0
        self.label_counter = 0
        self.scope_names = []
        self.scope_level = 0
        self.prev_node = ''
        self.params_offset = []
        self.num_func_params = 0
        self.num_func_params_list = {}
        self.params_counted = [False, False, False]

    def init_file(self):
        self.f.writelines([
                            ';-----------------------------\n',
                            '; exports\n',
                            ';-----------------------------\n',
                            'GLOBAL main\n',
                            '\n',

                            ';-----------------------------\n',
                            '; imports\n',
                            ';-----------------------------\n',
                            'extern printf\n',
                            'extern scanf\n',
                            'extern exit\n',

                            ';-----------------------------\n',
                            '; initialized data\n',
                            ';-----------------------------\n',
                            'section .data\n',
                            '\n',
                            'fmtint:\t db\t\t"%d", 10, 0\n',
                            'fmtflt:\t db\t\t"%g", 10, 0\n',
                            '\n',

                            ';-----------------------------\n',
                            '; Code! (execution starts at main)\n',
                            ';-----------------------------\n',
                            'section .text\n',
                            'printInt:\n',
                            '\t\t; We need to call printf, but we are using rax, rbx, and rcx. printf\n',
                            '\t\t; may destroy rax and rcx so we will save these before the call and\n',
                            '\t\t; restore them afterwards.\n',
                            '\t\tpush    rbp                     ; Avoid stack alignment isses\n',
                            '\t\tmov     rbp, rsp\n',
                            '\t\tpush    rax                     ; save rax,rcx, rsi, and rdi\n',
                            '\t\tpush    rcx\n',
                            '\t\tpush    rsi\n',
                            '\t\tpush    rdi\n',
                            '\n',
                            '\t\tmov     rsi, rax                ; set printf format parameter\n',
                            '\t\tmov     rdi, fmtint             ; set printf value parameter\n',
                            '\t\tmov     rax, 0                  ; printf is varargs, # of non-integer arguments\n',
                            '\t\tcall    printf\n'
                            '\n',
                            '\t\tpop     rdi                     ; restore rdi\n',
                            '\t\tpop     rsi                     ; restore rsi\n',
                            '\t\tpop     rcx                     ; restore rcx\n',
                            '\t\tpop     rax                     ; restore rax\n',
                            '\t\tmov     rsp, rbp\n'
                            '\t\tpop     rbp                     ; Avoid stack alignment issues\n',
                            '\n',
                            '\t\tret\n',
                            '\n',
                            'main:\n',
                            '\t\tpush    rbp\n',
                            '\t\tmov     rbp, rsp\n',
                            '\t\tsub     rsp, 1120               ; Allocate space on the stack\n',
                            '\n'
                            ])

    def finish_file(self):    
        self.f.writelines([
                            '\n',
                            '\t\t; All done.\n',
                            '\t\tmov     rax, 60                 ; system call for exit\n',
                            '\t\txor     rdi, rdi                ; Put an exit code of 0 into the rdi register\n',
                            '\t\tsyscall                         ; invoke operating system to exit\n'
                            ])
        self.f.close()

    def int_addition(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val1) +  '       ; 64 bit value loading of data values only through rax\n',
                            '\t\tmov     rbx, ' + str(val2) +  '\n',
                            '\t\tadd     rax, rbx\n'
                           ])

    def float_addition(self, val1, val2):
        self.f.writelines([
                            '\t\tmovsd   xmm0, ' + str(val1) +  '      ; 64 bit value loading of data values only through rax\n',
                            '\t\taddsd   xmm0, ' + str(val2) +  '\n'
                           ])

    def subtraction(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val1) +  '       ; 64 bit value loading of data values only through rax\n',
                            '\t\tmov     rbx, ' + str(val2) +  '\n',
                            '\t\tsub     rax, rbx\n'
                           ])
    
    def int_multiplication(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val1) +  '       ; 64 bit value loading of data values only through rax\n',
                            '\t\tmov     rbx, ' + str(val2) +  '\n',
                            '\t\timul    rax, rbx\n'
                           ])
    
    def float_multiplication(self, val1, val2):
        self.f.writelines([
                            '\t\tmovsd   xmm0, ' + str(val1) +  '      ; 64 bit value loading of data values only through xmm0\n',
                            '\t\tmovsd   xmm1, ' + str(val2) +  '      ; 64 bit value loading of data values only through xmm1\n',
                            '\t\tmulsd   xmm0, xmm1\n'
                           ])

    def division(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val1) + '\n',
                            '\t\tmov     rcx, ' + str(val2) + '\n',
                            '\t\tcqo\n',
                            '\t\tidiv    rcx\n'
                           ])
    
    def print_int(self, offset):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(offset) + '  ; 64 bit value loading of data values only through rax\n',
                            '\t\tcall    printInt\n'
                           ])

    def print_float(self, offset):
        self.f.writelines([
                            '\t\tmovsd   xmm0, ' + offset + '      ; xmm0 holds value to print for floats\n',
                            '\t\tmov     rdi,  fmtflt              ; 1st argument to printf\n',
                            '\t\tmov     rax,  1                   ; printf is varargs, there is 1 non-int argument\n',
                            '\t\tcall    printf\n'
                           ])

    def int_variable_assign(self, offset, val):
        self.f.writelines([
                            '\t\tmov     ' + offset + ', ' + str(val) + '        ; Push variable onto stack\n'
                           ])

    def int_variable_assign_variable(self, offset1, offset2):
        self.f.writelines([
                            '\t\tmov     rax, ' + offset2 + '\n'
                            '\t\tmov     ' + offset1 + ', rax            ; Push variable onto stack\n'
                           ])

    def float_variable_assign(self, offset1, offset2):
        self.f.writelines([
                            '\t\tmov     rax, __float64__(' + str(offset2) + ')\n'
                            '\t\tmov     ' + str(offset1) + ', rax       ; Push variable onto stack\n'
                           ])

    def float_variable_assign_var(self, offset1, offset2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(offset2) + '\n'
                            '\t\tmov     ' + str(offset1) + ', rax       ; Push variable onto stack\n'
                           ])

    def add_result_to_stack(self, reg, offset):
        self.f.writelines([
                            '\t\tmov     ' + offset + ', ' + reg + '     ; Push variable onto stack\n'
                           ])

    def add_flum_result_to_stack(self, offset):
        self.f.writelines([
                            '\t\tmovsd   ' + offset + ', xmm0             ; Push variable onto stack\n'
                           ])

    def if_compare(self, val, if_name):
        self.f.writelines([
                            '\t\tcmp     ' + val + ', 0      ; Compare value to 0\n',
                            '\t\tjz      ' + if_name + 'Done                    ; Skip if statement if 0\n'
                           ])

    def while_compare(self, val, while_name):
        self.f.writelines([
                            while_name + ':                                ; Beginning of while loop\n',
                            '\t\tcmp     ' + val + ', 0      ; Compare value to 0\n',
                            '\t\tjz      ' + while_name + 'Done                    ; Skip if statement if 0\n'
                           ])

    def if_scope_done(self, scope_name):
        self.f.writelines([
                            scope_name + 'Done:                                   ; End of if statement\n'
                           ])

    def while_scope_done(self, scope_name):
        self.f.writelines([
                            '\t\tjmp    ' + scope_name + '                    ; Skip if statement if 0\n',
                            scope_name + 'Done:                                   ; End of if statement\n'
                           ])

    def function_def(self, func_name):
        self.f.writelines([
                            '\n\t\tjmp    ' + func_name + 'Done                     ; Skip over function definition\n',
                            func_name + ':                                ; Beginning of function call\n',
                            '\n'
                           ])             

    def function_return_int(self, val):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val) + '     ; return value stored in rax\n'
                           ])

    def function_return_var(self, val):
        self.f.writelines([
                            '\t\tmov     rax, ' + val + '     ; return value stored in rax\n'
                           ])

    def function_done(self, func_name):
        self.f.writelines([
                            '\n',
                            '\t\tjmp     ' + func_name + 'CallDone\n',
                            '\n',
                            func_name + 'Done:                                ; End of function call\n'
                           ])

    def func_call(self, func_name):
        self.f.writelines([
                            '\t\tjmp     ' + func_name + '                  ; call function\n',
                            func_name + 'CallDone:                                ; End of function call\n'
                           ])                            

    def check_stack_top(self, top, symbol_table):
        if isinstance(top[0], int) or isinstance(top[0], float):
            self.type_flag = 'number'
            return top[0]
        elif 'param' in top[0]:
            self.type_flag = 'param'
            if top[0] == 'param1':
                param_offset = self.params_offset[0]
            elif top[0] == 'param2':
                param_offset = self.params_offset[1]
            elif top[0] == 'param3':
                param_offset = self.params_offset[2]
            offset = 'qword[rsp + ' + str(param_offset) + ']'
            top_ret = [('param', param_offset, 0, top[1])]
        else:
            self.type_flag = 'variable'
            if len(symbol_table[top[0]]) - 1 >= top[1]:
                offset = 'qword[rsp + ' + str(symbol_table[top[0]][top[1]][0][1]) + ']'
                top_ret = symbol_table[top[0]][top[1]]
            # deeper scope is set, but variable is from higher scope level
            else:
                find_var = top[1]
                while True:
                    try:
                        offset = 'qword[rsp + ' + str(symbol_table[top[0]][find_var][0][1]) + ']'
                        top_ret = symbol_table[top[0]][find_var]
                        break
                    except IndexError:
                        find_var -= 1
                        continue

        return offset, top_ret

    def convert_post_order(self, post_order, symbol_table):
        operators = ['+', '-', '*', '/', '^', '-u', '=', 'print', 'if', 'while']

        for tree in post_order:
            first, *_, last = symbol_table.values()

            # find where to add temporary variables to the stack ()
            self.stack_offset = last[-1][0][1]

            # location of function parameter variables
            self.params_offset = [self.stack_offset + 64, self.stack_offset + 72, self.stack_offset + 80]

            # stack to help process post-order tree
            stack = []

            self.prev_node = ''
            
            # process each line of the file
            for node in tree:
                if node[0] in operators:
                    top1 = self.check_stack_top(stack.pop(), symbol_table)
                    
                    if node[0] == 'print':
                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]

                        if isinstance(top1, int) or isinstance(top1[0], int) or (isinstance(top1, tuple) and top1[1][0][0] == 'num'):
                            self.print_int(num1)
                        elif isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top1, tuple) and top1[1][0][0] == 'flum'):
                            self.print_float(num1)
                    
                    elif node[0] == 'if':
                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]
                        
                        # add new label to scope stack, write nasm to evaluate if statement
                        self.scope_names.append("if" + str(self.label_counter)) 
                        self.if_compare(num1, self.scope_names[-1])
                        self.label_counter += 1
                        self.scope_level += 1
                    
                    elif node[0] == 'while':
                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]
                        
                        # add new label to scope stack, write nasm to evaluate if statement
                        self.scope_names.append("while" + str(self.label_counter)) 
                        self.while_compare(num1, self.scope_names[-1])
                        self.label_counter += 1
                        self.scope_level += 1

                    elif node[0] == '-u':
                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]

                        # perform unary operation
                        if isinstance(top1, int) or isinstance(top1[0], int) or (isinstance(top1, tuple) and top1[1][0][0] == 'num'):
                            self.int_multiplication(num1, -1)
                            op = 'num'
                        elif isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top1, tuple) and top1[1][0][0] == 'flum'):
                            self.float_multiplication(num1, -1)
                            op = 'flum'

                        # add result back to stack and symbol table
                        self.stack_offset += 8 
                        if op == 'num':
                            self.add_result_to_stack('rax', 'qword[rsp + ' + str(self.stack_offset) + ']')
                        elif op == 'flum':
                            self.add_flum_result_to_stack('qword[rsp + ' + str(self.stack_offset) + ']')
                        temp = 'temp' + str(self.temp_var_counter)
                        symbol_table[temp] = [[(op, self.stack_offset, 0, 0)]]
                        stack.append((temp, 0))
                        self.temp_var_counter += 1

                    elif node[0] == '=':
                        # get variable from symbol table
                        top2 = self.check_stack_top(stack.pop(), symbol_table)

                        # perform int operation
                        if top2[1][0][0] == 'num':
                            if isinstance(top1, int):
                                self.int_variable_assign(top2[0], top1)
                            else:
                                self.int_variable_assign_variable(top2[0], top1[0])
                        # perform floating-point operation
                        elif top2[1][0][0] == 'flum':
                            if isinstance(top1, float):
                                self.float_variable_assign(top2[0], top1)
                            else:
                                self.float_variable_assign_var(top2[0], top1[0])

                    elif node[0] == '+':
                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]

                        # get second value from stack
                        top2 = self.check_stack_top(stack.pop(), symbol_table)

                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num2 = top2
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num2 = top2[0]
                        
                        # perform addition
                        if isinstance(top1, int) or isinstance(top1[0], int) or (isinstance(top1, tuple) and top1[1][0][0] in ['num', 'param']):
                            if isinstance(top2, int) or isinstance(top2[0], int) or \
                              (isinstance(top2, tuple) and top2[1][0][0] in ['num', 'param']):
                                self.int_addition(num2, num1)
                                op = 'num'
                        elif isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top1, tuple) and top1[1][0][0] == 'flum') or \
                             isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top2, tuple) and top2[1][0][0] == 'flum'):
                            self.float_addition(num2, num1)
                            op = 'flum'

                        # add result back to stack and symbol table
                        self.stack_offset += 8 
                        if op == 'num':
                            self.add_result_to_stack('rax', 'qword[rsp + ' + str(self.stack_offset) + ']')
                        elif op == 'flum':
                            self.add_flum_result_to_stack('qword[rsp + ' + str(self.stack_offset) + ']')
                        temp = 'temp' + str(self.temp_var_counter)
                        symbol_table[temp] = [[(op, self.stack_offset, 0, 0)]]
                        stack.append((temp, 0))
                        self.temp_var_counter += 1

                    elif node[0] == '-':
                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]

                        # get second value from stack
                        top2 = self.check_stack_top(stack.pop(), symbol_table)

                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num2 = top2
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num2 = top2[0]
                        
                        # perform subtraction
                        if isinstance(top1, int) or isinstance(top1[0], int) or (isinstance(top1, tuple) and top1[1][0][0] in ['num', 'param']):
                            if isinstance(top2, int) or isinstance(top2[0], int) or \
                              (isinstance(top2, tuple) and top2[1][0][0] in ['num', 'param']):
                                self.subtraction(num2, num1)
                                op = 'num'

                        # add result back to stack and symbol table
                        self.stack_offset += 8 
                        if op == 'num':
                            self.add_result_to_stack('rax', 'qword[rsp + ' + str(self.stack_offset) + ']')
                        elif op == 'flum':
                            self.add_flum_result_to_stack('qword[rsp + ' + str(self.stack_offset) + ']')
                        temp = 'temp' + str(self.temp_var_counter)
                        symbol_table[temp] = [[(op, self.stack_offset, 0, 0)]]
                        stack.append((temp, 0))
                        self.temp_var_counter += 1

                    elif node[0] == '*':
                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]

                        # get second value from stack
                        top2 = self.check_stack_top(stack.pop(), symbol_table)

                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num2 = top2
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num2 = top2[0]
                        
                        # perform multiplication
                        if isinstance(top1, int) or isinstance(top1[0], int) or (isinstance(top1, tuple) and top1[1][0][0] in ['num', 'param']):
                            if isinstance(top2, int) or isinstance(top2[0], int) or \
                              (isinstance(top2, tuple) and top2[1][0][0] in ['num', 'param']):
                                self.int_multiplication(num2, num1)
                                op = 'num'
                        elif isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top1, tuple) and top1[1][0][0] == 'flum') or \
                             isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top2, tuple) and top2[1][0][0] == 'flum'):
                            self.float_multiplication(num2, num1)
                            op = 'flum'

                        # add result back to stack and symbol table
                        self.stack_offset += 8 
                        if op == 'num':
                            self.add_result_to_stack('rax', 'qword[rsp + ' + str(self.stack_offset) + ']')
                        elif op == 'flum':
                            self.add_flum_result_to_stack('qword[rsp + ' + str(self.stack_offset) + ']')
                        temp = 'temp' + str(self.temp_var_counter)
                        symbol_table[temp] = [[(op, self.stack_offset, 0, 0)]]
                        stack.append((temp, 0))
                        self.temp_var_counter += 1

                    elif node[0] == '/':
                         # check if constant value from stack
                        if self.type_flag == 'number':
                            num1 = top1
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num1 = top1[0]

                        # get second value from stack
                        top2 = self.check_stack_top(stack.pop(), symbol_table)

                        # check if constant value from stack
                        if self.type_flag == 'number':
                            num2 = top2
                        # check if variable that needs to pulled from symbol table
                        elif self.type_flag == 'variable' or self.type_flag == 'param':
                            num2 = top2[0]
                        
                        # perform division
                        if isinstance(top1, int) or isinstance(top1[0], int) or (isinstance(top1, tuple) and top1[1][0][0] in ['num', 'param']):
                            if isinstance(top2, int) or isinstance(top2[0], int) or \
                              (isinstance(top2, tuple) and top2[1][0][0] in ['num', 'param']):
                                self.division(num2, num1)
                                op = 'num'
                        elif isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top1, tuple) and top1[1][0][0] == 'flum') or \
                             isinstance(top2, float) or isinstance(top2[0], float) or (isinstance(top2, tuple) and top2[1][0][0] == 'flum'):
                            self.float_division(num2, num1)
                            op = 'flum'

                        # add result back to stack and symbol table
                        self.stack_offset += 8 
                        if op == 'num':
                            self.add_result_to_stack('rax', 'qword[rsp + ' + str(self.stack_offset) + ']')
                        elif op == 'flum':
                            self.add_flum_result_to_stack('qword[rsp + ' + str(self.stack_offset) + ']')
                        temp = 'temp' + str(self.temp_var_counter)
                        symbol_table[temp] = [[(op, self.stack_offset, 0, 0)]]
                        stack.append((temp, 0))
                        self.temp_var_counter += 1
                
                # check if function
                elif node[0] in symbol_table and symbol_table[node[0]][0][0] == 'function':
                    # check if function declaration
                    if self.prev_node == '{':
                        self.prev_node = ''

                        # add new function label to scope stack, write nasm for function definition
                        self.scope_names.append(node[0]) 
                        self.function_def(self.scope_names[-1])
                        self.scope_level += 1
                    # function call
                    else:
                        # move parameters into locations
                        for i in range(0, self.num_func_params_list[node[0]]):
                            # get value from stack
                            stack_top = stack.pop()
                            val = self.check_stack_top(stack_top, symbol_table)

                            # check if constant value from stack
                            if isinstance(val, int):
                                self.int_variable_assign('qword[rsp + ' + str(self.params_offset[i]) + ']', val)
                            # check if variable that needs to pulled from symbol table
                            elif stack_top[0] in symbol_table:
                                self.int_variable_assign_variable('qword[rsp + ' + str(self.params_offset[i]) + ']', 'qword[rsp + ' + str(symbol_table[stack_top[0]][0][0][1]) + ']')
                            # stack top is a parameter location
                            else:
                                self.int_variable_assign_variable('qword[rsp + ' + str(self.params_offset[i]) + ']', 'qword[rsp + ' + str(val) + ']')
                            
                        # call function
                        self.func_call(node[0])
                        
                        # add result to stack and symbol table
                        self.stack_offset += 8 
                        self.add_result_to_stack('rax', 'qword[rsp + ' + str(self.stack_offset) + ']')
                        temp = 'temp' + str(self.temp_var_counter)
                        symbol_table[temp] = [[('num', self.stack_offset, 0, 0)]]
                        stack.append((temp, 0))
                        self.temp_var_counter += 1

                # function needs to return a value
                elif node[0] == 'gift':
                    # return value from function, stored in rax
                    if isinstance(top1, int):
                        self.function_return_int(top1)
                    else:
                        self.function_return_var(top1[0])

                    self.num_func_params_list[self.scope_names[-1]] = self.num_func_params
                    self.num_func_params = 0
                    self.params_counted = [False, False, False]

                elif node[0] == '}':
                    # if, while, or function scope has ended
                    label = self.scope_names.pop()
                    if 'while' in label:
                        self.while_scope_done(label)
                    elif 'if' in label:
                        self.if_scope_done(label)
                    elif 'func' in symbol_table[label][0][0]:
                        self.function_done(label)
                    self.scope_level -= 1
                
                elif node[0] == '{':
                    self.prev_node = '{'
                    pass

                # keep track of number of function parameters
                elif not isinstance(node[0], int) and 'param' in node[0]:
                    stack.append(node)

                    if node[0] == 'param1' and not self.params_counted[0]:
                        self.params_counted[0] = True
                        self.num_func_params += 1
                    elif node[0] == 'param2' and not self.params_counted[1]:
                        self.params_counted[1] = True
                        self.num_func_params += 1
                    elif node[0] == 'param3' and not self.params_counted[2]:
                        self.params_counted[2] = True
                        self.num_func_params += 1
                        
                # add everything else (numbers and variables) directly to the stack
                else:                
                    stack.append(node)
                
                self.type_flag = ''

            for i in range(1, self.temp_var_counter):
                symbol_table.popitem()
            self.temp_var_counter = 1
            
        