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
fmtflt:	 db		"%g", 10, 0

;-----------------------------
; Code! (execution starts at main)
;-----------------------------
section .text
printInt:
		; We need to call printf, but we are using rax, rbx, and rcx. printf
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
		sub     rsp, 1120               ; Allocate space on the stack

		mov     qword[rsp + 0], 2        ; Push variable onto stack
		mov     rax, qword[rsp + 0]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 0]
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 8], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 8]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 8]
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 16], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 16]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 16]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 8]
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 24], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 24]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 24]
		mov     rcx, qword[rsp + 16]
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 32], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 32]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 8]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 16]
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 40], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 40]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 24]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 0]
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 48], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 48]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, 4
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 56], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 56]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 12
		mov     rcx, 6
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 64], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 64]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 12
		mov     rcx, 6
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 72], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 72]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 4       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 5       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 80], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 80]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 34       ; 64 bit value loading of data values only through rax
		mov     rbx, 45
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 12       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 88], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 88]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 6
		mov     rcx, 5
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 96], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 96]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 2
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 5       ; 64 bit value loading of data values only through rax
		mov     rbx, 5
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		add     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 104], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 104]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 112], 42        ; Push variable onto stack
		mov     rax, qword[rsp + 112]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 120], 42        ; Push variable onto stack
		mov     rax, qword[rsp + 120]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 128], 42        ; Push variable onto stack
		mov     rax, qword[rsp + 128]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 136], 42        ; Push variable onto stack
		mov     rax, qword[rsp + 136]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]
		mov     qword[rsp + 144], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 144]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 144]
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 152], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 152]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 8]
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 160], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 160]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 64]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 72]
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 168], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 168]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 8]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 16]
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 176], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 176]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 144]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 152]
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 184], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 184]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 1234       ; 64 bit value loading of data values only through rax
		mov     rbx, 5678
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 192], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 192]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 100000
		mov     rcx, qword[rsp + 96]
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 200], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 200]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 12       ; 64 bit value loading of data values only through rax
		mov     rbx, 8
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		sub     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 208], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 208]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 8
		mov     rcx, 4
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 5       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 216], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 216]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 1       ; 64 bit value loading of data values only through rax
		mov     rbx, 2
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 224], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 224]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]
		mov     rcx, qword[rsp + 8]
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 16]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 24]
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		add     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 232], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 232]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 240], 1        ; Push variable onto stack
		mov     qword[rsp + 248], 2        ; Push variable onto stack
		mov     qword[rsp + 256], 2        ; Push variable onto stack
		mov     qword[rsp + 264], 3        ; Push variable onto stack
		mov     rax, qword[rsp + 248]
		mov     qword[rsp + 272], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 272]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 248]
		mov     qword[rsp + 280], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 280]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 256]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 264]
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 288], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 288]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 300       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 0]
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 296], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 296]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 288]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 8]
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, 18
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 304], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 304]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 30
		mov     rcx, 2
		cqo
		idiv    rcx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 110       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		sub     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		imul    rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, 9       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 840]
		add     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 848]       ; 64 bit value loading of data values only through rax
		mov     rbx, 8
		imul    rax, rbx
		mov     qword[rsp + 856], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 856]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1000
		add     rax, rbx
		mov     qword[rsp + 864], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 864]
		mov     rcx, 2
		cqo
		idiv    rcx
		mov     qword[rsp + 872], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		imul    rax, rbx
		mov     qword[rsp + 880], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 880]       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		imul    rax, rbx
		mov     qword[rsp + 888], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 888]       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		imul    rax, rbx
		mov     qword[rsp + 896], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 896]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		add     rax, rbx
		mov     qword[rsp + 904], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 904]
		mov     rcx, 2
		cqo
		idiv    rcx
		mov     qword[rsp + 912], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 872]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 912]
		add     rax, rbx
		mov     qword[rsp + 920], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 920]
		mov     qword[rsp + 312], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 312]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 320], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 320]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 8]
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 328], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 328]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 42       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 336], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 336]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 42       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 344], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 344]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 42       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 352], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 352]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 0]       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 360], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 360]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 368], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 368]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 376], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 376]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		sub     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 384], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 384]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		sub     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 392], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 392]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		sub     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 400], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 400]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 408], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 408]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 416], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 416]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 424], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 424]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 432], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 432]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 440], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 440]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 448], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 448]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 832]
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 456], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 456]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, 4
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 840]
		sub     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 848]
		mov     qword[rsp + 464], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 464]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, 4
		sub     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 840]
		sub     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 848]
		mov     qword[rsp + 472], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 472]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, 4       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 840]
		sub     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 848]
		sub     rax, rbx
		mov     qword[rsp + 856], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 856]
		mov     qword[rsp + 480], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 480]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]       ; 64 bit value loading of data values only through rax
		mov     rbx, 2
		sub     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 848]
		sub     rax, rbx
		mov     qword[rsp + 856], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 856]
		sub     rax, rbx
		mov     qword[rsp + 864], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 864]
		mov     qword[rsp + 488], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 488]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]       ; 64 bit value loading of data values only through rax
		mov     rbx, 2
		sub     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 848]
		sub     rax, rbx
		mov     qword[rsp + 856], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 856]
		sub     rax, rbx
		mov     qword[rsp + 864], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 864]
		mov     qword[rsp + 496], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 496]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 11       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 22       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, 33       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, 44       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, 55       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 856], rax     ; Push variable onto stack
		mov     rax, 66       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 864], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 856]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 864]
		sub     rax, rbx
		mov     qword[rsp + 872], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 848]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 872]
		sub     rax, rbx
		mov     qword[rsp + 880], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 880]
		sub     rax, rbx
		mov     qword[rsp + 888], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 888]
		sub     rax, rbx
		mov     qword[rsp + 896], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 896]
		sub     rax, rbx
		mov     qword[rsp + 904], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 904]
		mov     qword[rsp + 504], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 504]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		sub     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 512], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 512]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 3       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 520], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 520]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 84       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 184       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 528], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 528]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 240]       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		sub     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 536], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 536]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 240]       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 544], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 544]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 4       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 552], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 552]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 4       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 560], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 560]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 4       ; 64 bit value loading of data values only through rax
		mov     rbx, -1
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 824]
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 568], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 568]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 4       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     rcx, 2
		cqo
		idiv    rcx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		add     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 576], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 576]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 584], 4        ; Push variable onto stack
		mov     qword[rsp + 592], 3        ; Push variable onto stack
		mov     qword[rsp + 600], 2        ; Push variable onto stack
		mov     qword[rsp + 608], 1        ; Push variable onto stack
		mov     rax, qword[rsp + 584]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 592]
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     rcx, qword[rsp + 600]
		cqo
		idiv    rcx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 608]
		add     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 616], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 616]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 4       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     rcx, 2
		cqo
		idiv    rcx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 608]
		add     rax, rbx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 624], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 624]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, 4
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, 8
		mov     rcx, 2
		cqo
		idiv    rcx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, 7       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 840]
		add     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 848]
		add     rax, rbx
		mov     qword[rsp + 856], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 856]
		mov     qword[rsp + 632], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 632]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, 2       ; 64 bit value loading of data values only through rax
		mov     rbx, 3
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, 4
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 0]
		mov     rcx, 2
		cqo
		idiv    rcx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, 7       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 840]
		add     rax, rbx
		mov     qword[rsp + 848], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]       ; 64 bit value loading of data values only through rax
		mov     rbx, qword[rsp + 848]
		add     rax, rbx
		mov     qword[rsp + 856], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 856]
		mov     qword[rsp + 640], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 640]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 648], 1234        ; Push variable onto stack
		mov     rax, qword[rsp + 648]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 656], 314        ; Push variable onto stack
		mov     rax, qword[rsp + 656]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 664], 1        ; Push variable onto stack
		cmp     qword[rsp + 664], 0      ; Compare value to 0
		jz      if0Done                    ; Skip if statement if 0
		mov     rax, qword[rsp + 664]  ; 64 bit value loading of data values only through rax
		call    printInt
if0Done:                                   ; End of if statement
		mov     qword[rsp + 672], 0        ; Push variable onto stack
		cmp     qword[rsp + 672], 0      ; Compare value to 0
		jz      if1Done                    ; Skip if statement if 0
		mov     rax, qword[rsp + 672]  ; 64 bit value loading of data values only through rax
		call    printInt
if1Done:                                   ; End of if statement
		mov     qword[rsp + 680], 1        ; Push variable onto stack
		cmp     qword[rsp + 680], 0      ; Compare value to 0
		jz      if2Done                    ; Skip if statement if 0
		mov     qword[rsp + 688], 666        ; Push variable onto stack
		mov     rax, qword[rsp + 688]  ; 64 bit value loading of data values only through rax
		call    printInt
if2Done:                                   ; End of if statement
		mov     rax, qword[rsp + 680]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 696], 10        ; Push variable onto stack
while3:                                ; Beginning of while loop
		cmp     qword[rsp + 8], 0      ; Compare value to 0
		jz      while3Done                    ; Skip if statement if 0
		mov     rax, qword[rsp + 8]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 8], rax            ; Push variable onto stack
		jmp    while3                    ; Skip if statement if 0
while3Done:                                   ; End of if statement
		mov     qword[rsp + 704], 4        ; Push variable onto stack
		mov     qword[rsp + 712], 5        ; Push variable onto stack
while4:                                ; Beginning of while loop
		cmp     qword[rsp + 704], 0      ; Compare value to 0
		jz      while4Done                    ; Skip if statement if 0
while5:                                ; Beginning of while loop
		cmp     qword[rsp + 712], 0      ; Compare value to 0
		jz      while5Done                    ; Skip if statement if 0
		mov     rax, qword[rsp + 712]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 712]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 712], rax            ; Push variable onto stack
		jmp    while5                    ; Skip if statement if 0
while5Done:                                   ; End of if statement
		mov     rax, qword[rsp + 704]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     rax, qword[rsp + 704]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 704], rax            ; Push variable onto stack
		jmp    while4                    ; Skip if statement if 0
while4Done:                                   ; End of if statement
		mov     qword[rsp + 704], 3        ; Push variable onto stack
		mov     qword[rsp + 712], 3        ; Push variable onto stack
		mov     qword[rsp + 736], 0        ; Push variable onto stack
while6:                                ; Beginning of while loop
		cmp     qword[rsp + 704], 0      ; Compare value to 0
		jz      while6Done                    ; Skip if statement if 0
		mov     qword[rsp + 712], 3        ; Push variable onto stack
while7:                                ; Beginning of while loop
		cmp     qword[rsp + 712], 0      ; Compare value to 0
		jz      while7Done                    ; Skip if statement if 0
		mov     qword[rsp + 720], 3        ; Push variable onto stack
while8:                                ; Beginning of while loop
		cmp     qword[rsp + 720], 0      ; Compare value to 0
		jz      while8Done                    ; Skip if statement if 0
		mov     qword[rsp + 728], 3        ; Push variable onto stack
while9:                                ; Beginning of while loop
		cmp     qword[rsp + 728], 0      ; Compare value to 0
		jz      while9Done                    ; Skip if statement if 0
		cmp     qword[rsp + 704], 0      ; Compare value to 0
		jz      if10Done                    ; Skip if statement if 0
		mov     rax, qword[rsp + 736]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 736], rax            ; Push variable onto stack
if10Done:                                   ; End of if statement
		mov     rax, qword[rsp + 728]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 728], rax            ; Push variable onto stack
		jmp    while9                    ; Skip if statement if 0
while9Done:                                   ; End of if statement
		mov     rax, qword[rsp + 720]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 720], rax            ; Push variable onto stack
		jmp    while8                    ; Skip if statement if 0
while8Done:                                   ; End of if statement
		mov     rax, qword[rsp + 712]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 712], rax            ; Push variable onto stack
		jmp    while7                    ; Skip if statement if 0
while7Done:                                   ; End of if statement
		mov     rax, qword[rsp + 704]       ; 64 bit value loading of data values only through rax
		mov     rbx, 1
		sub     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 704], rax            ; Push variable onto stack
		jmp    while6                    ; Skip if statement if 0
while6Done:                                   ; End of if statement
		mov     rax, qword[rsp + 736]  ; 64 bit value loading of data values only through rax
		call    printInt

		jmp    myFunctionDone                     ; Skip over function definition
myFunction:                                ; Beginning of function call
		push    rbp                     ; Avoid stack alignment isses
		mov     rbp, rsp
		mov     qword[rsp + 744], 1234        ; Push variable onto stack
		mov     rax, 1234     ; return value stored in rax

		mov     rsp, rbp
		pop     rbp                     ; Avoid stack alignment issues
		ret

myFunctionDone:                                ; End of function call
		mov     qword[rsp + 752], 0        ; Push variable onto stack
		call    myFunction                  ; call function
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 752], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 752]  ; 64 bit value loading of data values only through rax
		call    printInt

		jmp    myAddingFunctionDone                     ; Skip over function definition
myAddingFunction:                                ; Beginning of function call
		push    rbp                     ; Avoid stack alignment isses
		mov     rbp, rsp
		mov     rax, r8       ; 64 bit value loading of data values only through rax
		mov     rbx, r9
		add     rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, r10
		add     rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 792], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 832]     ; return value stored in rax

		mov     rsp, rbp
		pop     rbp                     ; Avoid stack alignment issues
		ret

myAddingFunctionDone:                                ; End of function call
		mov     qword[rsp + 768], 0        ; Push variable onto stack
		mov     qword[rsp + 880], 300        ; Push variable onto stack
		mov     r8, qword[rsp + 880]
		mov     qword[rsp + 888], 200        ; Push variable onto stack
		mov     r9, qword[rsp + 888]
		mov     qword[rsp + 896], 100        ; Push variable onto stack
		mov     r10, qword[rsp + 896]
		call    myAddingFunction                  ; call function
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 768], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 768]  ; 64 bit value loading of data values only through rax
		call    printInt

		jmp    approxCircleAreaDone                     ; Skip over function definition
approxCircleArea:                                ; Beginning of function call
		push    rbp                     ; Avoid stack alignment isses
		mov     rbp, rsp
		mov     qword[rsp + 792], 0        ; Push variable onto stack
		mov     rax, 314       ; 64 bit value loading of data values only through rax
		mov     rbx, r8
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]       ; 64 bit value loading of data values only through rax
		mov     rbx, r8
		imul    rax, rbx
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     rcx, 100
		cqo
		idiv    rcx
		mov     qword[rsp + 840], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 840]
		mov     qword[rsp + 792], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 840]     ; return value stored in rax

		mov     rsp, rbp
		pop     rbp                     ; Avoid stack alignment issues
		ret

approxCircleAreaDone:                                ; End of function call
		mov     qword[rsp + 784], 0        ; Push variable onto stack
		mov     qword[rsp + 880], 50        ; Push variable onto stack
		mov     r8, qword[rsp + 880]
		call    approxCircleArea                  ; call function
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 784], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 784]  ; 64 bit value loading of data values only through rax
		call    printInt

		jmp    cylinderVolumeDone                     ; Skip over function definition
cylinderVolume:                                ; Beginning of function call
		push    rbp                     ; Avoid stack alignment isses
		mov     rbp, rsp
		mov     qword[rsp + 792], 0        ; Push variable onto stack
		mov     rax, r8       ; 64 bit value loading of data values only through rax
		mov     rbx, r9
		imul    rax, rbx
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 792], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 824]     ; return value stored in rax

		mov     rsp, rbp
		pop     rbp                     ; Avoid stack alignment issues
		ret

cylinderVolumeDone:                                ; End of function call
		mov     qword[rsp + 800], 114        ; Push variable onto stack
		mov     qword[rsp + 808], 100        ; Push variable onto stack
		mov     qword[rsp + 816], 0        ; Push variable onto stack
		mov     rax, qword[rsp + 808]
		mov     qword[rsp + 880], rax            ; Push variable onto stack
		mov     r8, qword[rsp + 880]
		mov     rax, qword[rsp + 800]
		mov     qword[rsp + 888], rax            ; Push variable onto stack
		mov     r9, qword[rsp + 888]
		call    cylinderVolume                  ; call function
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 816], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 816]  ; 64 bit value loading of data values only through rax
		call    printInt
		mov     qword[rsp + 880], 33        ; Push variable onto stack
		mov     r8, qword[rsp + 880]
		call    approxCircleArea                  ; call function
		mov     qword[rsp + 824], rax     ; Push variable onto stack
		mov     qword[rsp + 880], 44        ; Push variable onto stack
		mov     r8, qword[rsp + 880]
		mov     rax, qword[rsp + 824]
		mov     qword[rsp + 888], rax            ; Push variable onto stack
		mov     r9, qword[rsp + 888]
		call    cylinderVolume                  ; call function
		mov     qword[rsp + 832], rax     ; Push variable onto stack
		mov     rax, qword[rsp + 832]
		mov     qword[rsp + 816], rax            ; Push variable onto stack
		mov     rax, qword[rsp + 816]  ; 64 bit value loading of data values only through rax
		call    printInt

		; All done.
		mov     rax, 60                 ; system call for exit
		xor     rdi, rdi                ; Put an exit code of 0 into the rdi register
		syscall                         ; invoke operating system to exit
