import jasminGenerator as JPG
import jasminPrettyPrint as JPP
import subprocess
#import pandas as pd

def main():

    #result_outputs = pd.DataFrame(columns=["Seed", "Errors"])
    pandas_index  = 0
    source_path   = "/Users/thorjakobsen/GIT/jasmin/compiler/tests/jasminFuzzer/test.jazz"
    compiler_path = "/Users/thorjakobsen/GIT/jasmin/compiler/./jasminc"

    for i in range(0, 100):

        program_generator = JPG.JasminGenerator(i)
        out = program_generator.get_program()

        out = [str(x) for x in out]
        out = "".join(out)
        out = JPP.jasmin_pretty_print(out)

        with open("/Users/thorjakobsen/GIT/jasmin/compiler/tests/jasminFuzzer/test.jazz", "w") as file:
            file.write(out)
            file.close()

            process = subprocess.Popen([compiler_path, source_path, "-o", "test"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            _, stderr = process.communicate()
            result = stderr.decode("utf-8")
            if result != "":
                print(i, result)
                #result_outputs.loc[pandas_index] = [i, result]
                pandas_index += 1

    #result_outputs.to_csv("/Users/thorjakobsen/GIT/JasminFuzzer/results.csv")

if __name__ == '__main__':
    main()