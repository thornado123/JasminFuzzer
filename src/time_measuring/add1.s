	.text
	.p2align	5
	.globl	_add1
	.globl	add1
_add1:
add1:
	movq	$0, %rax
	jmp 	Ladd1$1
Ladd1$2:
	movq	$10000000000, %rcx
	addq	%rcx, %rax
Ladd1$1:
	cmpq	%rdi, %rax
	jb  	Ladd1$2
	ret 
