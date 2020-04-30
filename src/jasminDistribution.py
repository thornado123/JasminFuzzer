import numpy as np
from jasminNonterminalAndTokens import Nonterminals as JN


def draw_from_dist(dist, seed):

    np.random.seed(seed)
    values  = list(dist.keys())
    probs   = list(dist.values())


    #print(probs)
    #print(values)

    val = np.random.choice(np.arange(len(probs)), p=probs)
    #print(np.arange(len(probs)))
    #print(val)

    return values[val]


class Functions:

    def __init__(self, seed):
        self.seed = seed
        self.actions = {
            JN.Pfundef : 0.5,
            JN.Storage : 0.1,
            JN.Stor_type: 0.1,
            JN.Pvardecl: 0.3
        }

        self.sub_actions = {

            JN.Storage : {
                "reg": 0.8,
                "stack": 0.1,
                "inline": 0.1
            }

        }

    def get_action(self, sub=None):

        if sub is not None:

            return draw_from_dist(self.sub_actions[sub], self.seed)

        else:

            return draw_from_dist(self.actions, self.seed)


class Instructions:

    def __init__(self, seed):
        self.seed = seed
        self.actions = {
            JN.Pinstr : 1,
            JN.Pblock : 0,
            JN.Peqop  : 0,
            JN.Plvalue: 0
        }

        self.sub_actions = {

            JN.Pinstr : {

                "arrayinit" : 0.1,  # ARRAYINIT ⟨parens⟨var⟩⟩ ;
                "if"        : 0.1,
                "ifelse"    : 0.1,
                #"forto"     : 0.1,
                #"fordown"   : 0.1,
                "while"     : 0.7
            },

            JN.Peqop: {

                "="     : 0.125,
                "+="    : 0.125,
                "-="    : 0.125,
                "*="    : 0.125,
                ">>="   : 0.125,
                "<<="   : 0.125,
                "&="    : 0.125,
                "^="    : 0.125

            },

            JN.Plvalue : {

                "_"     : 0.2,
                "var"   : 0.5,
                "array" : 0.3

            }

        }



    def get_action(self, sub=None):

        if sub is not None:

            return draw_from_dist(self.sub_actions[sub], self.seed)

        else:

            return draw_from_dist(self.actions, self.seed)


class Types:

    def __init__(self, seed):
        self.seed = seed
        self.actions = {
            JN.Ptype : 0.5,
            JN.Utype : 0.5
        }

        self.sub_actions = {

            JN.Utype : {

                "u8" : 0.05,
                "u16": 0.1,
                "u32": 0.2,
                "u64": 0.5,
                "u128": 0.1,
                "u256": 0.05

            },

            JN.Ptype : {

                "bool": 0.1,
                "int" : 0.1,
                JN.Utype: 0.5,
                "array": 0.3

            }

        }



    def get_action(self, sub=None):

        if sub is not None:

            return draw_from_dist(self.sub_actions[sub], self.seed)

        else:

            return draw_from_dist(self.actions, self.seed)


class Expressions:

    def __init__(self, seed):
        self.seed = seed
        self.actions = {
            JN.Pexpr: 1.0,
            JN.Ident: 0.0,
            JN.Var  : 0.0,
            JN.Prim : 0.0,
            JN.Peop1: 0.0,
            JN.Peop2: 0.0
        }


        self.sub_actions = {

            JN.Pexpr : {

                "true"  : 0.05,  # TRUE
                "false" : 0.05,  # FALSE
                "int"   : 0.05,  # INT
                "var"   : 0.25,  # var
                "array" : 0.1,  # <var>[<pexpr>]
                "negvar": 0.1,  # < peop1 > < pexpr >
                "exp"   : 0.4,  # < pexpr > < peop2 > < pexpr >
            },

            JN.Peop1: {

                "!" : 0.5,
                "-" : 0.5

            },

            JN.Peop2: {

                "+"     : 0.2,
                "-"     : 0.2,
                "*"     : 0.1,
                "&&"    : 0.05,
                "&"     : 0.05,
                "^"     : 0.02,
                "<<"    : 0.04,
                ">>"    : 0.04,
                "=="    : 0.05,
                "!="    : 0.05,
                "<"     : 0.05,
                "<="    : 0.05,
                ">"     : 0.05,
                ">="    : 0.05
            }

        }

    def get_action(self, sub=None):

        if sub is not None:

            return draw_from_dist(self.sub_actions[sub], self.seed)

        else:

            return draw_from_dist(self.actions, self.seed)


class GlobalDeclarations:

    def __init__(self, seed):
        self.seed = seed
        self.actions = {
            JN.Module   : 0.01,
            JN.Top      : 0.25,
            JN.Call_conv: 0.0,
            JN.Pfundef  : 0.5,
            JN.Param    : 0.1,
            JN.Pglobal  : 0.14
        }

        self.sub_actions = {

            JN.Module : {
                "top" : 0.5,
                "error" : 0.5,
            },

            JN.Top : {
                "pfundef":   0.75,
                "pparam":    0.07,
                "pglobal":   0.18
            },

            JN.Call_conv : {
                "export" : 0.2,
                "inline" : 0.8
            }

        }

    def get_action(self, sub=None):

        if sub is not None:

            return draw_from_dist(self.sub_actions[sub], self.seed)

        else:

            return draw_from_dist(self.actions, self.seed)




