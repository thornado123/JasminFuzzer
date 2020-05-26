	.text
	.p2align	5
	.globl	_f0
	.globl	f0
_f0:
f0:
	cmpq	$42, %rdi
	jp  	Lf0$1
Lf0$4:
	jne 	Lf0$4
	jmp 	Lf0$2
Lf0$1:
	jp  	Lf0$3
	xorq	$9360, %rax
Lf0$3:
Lf0$2:
	ret 
