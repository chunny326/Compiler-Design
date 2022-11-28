section .data
flum1:    dq      3.141_592_653_589_79          
format:   db      "%g", 10, 0

          global main
          extern printf
          section .text

main:
          push rbp
          mov  rbp, rsp
          ; Doesn't work
          ;movss  xmm0, [flum1]

          ; This does work
          ;mov    rax,  [flum1]
          ;movq   xmm0, rax
       
          ; This also works
          ;mov    rax, __float64__(3.14159265358979)
          ;movq   xmm0, rax
          sub    rsp, 0x20
          mov    rax, __float64__(3.14159265358979)
          mov    [rbp-0x18], rax
          mov    rax, __float64__(2.718)
          mov    [rbp-0x10], rax
          movsd  xmm0, QWORD [rbp-0x18]
          addsd  xmm0, QWORD [rbp-0x10]
          mov    rdi,  format        ; 1st argument to printf
          mov    rax,  1             ; printf is varargs, there is 1 non-int argument
          call   printf  

          movsd  xmm0, QWORD [rbp-0x18] ; Get left operand into xmm0

          mulsd  xmm0, [rbp-0x10] ; Multiply first operand with second

          mov    rdi,  format        ; 1st argument to printf
          mov    rax,  1             ; printf is varargs, there is 1 non-int argument
          call   printf  
          
          add    rsp, 0x20
          pop    rbp
          xor    rax, rax
          ret