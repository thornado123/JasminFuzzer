import jasminGenerator as JPG
import jasminPrettyPrint as JPP


def main():
    out = ""

    for i in range(0, 100):

        program_generator = JPG.JasminGenerator(i)
        out = program_generator.get_program()
        out = [str(x) for x in out]
        out = "".join(out)
        out = JPP.jasmin_pretty_print(out)
        print(out)

        with open("/Users/thorjakobsen/GIT/jasmin/compiler/tests/jasminFuzzer/test" + str(i) + ".jazz", "w") as file:
            file.write(out)
            file.close()


if __name__ == '__main__':
    main()