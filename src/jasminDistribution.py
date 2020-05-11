import numpy as np
from jasminNonterminalAndTokens import Nonterminals as JN
from jasminTypes import JasminTypes as JT
from jasminScopes import Scopes as JS


def draw_from_dist(dist, seed):

    np.random.seed(seed)
    values  = list(dist.keys())
    probs   = list(dist.values())

    val = np.random.choice(np.arange(len(probs)), p=probs)

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
                "reg": 0.33,
                "stack": 0.33,
                "inline": 0.34
            },

            "return" : {

                True : 0.8,
                False: 0.2

            }

        }

    def get_amount_of_decls(self):

        return np.random.randint(low=0, high=10, size=1)[0]

    def get_amount_of_instructions(self):

        return np.random.randint(low=0, high=2, size=1)[0]

    def get_action(self, sub=None, r_depth=0):

        self.seed += 1

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

                "arrayinit" : 0.1,  #Non branching
                "assign"    : 0.15, #Non branching
                "if"        : 0.15,
                "ifelse"    : 0.15,
                "forto"     : 0.15,
                "fordown"   : 0.15,
                "while"     : 0.15
            },

            JN.Peqop: {

                "="     : 0.125,
                "+="    : 0.15,
                "-="    : 0.125,
                "*="    : 0.125,
                ">>="   : 0.125,
                "<<="   : 0.125,
                "^="    : 0.125,
                "&="    : 0.1

            },

            "logic" : {

                "=" : 1
                #"&=": 1 is not a logic assignment

            },

            JN.Plvalue : {

                "_"     : 0.1,
                JN.Var  : 0.6,
                "array" : 0.3

            },

            "while" : {

                True : 0.5,
                False: 0.5,
            }

        }

    def get_action(self, sub=None, r_depth=0):

        self.seed += 1

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

                JT.U8 : 0.05,
                JT.U16: 0.1,
                JT.U32: 0.1,
                JT.U64: 0.6,
                JT.U128: 0.1,
                JT.U256: 0.05

            },

            JN.Ptype : {

                JT.BOOL: 0.3,
                JT.INT: 0.3,
                JN.Utype: 0.3,
                "array": 0.1

            },

            "eval_type" : {

                JT.U8: 0.025,
                JT.U16: 0.05,
                JT.U32: 0.05,
                JT.U64: 0.3,
                JT.U128: 0.05,
                JT.U256: 0.025,
                JT.BOOL: 0.3,
                JT.INT: 0.2
            },

            "assign_type": {

                JT.U8: 0.025,
                JT.U16: 0.05,
                JT.U32: 0.15,
                JT.U64: 0.41,
                JT.U128: 0.05,
                JT.U256: 0.015,
                JT.INT: 0.3
            }

        }

    def get_action(self, sub=None, r_depth=0):

        self.seed += 1

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
            JN.Peop2: 0.0,
            JN.Plvalue: 0.0
        }

        self.sub_actions = {

            JN.Pexpr : {

                "true"  : 0.1,  #Non branching
                "false" : 0.1,  #Non branching
                "int"   : 0.15, #Non branching
                JN.Var   : 0.20, #Non branching
                "array" : 0.15, #<var>[<pexpr>] should deteriorate
                "negvar": 0.1,  #< peop1 > < pexpr > should deteriorate
                "exp"   : 0.2,  # < pexpr > < peop2 > < pexpr > should deteriorate
            },

            JS.Number : {

                "int": 0.4,  # Non branching
                JN.Var: 0.35,  # Non branching
                "array": 0.15,  # <var>[<pexpr>] should deteriorate
                "negvar": 0.1  # < peop1 > < pexpr > should deteriorate

            },

            JN.Peop1: {

                "!" : 0.5,
                "-" : 0.5

            },


            "artemtic" : {
                "+"     : 0.3,
                "-"     : 0.3,
                "*"     : 0.3,
                "^"     : 0.1

            },

            "logic" : {

                "&&": 1 #Logic and?
                #"&": 1

            },

            "compare" : {
                #"<<"    : 0.1,
                #">>"    : 0.15,
                "=="    : 0.2,
                "!="    : 0.2,
                "<"     : 0.15,
                "<="    : 0.15,
                ">"     : 0.15,
                ">="    : 0.15

            }
        }

    def get_action(self, sub=None, scope=None, r_depth=0):

        self.seed += 1

        if sub is not None:

            if scope == JS.Number:

                return draw_from_dist(self.sub_actions[JS.Number], self.seed)

            else:

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
            JN.Pfundef  : 0.4,
            JN.Param    : 0.1,
            JN.Pglobal  : 0.24
        }

        self.sub_actions = {

            JN.Module : {
                JN.Top : 0.5,
                "error" : 0.5,
            },

            JN.Top : {
                JN.Pfundef:   0.75,
                JN.Param  :    0.07,
                JN.Pglobal:   0.18
            },

            JN.Call_conv : {
                "export" : 1,
                "inline" : 0
            }

        }

    def get_action(self, sub=None, r_depth=0):

        self.seed += 1

        if sub is not None:

            return draw_from_dist(self.sub_actions[sub], self.seed)

        else:

            return draw_from_dist(self.actions, self.seed)
