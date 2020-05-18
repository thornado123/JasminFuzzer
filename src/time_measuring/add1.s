	.text
	.p2align	5
	.globl	_add1
	.globl	add1
_add1:
add1:
	movq	%rdi, %rax
	incq	%rax
	ret 
