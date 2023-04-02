import sys


def get_result_code(code):
    result_code = ""
    count_functions = 0
    functions = []
    for i in code:
        if i:
            if i[0] == "function":
                if len(i) == 3:
                    result_code += f"def {i[1]}({i[2]}):\n"
                else:
                    result_code += f"def {i[1]}({i[2]}, {i[3]}):\n"
                functions.append(i[1])
                count_functions += 1

            elif i[0] == "init":
                for j in range(count_functions):
                    result_code += "\t" * count_functions
                result_code += f"{i[1]} = {i[2]}\n"

            elif i[0] == "add":
                for j in range(count_functions):
                    result_code += "\t" * count_functions
                result_code += f"{i[1]} += {i[2]}\n"

            elif i[0] == "sub":
                for j in range(count_functions):
                    result_code += "\t" * count_functions
                result_code += f"{i[1]} -= {i[2]}\n"

            elif i[0] == "mul":
                for j in range(count_functions):
                    result_code += "\t" * count_functions
                result_code += f"{i[1]} *= {i[2]}\n"

            elif i[0] == "div":
                for j in range(count_functions):
                    result_code += "\t" * count_functions
                result_code += f"{i[1]} /= {i[2]}\n"

            elif i[0] == "return":
                for j in range(count_functions):
                    result_code += "\t" * count_functions
                if count_functions > 0:
                    result_code += f"return {i[1]}\n"
                    count_functions -= 1
                else:
                    result_code += f"print({i[1]})\n"
            elif i[0] in functions:
                result_code += f"{i[1]} = {i[0]}({i[1]})\n"
    return result_code


def solution(f_in, f_out):
    code = f_in.readlines()

    for i in range(len(code)):
        code[i] = code[i].split()

    result_code = get_result_code(code)
    f_out = exec(result_code)


if __name__ == "__main__":
    solution(sys.stdin, sys.stdout)
