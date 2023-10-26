import sys

def validateCode(code):
    passedopenbrackets = 0
    passedclosedbrackets = 0
    passedopenbracketsarr = []
    passedclosedbracketsarr = []
    validated = True

    for i in range(len(code)):
        if code[i] == "[":
            passedopenbrackets += 1
            passedopenbracketsarr.append(i)
        elif code[i] == "]":
            passedclosedbrackets += 1
            passedclosedbracketsarr.append(i)
    if passedopenbrackets > passedclosedbrackets:
        print("unmatched [")
        validated = False
    elif passedclosedbrackets > passedopenbrackets:
        print("unmatched ]")
        validated = False
    else:
        for i in range(len(passedclosedbracketsarr)):
            if passedopenbracketsarr[i] > passedclosedbracketsarr[i]:
                print("] detected before [")
                validated = False
                break

    return validated

if len(sys.argv) < 2:
    print("Please specify a bf file")
elif not sys.argv[1].endswith(".bf"):
    print("The file given was not a .bf file")
else:
    file = open(sys.argv[1], "r")
    code = file.read()
    validated = validateCode(code)

    acceptedchrs = ["+", "-", "[", "]", ".", ",", ">", "<"]
    for c in code:
        if c not in acceptedchrs:
            code = code.replace(c, "")

    inputindex = 0
    codeindex = 0
    memory = [0 for i in range(30000)]
    memoryindex = 0
    loopindexes = []

    if validated:
        while codeindex < len(code):
            char = code[codeindex]
            match (char):
                case "+": memory[memoryindex] += 1
                case "-": memory[memoryindex] -= 1 if memory[memoryindex] > 0 else 0
                case "[":
                    if memory[memoryindex] == 0:
                        tmpchar = code[codeindex]
                        tempi = codeindex
                        openbrackets = 0
                        while True:
                            if tmpchar == "]" and openbrackets == 0:
                                codeindex = tempi
                                break
                            else:
                                if tmpchar == "]":
                                    openbrackets -= 1
                                    tempi += 1
                                    tmpchar = code[tempi]
                                elif tmpchar == "[" and codeindex != tempi:
                                    openbrackets += 1
                                    tempi += 1
                                    tmpchar = code[tempi]
                                elif tempi != len(code) - 1:
                                    tempi += 1
                                    tmpchar = code[tempi]
                    else:
                        loopindexes.append(codeindex)

                case "]":
                    if memory[memoryindex] == 0:
                        loopindexes.pop()
                    else:
                        codeindex = loopindexes[-1]
                case ".": print(chr(memory[memoryindex]), end="")
                case ",":
                    if inputindex == len(input):
                        memory[memoryindex] = 0
                    else:
                        memory[memoryindex] = ord(input[inputindex])
                        inputindex += 1
                case ">": memoryindex = 0 if memoryindex == 29999 else memoryindex + 1
                case "<": memoryindex = 29999 if memoryindex == 0 else memoryindex - 1
            codeindex += 1
