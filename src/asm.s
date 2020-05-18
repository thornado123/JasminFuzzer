	.text
	.p2align	5
	.globl	_f0
	.globl	f0
_f0:
f0:
	cmpq	$42, %rdi
	jne 	Lf0$1
	jnp 	Lf0$2
	jp  	Lf0$3
Lf0$3:
Lf0$2:
Lf0$1:
	movq	%rdi, %rax
	ret 
