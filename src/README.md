# Implementation nodes

In the following any shortcomings or bugs in the implementation should be noted
All the bugs or limiting behaviour should be documented such that it can be 
added to the report.

## Expressions

1. Signed operations: Has been left out of the initial code (and maybe for good).
2. Direct memory access: Has been left out of the initial. BNF: [ < parens < ptype >>] < brackets( < var > + < pexpr >) >
3. Parens expression: left out BNF < pexpr > < peop2 > < pexpr >
4. Assembly operations: left out BNF < prim > < parens_tuple < pexpr >>
5. Some tuple function: < var > < parens_tuple < pexpr >> 
6. Primitives: left out <prim> ::= # <ident>
7. ident merged with var as its only used by var and prim 


## Instructions

1. Some tuple if def left out BNF: ⟨tuple1⟨plvalue⟩⟩ ⟨peqop⟩ ⟨pexpr⟩ [IF ⟨pexpr⟩] ;
2. More tuple stuff BNF: ⟨var⟩ ⟨parens_tuple⟨pexpr⟩⟩ ;
3. Signed operators and pipeq has ben left out
4. Mem access left out BNF [<parens<ptype>>]<brackets(<var> + <pexpr>)>

# Achieving complex program

To achieve more complex programs that use more complex tokens but without entering a recursive non terminating loop
the probabilities of the more complex tokens should be decay with respect to the depth of the current scope. 
While the terminating/final token's probabilities should grow.
