import enum


class Nonterminals(enum.Enum):

    """

        TYPES

    """

    Ptype = "ptype"
    Utype = "utype"

    """
            
        EXPRESSIONS    
    
    """

    Pexpr   = "pexpr"
    Ident   = "ident"
    Prim    = "prim"
    Peop1   = "peop1"
    Peop2   = "peop2"
    Var     = "var"

    """
    
        INSTRUCTIONS
    
    """

    Pinstr  = "pinstr"
    Pblock  = "pblock"
    Peqop   = "peqop"
    Plvalue = "plvalue"

    """
    
        FUNCTIONS
    
    """

    Pfunbody    = "pfunbody"
    Storage     = "storage"
    Stor_type   = "stor_type"
    Pvardecl    = "pvardecl"

    """
    
        GLOBAL DECLARATIONS
    
    """

    Module      = "module"
    Top         = "top"
    Call_conv   = "call_conv"
    Pfundef     = "pfundef"
    Param       = "param"
    Pglobal     = "pglobal"


class Tokens(enum.Enum):

    If      = "if"
    Else    = "else"
    For     = "for"
    While   = "while"
    To      = "to"