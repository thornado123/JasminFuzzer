import enum


class Scopes(enum.Enum):

    Function_name   = "func"
    Variables       = "dfunc"
    Decl            = "decl"
    Arrays          = "arrays"

    """
        
        Expression evaluation
    
    """
    Number       = "number"
    Bool         = "bool"