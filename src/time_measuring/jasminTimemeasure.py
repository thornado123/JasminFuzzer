import subprocess


"""

    Program todo:
    
    1) Read a jasmin program and get its export function name (main or f0)
    2) Compile the jasmin file into test.s
    3) Change the name in the main.c file
    4) Compile the main.c file with the test.s file as input into test
    5) Run the ./test and read outputs 
    6) Save these outputs to a file on disk (pandas)

"""


class JasminTimeMeasurer:

    def __init__(self, jasmin_file, main_c_file):

        self.jasmin_file = jasmin_file
        self.jasmin_func_name = None
        self.main_c_file = main_c_file

    def get_jasmin_func_name(self):

        with open(self.jasmin_file, "r") as jazz_file:

            function_name = ""
            export_name = True

            while(export_name):

                new_line = jazz_file.readline()

                if "export" in new_line:

                    function_name = new_line.split("fn ")[1].split("(")[0]
                    export_name = False
            jazz_file.close()

        function_name.replace(" ", "")
        self.jasmin_func_name = function_name

    def change_name_in_main(self):

        with open(self.main_c_file, "wr") as c_file:
            new_file_content = ""

            for line in c_file:
                stripped_line = line.strip()

                if "extern uint64_t " in line:
                    old_func_name = line.split("uint64_t")[1].split("(")[0]
                    old_func_name.replace(" ", "")
                    stripped_line.replace(old_func_name, self.jasmin_func_name)

                new_file_content += stripped_line + "\n"
                
            c_file.close()


            writing_file = open("sample.txt", "w")
            writing_file.write(new_file_content)
            writing_file.close()


def main():

    jasmin_t = JasminTimeMeasurer("add1.jazz")
    jasmin_t.get_jasmin_func_name()

    print(jasmin_t.jasmin_func_name)

if __name__ == '__main__':
    main()