import numpy as np


def draw_from_dist(dist, seed):

    np.random.seed(seed)
    values  = list(dist.keys())
    probs   = list(dist.values())

    return values[np.random.choice(np.arange(len(probs)), p=probs)]


class Functions:

    def __init__(self, seed):
        self.seed = seed
        self.actions = {
            "pfunbody" : 0.5,
            "storage"  : 0.1,
            "stor_type": 0.1,
            "pvardecl" : 0.3
        }

        self.sub_actions = {

            "storage" : {
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
            "pinstr" : 1,
            "pblock" : 0,
            "peqop"  : 0,
            "plvalue": 0
        }

        self.sub_actions = {

            "pinstr" : {

                "arrayinit" : 0.1,  # ARRAYINIT ⟨parens⟨var⟩⟩ ;
                "if"        : 0.2,
                "ifelse"    : 0.2,
                #"forto"     : 0.1,
                #"fordown"   : 0.1,
                "while"     : 0.5
            },

            "peqop" : {

                "="     : 0.125,
                "+="    : 0.125,
                "-="    : 0.125,
                "*="    : 0.125,
                ">>="   : 0.125,
                "<<="   : 0.125,
                "&="    : 0.125,
                "^="    : 0.125

            },

            "plvalue" : {

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
            "ptype" : 0.5,
            "utype" : 0.5
        }

        self.sub_actions = {

            "utype" : {

                "u8" : 0.05,
                "u16": 0.1,
                "u32": 0.2,
                "u64": 0.5,
                "u128": 0.1,
                "u256": 0.05

            },

            "ptype" : {

                "bool": 0.2,
                "int" : 0.2,
                "utype": 0.4,
                "array": 0.2

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
            "pexpr" : 1.0,
            "ident" : 0.0,
            "var"   : 0.0,
            "prim"  : 0.0,
            "peop1" : 0.0,
            "peop2" : 0.0
        }


        self.sub_actions = {

            "pexpr" : {

                "true"  : 0.09,  # TRUE
                "false" : 0.09,  # FALSE
                "int"   : 0.08,  # INT
                "var"   : 0.2,  # var
                "array" : 0.18,  # <var>[<pexpr>]
                "negvar": 0.12,  # < peop1 > < pexpr >
                "exp"   : 0.24,  # < pexpr > < peop2 > < pexpr >
            },

            "peop1" : {

                "!" : 0.5,
                "-" : 0.5

            },

            "peop2" : {

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
            "module"    : 0.01,
            "top"       : 0.25,
            "call_conv" : 0.0,
            "pfundef"   : 0.5,
            "pparam"    : 0.1,
            "pglobal"   : 0.14
        }

        self.sub_actions = {

            "module" : {
                "top" : 0.5,
                "error" : 0.5,
            },

            "top" : {
                "pfundef":   0.75,
                "pparam":    0.07,
                "pglobal":   0.18
            },

            "call_conv" : {
                "export" : 0.2,
                "inline" : 0.8
            }

        }

    def get_action(self, sub=None):

        if sub is not None:

            return draw_from_dist(self.sub_actions[sub], self.seed)

        else:

            return draw_from_dist(self.actions, self.seed)




