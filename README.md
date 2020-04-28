# JasminFuzzer
Fuzzer for the jasmin compiler.

This repository is a fuzzer for the Jasmin compiler for detecting unintended behaviour. 

## Introduction

The Jasmin framework consists of the Jasmin language and a compiler which compiles a Jasmin source to assembly.
The framework is targeted implementation of cryptographic algorithms and security essential parts of applications.
The Jasmin language makes it easy to verify cryptographic constant time and memory safety. The compilers correctness is formally proven using Coq.


### Compiler introduction

The compiler uses the programmers annotations to verify cryptographic constant time and memory safety. After this has passed it 
compiles the Jasmin source to assembly.

## Fuzzing the Jasmin compiler

In a fuzzer perspective the compiler consists of two different fuzzable parts which will be described in the following:

### 1) The Jasmin to assembly compiler

This part of the compiler's correctness is verified and written in Coq. The purpose of this is to translate the Jasmin source to a assembly target. The correctness is defined as follows: A execution of a target program should correspond to the execution of the source program.

This part of the compiler can be fuzzed with well formed Jasmin source programs which should try to reach all the areas of the compiler. As there currently do not exist any other Jasmin compilers it is not possible to do differential testing where we check for miscompliation. 
It might be possible to do metamorphic testing but it is still to early to say if generating of such programs is possible. 
So far we start out by checking if it is possible to break the compiler on correct input, we demand that it is well formed to get past the parser.   

### 2) The C. Constant time and memory safe verifier 

This part of the compiler can be tested using the annotations of the Jasmin programs. These has to be well formed as well where here the annotations are the variables that can be adjusted with the rest of the program. We will test this part if there is time.

## Interesting papers

https://eprint.iacr.org/2019/1155.pdf
https://blackboard.au.dk/bbcswebdav/pid-2535790-dt-content-rid-8052926_1/courses/BB-Cou-UUVA-89108/BB-Cou-UUVA-
89108_ImportedContent_20200129103750/Group10.pdf
https://arxiv.org/pdf/1904.04606.pdf
https://arxiv.org/pdf/1902.09334.pdf
https://rjlipton.wordpress.com/2019/11/19/a-clever-way-to-find-compiler-bugs/#comment-106348
https://blog.regehr.org/archives/1700
https://srg.doc.ic.ac.uk/files/papers/compilerbugs-oopsla-19.pdf
https://i.blackhat.com/asia-19/Fri-March-29/bh-asia-Dominiak-Efficient-Approach-to-Fuzzing-Interpreters-wp.pdf
https://eprint.iacr.org/2019/1155.pdf
https://vincentlaporte.info/CCS2017_Jasmin+presentation.pdf
https://www.fuzzingbook.org/html/Fuzzer.html
https://github.com/rohanpadhye/jqf/wiki/Fuzzing-a-Compiler
https://srg.doc.ic.ac.uk/files/papers/compilerbugs-oopsla-19.pdf
web.engr.oregonstate.edu/~wongwe/papers/pdf/pldi13.pdf
https://www.phoronix.com/scan.php?page=news_item&px=Prog-Fuzz-Compiler-Fuzzing
http://fm.csl.sri.com/SSFT19/gregoir-slides2.pdf
