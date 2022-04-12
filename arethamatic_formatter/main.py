i = ['3 + 855', '988 + 40']


def arithmetic_arranger(problems, bool=False):
    arranged_problems = ""
    l1 = ""
    l2 = ""
    l3 = ""
    l4 = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for j in problems:
        k = j.split()
        if len(k[0]) > 4 or len(k[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        l1 += " " * 2 + " " * (len(k[2]) - len(k[0]) if len(k[2]) - len(k[0]) > 0 else 0) + k[0]
        l1 += " " * 4
        l2 += k[1] + " " + " " * (len(k[0]) - len(k[2]) if len(k[0]) - len(k[2]) > 0 else 0) + k[2]
        l2 += " " * 4
        l3 += "-" * (len(k[0]) + 2 if len(k[0]) > len(k[2]) else len(k[2]) + 2)
        l3 += " " * 4
        try:
            if k[1] == '+':
                out = int(k[0]) + int(k[2])
            elif k[1] == '-':
                out = int(k[0]) - int(k[2])
            else:
                return "Error: Operator must be \'+\' or \'-\'."
            out = str(out)
            l4 += " " * (2 if len(out) <= max(len(k[0]), len(k[2])) else 1) + out
            l4 += 4 * " "
        except:
            return "Error: Numbers must only contain digits."

    arranged_problems += l1.rstrip() + "\n" + l2.rstrip() + "\n" + l3.rstrip()
    if bool:
        arranged_problems += "\n" + l4.rstrip()

    return arranged_problems


print(arithmetic_arranger(i, True))
