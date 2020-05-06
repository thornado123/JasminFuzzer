import jasminGenerator as JPG


def main():

    program_generator = JPG.JasminGenerator(25)
    out = program_generator.get_program()

    out = [str(x) for x in  out]
    print(out)
    out = "".join(out)
    print(out)
    with open("/Users/thorjakobsen/GIT/jasmin/compiler/tests/jasminFuzzer/test1.jazz", "w") as file:

        file.write(out)

        file.close()

if __name__ == '__main__':
    main()