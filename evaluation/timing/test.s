	.text
	.p2align	5
	.globl	_f0
	.globl	f0
_f0:
f0:
	cmpq	$43, %rdi
	jb  	Lf0$1
	movq	$1, %rax
	jmp 	Lf0$2
Lf0$1:
	incq	%rdi
	cmpq	$43, %rdi
	jnb 	Lf0$3
	movq	$2, %rax
	jmp 	Lf0$4
Lf0$3:
Lf0$5:
	incq	%rax
	jmp 	Lf0$5
Lf0$4:
Lf0$2:
	ret 
