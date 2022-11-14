;----------------------------------------------------------------------------
; 64-bit helloworld in assembly, using printf() from C
; Modified from here: https://montcs.bloomu.edu/~bobmon/Code/Asm.and.C/Asm.Nasm/hello-printf-64.asm.html
;----------------------------------------
; Assemble in 64-bit:   nasm  -f elf64 -o hp64.o -l hp64.lst  hello-printf-64.asm
;
; Link:                 gcc -no-pie -o hp64 -hp64.o
;
; run:          ./hp64
;----------------------------------------------------------------------------
        SECTION .data

fmtint: db "%d", 10, 0   ; Comma concatenates.  The 10 is the \n followed by a \0

        SECTION .text
        extern printf
        global main
main:


        mov rsi, 42      ; 64-bit ABI passing order starts w/ edi, esi, ...
        mov rdi, fmtint  ;
        mov rax, 0       ; printf is varargs, so EAX counts # of non-integer arguments being passed
        call printf

        mov rbx, 0      ; normal-exit code
        mov rax, 1      ; process-termination service
        int 0x80        ; linux kernel service
;----------------------------------------------------------------------------
