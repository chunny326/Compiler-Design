section .text
          extern printf
          global main
printInt:
          push    rbp
          mov     rbp, rsp 
          push    rax
          push    rcx
          push    rsi
          push    rdi
          ; If I need new variables, I could extend rsp

          mov     rsi, rax        ; Prepare to print it
          mov     rdi, fmtint     ; Put the address of "%d" in rdi
          mov     rax, 0          ; printf is varargs, # of non-integer arguments
          call    printf
          
          pop     rdi
          pop     rsi
          pop     rcx
          pop     rax 
          mov     rsp, rbp
          pop     rbp

          ret
main:
          mov     rax, 1          ; system call for write 
          mov     rdi, 1          ; file handle 1 stdout
          mov     rsi, message    ; address of string to print
          mov     rdx, 13         ; number of bytes in the string
          syscall
          
          sub     rsp, 16         ; Set aside room for 2 64 bit values
          
          mov     qword[rsp+8], 42 ; Put the value 42 in the stack
          mov     qword[rsp], 43; Put the value 42 in the stack
          
          mov     rax, [rsp+8]
          call    printInt
          mov     rax, [rsp]
          call    printInt
          mov     rax, [rsp+8]
          call    printInt
          

          mov     rax, 60         ; system call for exit
          xor     rdi, rdi        ; return value of 0
          syscall

          section .data
message:  db      "Hello, World", 10 ;10 is newline
fmtint:   db      "%d", 10, 0  