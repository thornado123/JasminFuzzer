"""

    The Jasmin program generator is a deterministic Jasmin source program generator
    that take a seed token and generates a program with offset in this token.


    Methods:

        __init__:

            - set the current seed value

        getProgram:

            - given a seed value return a valid Jasmin program


    Jasmin BNF:

    TYPES:

    <ptype>     ::= T_BOOL | T_INT | <utype> | <utype><brackets <pexpr>>
    <utype>     ::= T_U8 | T_U16 | T_U32 | T_U64 | T_U128 | T_U256


    EXPRESSIONS:

    <pexpr>     ::= <var> | <var><brackets<pexpr>> | TRUE | FALSE | INT | [<parens<ptype>>]<brackets(<var>+<pexpr>)>
                | <peop1><pexpr> | <pexpr><peop2><pexpr> | <parens<pexpr>> | <var><parens_tuple<pexpr>>
                | <prim><parens_tuple<pexpr>>

    <ident>     ::= NID
    <var>       ::= <ident>
    <prim>      ::= #<ident>

    <peop1>     ::= ! | -
    <peop2>     ::= + | - | * | && | PIPEPIPE | & | PIPE | ^ | << | >> | >>s | == | != | < | <= | > | >= | <s | <=s | >s
                | >=s

    INSTRUCTIONS:

    <pinstr>    ::= ARRAYINIT ⟨parens⟨var⟩⟩ ;
                | ⟨tuple1⟨plvalue⟩⟩ ⟨peqop⟩ ⟨pexpr⟩ [IF ⟨pexpr⟩] ; | ⟨var⟩ ⟨parens_tuple⟨pexpr⟩⟩ ;
                | IF ⟨pexpr⟩ ⟨pblock⟩
                | IF ⟨pexpr⟩ ⟨pblock⟩ ELSE ⟨pblock⟩
                | FOR ⟨var⟩ = ⟨pexpr⟩ TO ⟨pexpr⟩ ⟨pblock⟩
                | FOR ⟨var⟩ = ⟨pexpr⟩ DOWNTO ⟨pexpr⟩ ⟨pblock⟩ | WHILE [⟨pblock⟩] ⟨parens⟨pexpr⟩⟩ [⟨pblock⟩]

    <pblock>    ::= ⟨braces⟨pinstr⟩*⟩

    <peqop>     ::= =
                | += | -= | *=
                | >>= |>>s= |<<=
                | &= |^= | PIPEEQ

    <plvalue>   ::= UNDERSCORE | <var> | <var> <brackets<pexpr>> | [<parens<ptype>>]<brackets(<var> + <pexpr>)>

    FUNCTIONS:

    <pfunbody>  ::= LBRACE (⟨pvardecl⟩ ;)∗ ⟨pinstr⟩∗ [RETURN ⟨tuple⟨var⟩⟩ ;] RBRACE

    <storage>   ::= REG | STACK | INLINE

    <stor_type> ::= <storage><ptype>
    <pvardecl>  ::= <stor_type><var>


    GLOBAL DECLARATIONS:

    <module>    ::= <top> * EOF | error
    <top>       ::= <pfundef> | <pparam> | <pglobal>
    <call_conv> ::= EXPORT | INLINE
    <pfundef>   ::= [<call_conv>]FN <ident> <parens_tuple(<stor_type><var>)>[-><tuple<stor_type>>]<pfunbody>
    <pparam>    ::= PARAM <ptype><ident> = <pexpr>;
    <pglobal>   ::= <ident> = <pexpr>;

"""

# Standin

def action_prop(seed):

    return "jell"


class jasmingenerator:

    def __init__(self, program_seed):

        seed = program_seed

    def getProgram(self):

        return "jasmin program"

    def global_declarations(self, action=None):

        if action is None:

            action = action_prop(self.seed, "global")

        if action == "module":

            if action_prop(self.seed, "module"):

                return self.global_declarations("top")+" * EOF"

            else:

                return  "error"

        if action == "top":

            action = action_prop("top")

            if action == "pfundef":

                return self.global_declarations("pfundef")

            if action == "pparam":

                return self.global_declarations("pparam")

            if action == "pglobal":

                return self.global_declarations("pglobal")

        if action == "call_conv"

            action = action_prop(self.seed, "call_conv")

            if action:

                return "export"

            else:

                return "inline"

        if action == "pfundef":

            return  self.global_declarations(action="call_conv") + "fn" + self.expressions(action="ident") + \
                    "(" + self.functions(action="stor_type") \
                    + self.expressions(action="var") + ") -> (" \
                    + self.functions(action="stor_type") + ")" \
                    + self.functions(action="pfunbody")


        if action == "pparam":

            return "param" + self.types(action="ptype") + self.expressions(action="ident") + " = " + self.expressions(action="pexpr")

        if action == "pglobal":

            return self.expressions(action="ident") + " = " + self.expressions(action="pexpr")

    def expressions(self, action=None):

        return "expression"

    def functions(self, action=None):

        return "function"

    def types(self, action=None):

        return "type"










