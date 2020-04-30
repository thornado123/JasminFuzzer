import jasminGenerator as JPG


def main():

    program_generator = JPG.JasminGenerator(2343)
    print(program_generator.get_program())


if __name__ == '__main__':
    main()