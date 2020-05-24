import jasminGenerator as JPG
import jasminPrettyPrint as JPP
import subprocess
import sys
import pandas as pd
import time


def error_analyzer(error_line):

    if "compilation error" in error_line:

        result = "compilation error "
        x = error_line.split(":")

        for i in range(1, len(x)):

            result += x[i]

    elif "WARNING" in error_line:

        prefix = "WARNING"

        if "," in error_line:

            result = prefix + error_line.split(",")[1]

        else:

            result = error_line

    elif "typing error" in error_line:

        return "typing error"

    elif "the variable is already allocated" in error_line:

        return "the variable is already allocated"

    elif "Register allocation" in error_line:

        result = "Register allocation error"

    elif error_line.startswith("("):

        return "CON"

    elif error_line == "PLEASE REPORT":

        return "PR"

    else:

        result = error_line

    return result


def main():

    result_outputs = pd.DataFrame(columns=["Seed", "Errors", "Size", "Safe", "GenerationTime", "SafetyCheckTime"])
    pandas_index  = 0
    source_path   = "/Users/thorjakobsen/GIT/jasmin/compiler/tests/jasminFuzzer/test"
    compiler_path = "/Users/thorjakobsen/GIT/jasmin/compiler/./jasminc"

    """
        if os.path.exists("/Users/thorjakobsen/GIT/JasminFuzzer/evaluation/error_code.p"):
    
            resulting_errors = pickle.load(open("/Users/thorjakobsen/GIT/JasminFuzzer/evaluation/error_code.p", "rb" ) )
            print("LOADED EXISTING ERROR CODES")
    
        else:
    
            print("MAKING NEW ERROR CODE LIST")
            resulting_errors = []
    """

    if len(sys.argv) == 2:

        print("ONLY GOT 1 Running dry run saving the target")


        program_generator = JPG.JasminGenerator(int(sys.argv[1]))
        out = program_generator.get_program()

        out = [str(x) for x in out]
        out = "".join(out)
        out = JPP.jasmin_pretty_print(out)

        with open(source_path + sys.argv[1] + ".jazz", "w") as file:
            file.write(out)
            file.close()

        print(out)

        process = subprocess.Popen([compiler_path, source_path + sys.argv[1] + ".jazz", "-o", "test"],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        _, stderr = process.communicate()
        result = stderr.decode("utf-8")

        print("RESULT:\n", result)

    else:

        start = int(sys.argv[1])
        end   = int(sys.argv[2])

        for i in range(start, end):

            gen_time = time.time()

            program_generator = JPG.JasminGenerator(i)
            out = program_generator.get_program()

            out = [str(x) for x in out]
            out = "".join(out)
            out = JPP.jasmin_pretty_print(out)

            gen_time = time.time() - gen_time

            size_of_program = len(out.encode('utf-8'))

            with open(source_path + ".jazz", "w") as file:
                file.write(out)
                file.close()

            process = subprocess.Popen([compiler_path, source_path + ".jazz","-o", "asm.s"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            _, stderr = process.communicate()
            result = stderr.decode("utf-8")

            error_codes = [[],[]]

            if result != "":

                lines = result.splitlines()

                for line in lines:
                    error_codes[0].append(line)

            safety_check_time = time.time()

            process = subprocess.Popen([compiler_path, source_path + ".jazz", "-checksafety"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            _, stderr = process.communicate()
            result = stderr.decode("utf-8")

            safety_check_time = time.time() - safety_check_time

            for line in result.splitlines():
                if "Fatal" in line or "WARNING" in line or "error" in line.lower():
                    error_codes[1].append(line)

            safe = "Program is not safe!" not in result

            result_outputs.loc[pandas_index] = [i, error_codes, size_of_program, safe, gen_time, safety_check_time]
            pandas_index += 1

        #pickle.dump(resulting_errors, open("/Users/thorjakobsen/GIT/JasminFuzzer/evaluation/error_code.p", "wb"))
        result_outputs.to_csv("/Users/thorjakobsen/GIT/JasminFuzzer/evaluation/data/results_" + str(start) + "_" + str(end) + ".csv")


if __name__ == '__main__':
    main()