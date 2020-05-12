import jasminGenerator as JPG
import jasminPrettyPrint as JPP


def main():

    program_generator = JPG.JasminGenerator(22)
    out = program_generator.get_program()
    out = [str(x) for x in out]
    out = "".join(out)
    out = JPP.jasmin_pretty_print(out)
    print(out)

    with open("/Users/thorjakobsen/GIT/jasmin/compiler/tests/jasminFuzzer/test1.jazz", "w") as file:

        file.write(out)

        file.close()

if __name__ == '__main__':
    main()