import sys
from PIL import Image

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
    filename = sys.argv[1]
    infile = open(filename, "r")
    code = infile.read()

    if validateCode(code):
        translations = {"+": "000", "-": "001", "[": "110", "]": "111",  ".": "101", ",": "100", ">": "010", "<": "011"}
        acceptedchrs = ["+", "-", "[", "]", ".", ",", ">", "<"]
        for c in code:
            if c not in acceptedchrs:
                code = code.replace(c, "")  

        while len(code) % 8 != 0:
            code += "+"

        binary = ""
        while len(code) > 0:
            tmp = code[:8]
            code = code[8:]
            for c in tmp:
                binary += translations[c]

        pixels = [binary[i:i+8] for i in range(0, len(binary), 8)]
        outimage = Image.new(mode="RGB", size=(int(len(pixels)//3), 1))
        pixelmap = outimage.load()
        for i in range(int(len(pixels)//3)):
            pixelmap[i, 0] = (int(pixels[i*3], 2), int(pixels[i*3+1], 2), int(pixels[i*3+2], 2))
            
        outimage.save(filename+".png", format="png")
        outimage.show()