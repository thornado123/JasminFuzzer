import os
import jasminPrettyPrint as JPP
import jasminGenerator as JPG
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
target_folder = f"{DIR_PATH}/../evaluation/generated_data/NonterminatingPrograms"
jasminc = "/Users/josefgharib/Desktop/jasmin/compiler./jasminc"
non_terminating_seeds = [30068, 31542, 33216, 33770, 34620, 35353, 35625, 35951, 39907, 44706, 44964, 45240, 45676]

for prog_seed in non_terminating_seeds:
    FILE = f"{target_folder}/{prog_seed}.jazz"
    program_generator = JPG.JasminGenerator(prog_seed)
    out = program_generator.get_program()

    out = [str(x) for x in out]
    out = "".join(out)
    out = JPP.jasmin_pretty_print(out)
    with open(FILE ,'w') as f:
        f.write(out)