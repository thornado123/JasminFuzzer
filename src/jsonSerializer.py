import os
import json
from jasminTypes import JasminTypes
from jasminNonterminalAndTokens import Nonterminals, Tokens
from jasminScopes import Scopes

#The remaining are for testing purposes
from jasminDistribution import Instructions, Types

def populate_dict(_dict, *enumerators):
    for enumerator in enumerators:
        for elem in enumerator:
            _dict[elem] = elem.name

enum_to_name = {}

populate_dict(enum_to_name, JasminTypes, Nonterminals, Tokens, Scopes)

name_to_enum = {val:key for key,val in enum_to_name.items()}

#print(token_dict)

# Replaces keys in 'dict_to_replace' with the corresponding values from 'dict_replacer'
def replace_recurse(dict_to_replace, dict_replacer):
    new_dict = {}
    for key, value in dict_to_replace.items():
        replaced_key = key
        replaced_value = value

        if isinstance(value, dict):
            replaced_value = replace_recurse(value, dict_replacer)
        if key in dict_replacer:
            replaced_key = dict_replacer[key]

        new_dict[replaced_key] = replaced_value
    return new_dict

def replace_enums_with_names(D):
    return replace_recurse(D, enum_to_name)

def replace_names_with_enums(D):
    return replace_recurse(D, name_to_enum)

dir_path = os.path.dirname(os.path.realpath(__file__))
def obj_to_json(file_name, obj):
    json_data = replace_enums_with_names(obj.__dict__)
    file_name = f'{dir_path}/json/{file_name}'
    with open(file_name, 'w') as FILE:
        json.dump(json_data, FILE, indent = 4)

def json_to_obj(file_name, class_ref, *class_args):
    obj = class_ref(*class_args)
    file_name = f'{dir_path}/json/{file_name}'
    with open(file_name, 'r') as FILE:
        raw_json_dict = json.load(FILE)
        data_dict = replace_names_with_enums(raw_json_dict)
    obj.__dict__ = data_dict
    return obj