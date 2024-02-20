# Note that this program does not exhaustively search every possibility. Some may be marked not possible incorrectly
maxnum = 6
goal = 24
factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040}
symbols = {0:"+", 1:"-", 2:"*", 3:"/", 4:"+", 5:"-", 6:"*", 7:"/"}

def answer(lst):
    # The arrangement of parenthesis is specific to 4 items, but could be abstracted an generalized if needed.
    # adding factorials would require a significant rework of this as they can be applied anywhere at any time.
    permuations = ["{}{}{}{}{}{}{}",        #abcd
                   "{}{}{}{}({}{}{})",      #ab(cd)
                   "{}{}({}{}{}){}{}",      #a(bc)d
                   "({}{}{}){}{}{}{}",      #(ab)cd
                   "({}{}{}){}({}{}{})",    #(ab)(cd)
                   "({}{}{}{}{}){}{}",      #(abc)d
                   "{}{}({}{}{}{}{})",      #a(bcd)
                   "(({}{}{}){}{}){}{}",    #((ab)c)d
                   "({}{}({}{}{})){}{}",    #(a(bc))d
                   "{}{}(({}{}{}){}{})",    #a((bc)d)
                   "{}{}({}{}({}{}{}))"]    #a(b(cd))
    
    # The various indexes at each layer of the nested array where the goal is found tells you
    # what operation was chosen at each step, useful for extracting that information to build 
    # a string for the formula which reaches the goal. Not possible to shortcut except at the last
    # layer for this implementation
    a,b,c,d = lst
    cd = op(c,d)
    bcd = [op(b, x) for x in cd]
    abcd = []
    for x in bcd:
        f = []
        for l in x:
            f.append(op(a,l))
        abcd.append(f)

    result = ""
    #a k b j c i d
    for i in range(len(abcd)):
        for j in range(len(abcd[i])):
            for k in range(len(abcd[i][j])):

                # Possible swaps
                order = [a, b, c, d] 
                if k > 3:
                    old_index = order.index(a)
                    order.remove(a)
                    order.insert(old_index+3, a)
                if j > 3:
                    old_index = order.index(b)
                    order.remove(b)
                    order.insert(old_index+2, b)
                if i > 3:
                    old_index = order.index(c)
                    order.remove(c)
                    order.insert(old_index+1, c)
                    
                for perm in permuations:
                    test = perm.format(order[0],symbols[k],order[1],symbols[j],order[2],symbols[i],order[3])
                    try: 
                        s = eval(test)
                        if s == goal:
                            result = test
                            return result
                        elif factorials[s] == goal:
                            result = "("+test+")!"
                            return result
                    except:
                        continue
    return result

# Factorials are only counted when using one on the final result produces the goal due to the uneccessary complexity
# they would add for my use case. Including them is perfectly feasable, but outside the scope of what I was seeking to do
def op(a, b):
    if a != 0 and b != 0:
        return [a+b, a-b, a*b, a/b, b+a, b-a, b*a, b/a]
    elif a == 0 and b != 0:
        return [b, -b, 0, 0, b, b, 0, float("inf")]
    elif a != 0 and b == 0:
        return [a, a, 0, float("inf"), a, -a, 0, 0]
    else:
        return [0, 0, 0, float("inf"), 0, 0, 0, float("inf")]

def getanswer(lst):
    a,b,c,d = lst

    # There are 24 ways to arrange 4 items but defining that many permutations here is ultimately unneccessary
    # Given 4 items, there are 6 ways of choosing 2. Each has a pair that completes the set perfectly. Since the 
    # op function takes care of the permutations where the items within the pairs are swapped, all that is left
    # is to write the 3 pairs of possible ways to choose 2 with the pairs in either position: yielding the 6 here
    permutations = [[a,b,c,d],
                    [c,d,a,b],
                    [a,c,b,d],
                    [b,d,a,c],
                    [a,d,b,c],
                    [b,c,d,a]]
    for i in range(len(permutations)):
        t = answer(permutations[i])
        if t != "":
            return t
    return "Impossible"


with open("test.txt", "w") as file:
    for i in range(1, maxnum+1):
        for j in range(i, maxnum+1):
            for k in range(j, maxnum+1):
                for l in range(k, maxnum+1):
                    file.write("{} {} {} {}: {}\n".format(i, j, k, l, getanswer([i, j, k, l])))
    file.close()