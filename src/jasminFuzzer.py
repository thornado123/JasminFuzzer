import jasminGenerator as JPG


def main():

    program_generator = JPG.JasminGenerator(2)
    print(program_generator.get_program())


if __name__ == '__main__':
    main()