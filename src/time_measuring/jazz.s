	.text
	.p2align	5
	.globl	_main_jazz
	.globl	main_jazz
_main_jazz:
main_jazz:
	movq	$632, %rax
	cmpq	$42, %rax
	jbe 	Lmain_jazz$1
	addq	$42, %rdi
Lmain_jazz$1:
	movq	%rdi, %rax
	ret 
