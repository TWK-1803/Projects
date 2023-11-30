def check(lst):
    if len(lst) == 4:
        a, b, c, d = lst
        return firstCheck(a, b, c, d)
    else:
        return False

def firstCheck(a, b, c, d):
    return any([fCheck(a, b, c, d), fCheck(b, c, d, a), fCheck(c, d, a, b), fCheck(d, a, b, c), fCheck(d, b, a, c), fCheck(a, c, b, d)])

def fCheck(a, b, c, d):
    return any(secondCheck(a, b, x) for x in op(c, d))

def finalCheck(a, b):
    s = op(a, b)
    if 24 in s or 4 in s:
        print(a, b, op(a,b))
        return True
    else:
        return False
    
def sCheck(a, b, c):
    print(a,b,c)
    return any(finalCheck(a, x) for x in op(b, c))

def secondCheck(a, b, c):
    return sCheck(a, b, c) or sCheck(b, a, c) or sCheck(c, a, b)

def opp(a, b):
    if a == 0:
        return [0, 1, b, -b, 1 + b, b - 1, 1 - b]
    elif a == 1:
        return [1 + b, b, 1 / b, 1 - b, b - 1, 1]
    else:
        if b == 0:
            return [a + b, a * b, float("inf"), a - b, b - a, b / a, 1, 0]
        else:
            return [a + b, a * b, a / b, a - b, b - a, b / a]#, a**b, b**a]

def op(a, b):
    if a == 3:
        return opp(min(3, b), max(3, b)) + op(b, 6) + op(6, b)
    elif a == 4:
        return opp(min(4, b), max(4, b)) + op(b, 24)
    elif a == 5:
        return opp(min(5, b), max(5, b)) + op(b, 120)
    elif a == 6:
        return opp(min(6, b), max(6, b)) + op(b, 720)
    elif a == 7:
        return opp(min(7, b), max(7, b)) + op(b, 5040)
    elif a == 8:
        return opp(min(8, b), max(8, b)) + op(b, 40320)
    elif a == 9:
        return opp(min(9, b), max(9, b)) + op(b, 362880)
    elif a == 10:
        return opp(min(10, b), max(10, b)) + op(b, 3628800)
    elif a == 11:
        return opp(min(11, b), max(11, b)) + op(b, 39916800)
    elif a == 12:
        return opp(min(12, b), max(12, b)) + op(b, 479001600)
    elif a == 13:
        return opp(min(13, b), max(13, b)) + op(b, 6227020800)
    else:
        return opp(min(a, b), max(a, b))

def lcheck(s):
    if len(s) == 4:
        return [check(s)]
    else:
        return list(map(lambda n: all(lcheck([n] + s)), range(s[0], 13)))

def ccheck(lst):
    return all(lcheck(lst))

with open("test.txt", "w") as file:
    for i in range(1, 14):
        for j in range(i, 14):
            for k in range(j, 14):
                for l in range(k, 14):
                    file.write("{} {} {} {}: {}\n".format(i, j, k, l, ccheck([i, j, k, l])))
                    print("{} {} {} {}\n".format(i, j, k, l))
    file.close()
#p1 = ccheck([3,6,7,11])
#print(p1)