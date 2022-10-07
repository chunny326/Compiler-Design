
class File():
    def __init__(self, f):
        self.f = f

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
                            '\n',

                            ';-----------------------------\n',
                            '; Code! (execution starts at main)\n',
                            ';-----------------------------\n',
                            'section .text\n',
                            'printInt:\n',
                            '\t\t; We need to call printf, but we are using rax, rbx, and rcx.  printf\n',
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
                            '\t\tsub     rsp, 336                ; Allocate space on the stack\n',
                            '\n'
                            ])

    def finish_file(self):    
        self.f.writelines([
                            '\n',
                            '\t\t; All done.\n',
                            '\t\tmov       rax, 60                 ; system call for exit\n',
                            '\t\txor       rdi, rdi                ; Put an exit code of 0 into the rdi register\n',
                            '\t\tsyscall                           ; invoke operating system to exit\n'
                            ])
        self.f.close()

    def addition(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val1) +  '       ; 64 bit value loading of data values only through rax\n',
                            '\t\tmov     rbx, ' + str(val2) +  '\n',
                            '\t\tadd     rax, rbx\n'
                           ])

    def subtraction(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val1) +  '       ; 64 bit value loading of data values only through rax\n',
                            '\t\tmov     rbx, ' + str(val2) +  '\n',
                            '\t\tsub     rax, rbx\n'
                           ])
    
    def multiplication(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rax, ' + str(val1) +  '       ; 64 bit value loading of data values only through rax\n',
                            '\t\tmov     rbx, ' + str(val2) +  '\n',
                            '\t\timul    rax, rbx\n'
                           ])
    
    def division(self, val1, val2):
        self.f.writelines([
                            '\t\tmov     rdx, 0\n',
                            '\t\tmov     rax, ' + str(val1) + '\n',
                            '\t\tmov     rcx, ' + str(val2) + '\n',
                            '\t\tdiv     rcx\n'
                           ])
    
    def print_console(self, offset):
        self.f.writelines([
                            '\t\tmov     rax, ' + offset + '       ; 64 bit value loading of data values only through rax\n',
                            '\t\tcall    printInt\n'
                           ])

    def variable_assign(self, offset, val):
        self.f.writelines([
                            '\t\tmov     ' + offset + ', ' + str(val) + '        ; Push variable onto stack\n'
                           ])

    def variable_assign_variable(self, offset1, offset2):
        self.f.writelines([
                            '\t\tmov     rax, ' + offset2 + '\n'
                            '\t\tmov     ' + offset1 + ', rax        ; Push variable onto stack\n'
                           ])