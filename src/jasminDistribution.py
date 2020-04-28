import numpy as np


def draw_from_dist(dist, seed):

    np.random.seed(seed)
    values  = list(dist.keys())
    probs   = list(dist.values())

    return values[np.random.choice(np.arange(len(probs)), p=probs)]


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

            }

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




