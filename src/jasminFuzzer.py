import jasminGenerator as JPG


def main():

    program_generator = JPG.JasminGenerator(1)
    out = program_generator.get_program()

    with open("/Users/thorjakobsen/GIT/jasmin/compiler/tests/jasminFuzzer/test1.jazz", "w") as file:

        file.write(out)

        file.close()

    print(out)


if __name__ == '__main__':
    main()