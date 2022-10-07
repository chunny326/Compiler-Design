;-----------------------------
; exports
;-----------------------------
GLOBAL main

;-----------------------------
; imports
;-----------------------------
extern printf
extern scanf
extern exit
;-----------------------------
; initialized data
;-----------------------------
section .data

fmtint:	 db		"%d", 10, 0

;-----------------------------
; Code! (execution starts at main)
;-----------------------------
section .text
printInt:
		; We need to call printf, but we are using rax, rbx, and rcx.  printf
		; may destroy rax and rcx so we will save these before the call and
		; restore them afterwards.
		push    rbp                     ; Avoid stack alignment isses
		mov     rbp, rsp
		push    rax                     ; save rax,rcx, rsi, and rdi
		push    rcx
		push    rsi
		push    rdi

		mov     rsi, rax                ; set printf format parameter
		mov     rdi, fmtint             ; set printf value parameter
		mov     rax, 0                  ; printf is varargs, # of non-integer arguments
		call    printf

		pop     rdi                     ; restore rdi
		pop     rsi                     ; restore rsi
		pop     rcx                     ; restore rcx
		pop     rax                     ; restore rax
		mov     rsp, rbp
		pop     rbp                     ; Avoid stack alignment issues

		ret

main:
		push    rbp
		mov     rbp, rsp
		sub     rsp, 336                ; Allocate space on the stack

		mov     qword[rsp+0], 3        ; Push variable onto stack
		mov     rax, qword[rsp+0]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+0]       ; 64 bit value loading of data values only through rax
		mov     rbx, 9
		add     rax, rbx
		mov     qword[rsp+8], rax        ; Push variable onto stack
		mov     rax, qword[rsp+8]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+16], 4        ; Push variable onto stack
		mov     rax, qword[rsp+16]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+16]
		add     rax, rbx
		mov     qword[rsp+24], rax        ; Push variable onto stack
		mov     rax, qword[rsp+24]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 7       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+16]
		add     rax, rbx
		mov     qword[rsp+32], rax        ; Push variable onto stack
		mov     rax, qword[rsp+32]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+8]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+8]
		add     rax, rbx
		mov     qword[rsp+40], rax        ; Push variable onto stack
		mov     rax, qword[rsp+40]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 2
		add     rax, rbx
		mov     qword[rsp+48], rax        ; Push variable onto stack
		mov     rax, qword[rsp+48]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+8]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+8]
		add     rax, rbx
		mov     qword[rsp+8], rax        ; Push variable onto stack
		mov     rax, qword[rsp+8]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+16]
		mov     qword[rsp+8], rax        ; Push variable onto stack
		mov     rax, qword[rsp+8]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+8], 1000        ; Push variable onto stack
		mov     rax, qword[rsp+8]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+56], 8        ; Push variable onto stack
		mov     rax, qword[rsp+56]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+56]       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		sub     rax, rbx
		mov     qword[rsp+64], rax        ; Push variable onto stack
		mov     rax, qword[rsp+64]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+72], 40        ; Push variable onto stack
		mov     rax, qword[rsp+72]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+72]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+56]
		sub     rax, rbx
		mov     qword[rsp+80], rax        ; Push variable onto stack
		mov     rax, qword[rsp+80]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 7       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+64]
		sub     rax, rbx
		mov     qword[rsp+88], rax        ; Push variable onto stack
		mov     rax, qword[rsp+88]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+64]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+64]
		sub     rax, rbx
		mov     qword[rsp+96], rax        ; Push variable onto stack
		mov     rax, qword[rsp+96]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 2
		sub     rax, rbx
		mov     qword[rsp+104], rax        ; Push variable onto stack
		mov     rax, qword[rsp+104]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+64]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+64]
		sub     rax, rbx
		mov     qword[rsp+64], rax        ; Push variable onto stack
		mov     rax, qword[rsp+64]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+72]
		mov     qword[rsp+64], rax        ; Push variable onto stack
		mov     rax, qword[rsp+72]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+64], 1000        ; Push variable onto stack
		mov     rax, qword[rsp+64]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+112], 3        ; Push variable onto stack
		mov     qword[rsp+120], 4        ; Push variable onto stack
		mov     rax, qword[rsp+112]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+120]
		sub     rax, rbx
		mov     qword[rsp+128], rax        ; Push variable onto stack
		mov     rax, qword[rsp+112]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+120]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+128]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+136], 3        ; Push variable onto stack
		mov     rax, qword[rsp+136]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+136]       ; 64 bit value loading of data values only through rax
		mov     rbx, 9
		imul    rax, rbx
		mov     qword[rsp+144], rax        ; Push variable onto stack
		mov     rax, qword[rsp+144]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+152], 4        ; Push variable onto stack
		mov     rax, qword[rsp+136]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+152]
		imul    rax, rbx
		mov     qword[rsp+160], rax        ; Push variable onto stack
		mov     rax, qword[rsp+160]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 7       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+152]
		imul    rax, rbx
		mov     qword[rsp+168], rax        ; Push variable onto stack
		mov     rax, qword[rsp+168]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+144]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+144]
		imul    rax, rbx
		mov     qword[rsp+176], rax        ; Push variable onto stack
		mov     rax, qword[rsp+176]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 2
		imul    rax, rbx
		mov     qword[rsp+184], rax        ; Push variable onto stack
		mov     rax, qword[rsp+184]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+144]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+144]
		imul    rax, rbx
		mov     qword[rsp+144], rax        ; Push variable onto stack
		mov     rax, qword[rsp+144]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+152]
		mov     qword[rsp+144], rax        ; Push variable onto stack
		mov     rax, qword[rsp+144]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+144], 1000        ; Push variable onto stack
		mov     rax, qword[rsp+144]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+192], 8        ; Push variable onto stack
		mov     qword[rsp+200], 2        ; Push variable onto stack
		mov     qword[rsp+208], 4        ; Push variable onto stack
		mov     rdx, 0
		mov     rax, qword[rsp+192]
		mov     rcx, qword[rsp+200]
		div     rcx
		mov     qword[rsp+216], rax        ; Push variable onto stack
		mov     rdx, 0
		mov     rax, qword[rsp+192]
		mov     rcx, qword[rsp+208]
		div     rcx
		mov     qword[rsp+224], rax        ; Push variable onto stack
		mov     qword[rsp+232], 7        ; Push variable onto stack
		mov     qword[rsp+240], 3        ; Push variable onto stack
		mov     rdx, 0
		mov     rax, qword[rsp+232]
		mov     rcx, qword[rsp+240]
		div     rcx
		mov     qword[rsp+248], rax        ; Push variable onto stack
		mov     rax, qword[rsp+192]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+200]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+208]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+216]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+224]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+232]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+240]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+248]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp+256], 2        ; Push variable onto stack
		mov     qword[rsp+264], 3        ; Push variable onto stack
		mov     rax, qword[rsp+256]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+264]
		add     rax, rbx
		mov     qword[rsp+272], rax        ; Push variable onto stack
		mov     rax, qword[rsp+0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+56]
		add     rax, rbx
		mov     qword[rsp+280], rax        ; Push variable onto stack
		mov     rax, qword[rsp+280]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+256]
		sub     rax, rbx
		mov     qword[rsp+288], rax        ; Push variable onto stack
		mov     rax, qword[rsp+288]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+256]
		imul    rax, rbx
		mov     qword[rsp+296], rax        ; Push variable onto stack
		mov     qword[rsp+304], -3        ; Push variable onto stack
		mov     qword[rsp+312], -4        ; Push variable onto stack
		mov     rax, qword[rsp+304]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp+312]
		add     rax, rbx
		mov     qword[rsp+320], rax        ; Push variable onto stack
		mov     rax, qword[rsp+320]       ; 64 bit value loading of data values only through rax
		mov     rbx, -2
		sub     rax, rbx
		mov     qword[rsp+328], rax        ; Push variable onto stack
		mov     rax, qword[rsp+256]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+264]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+272]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+280]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+288]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+296]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+304]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+312]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+320]       ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp+328]       ; 64 bit value loading of data values only through rax
		call    printInt

		; All done.
		mov       rax, 60                 ; system call for exit
		xor       rdi, rdi                ; Put an exit code of 0 into the rdi register
		syscall                           ; invoke operating system to exit
