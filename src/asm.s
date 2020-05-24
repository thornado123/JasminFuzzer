	.text
	.p2align	5
	.globl	_main_jazz
	.globl	main_jazz
_main_jazz:
main_jazz:
	movq	$0, %rax
	addq	%rax, %rdi
	movq	%rdi, %rax
	ret 
