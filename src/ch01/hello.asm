section .data
    hello db 'Hello, eBPF!',0

section .text
    global _start

_start:
    ; write Hello, eBPF! to stdout
    mov eax, 4          ; syscall number for sys_write
    mov ebx, 1          ; file descriptor 1 is stdout
    mov ecx, hello      ; pointer to the message
    mov edx, 13         ; length of the message
    int 0x80            ; call kernel

    ; exit the program
    mov eax, 1          ; syscall number for sys_exit
    xor ebx, ebx        ; exit code 0
    int 0x80            ; call kernel
