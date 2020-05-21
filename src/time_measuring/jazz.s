	.text
	.p2align	5
	.globl	_main_jazz
	.globl	main_jazz
_main_jazz:
main_jazz:
	movw	$172, %ax
	cmpw	$42, %ax
	jbe 	Lmain_jazz$1
	addq	$42, %rdi
Lmain_jazz$1:
	movq	%rdi, %rax
	ret 
