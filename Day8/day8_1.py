#!/bin/python3
import sys
prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]


def makePattern(phrase, pattern):
    rtn = ""
    for i in range(len(pattern)):
        if(pattern[i] in phrase):
            rtn += pattern[i]
        else:
            rtn += "."
    return rtn
def mapSig(line):
    array = []
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    # for word in line.split(" | ")[0].split(" "):
    #     if len(word) == 2: 
    #         array[0].append("..{}..{}.".format(word[0],word[1]))
    #         array[0].append("..{}..{}.".format(word[1],word[0]))


    #     elif len(word) == 3:
    #         array[1].append("{}.{}..{}.".format(word[0],word[1],word[2]))
    #         array[1].append("{}.{}..{}.".format(word[0],word[2],word[1]))
    #         array[1].append("{}.{}..{}.".format(word[1],word[0],word[2]))
    #         array[1].append("{}.{}..{}.".format(word[1],word[2],word[0]))
    #         array[1].append("{}.{}..{}.".format(word[2],word[1],word[0]))
    #         array[1].append("{}.{}..{}.".format(word[2],word[0],word[1]))


    #     elif len(word) == 4:
    #         local_combos =[]
    #         genCombos(word,local_combos, "")
    #         for combo in local_combos:
    #             array[2].append(".{}{}{}.{}.".format(word[0],word[1],word[2],word[3]))

    #     # print("array")
    #     # for i in array: print(array[i])
    #     # print("array")
    #     # print(word)
    #     # input()

    for combo in global_combos:
        fuck = [0] * 10
        
        key = []
        key.append(makePattern(combo[a] + combo[b] + combo[c] + combo[e] +combo[f] + combo[g],combo)) # 0
        key.append(makePattern(combo[c] + combo[f],combo)) # 1
        key.append(makePattern(combo[a] + combo[c] + combo[d] + combo[e] + combo[g],combo))
        key.append(makePattern(combo[a] + combo[c] + combo[d] + combo[f] + combo[g],combo))
        key.append(makePattern(combo[b] + combo[c] + combo[d] + combo[f],combo))
        key.append(makePattern(combo[a] + combo[b] + combo[d] + combo[f] + combo[g],combo)) # 5
        key.append(makePattern(combo[a] + combo[b] + combo[d] + combo[e] + combo[f] + combo[g],combo))
        key.append(makePattern(combo[a] + combo[c] + combo[f],combo))
        key.append(makePattern(combo[a] + combo[b] + combo[c] + combo[d] + combo[e] + combo[f] + combo[g],combo))
        key.append(makePattern(combo[a] + combo[b] + combo[c] + combo[d] + combo[f] + combo[g],combo))


        for word in line.split(" | ")[0].split(" "):
            pat = makePattern(word,combo)

            for i in range(10):
                if pat == key[i]: 
                    fuck[i] += 1
                    break
        
        #if(combo == "deafgbc"):
        #print(fuck)
        
        if( sum(fuck) == 10 and max(fuck) == 1):
            
            # print("array")
            # for i in array: print(array)
            # print("array")

            








            return key,combo
        

global_combos = []
def genCombos(letters_left, combos, combo="" ):

    if len(letters_left) == 0:
        combos.append(combo)
    else:
        for letter in letters_left:
            genCombos(letters_left.replace(letter,""), combos, combo+letter)

genCombos("abcdefg", global_combos)


#for key in 
 #: print(key)


count = 0
for line in prob_input:
    num = ""
    keys,combo = mapSig(line)
    for word in line.split(" | ")[1].split(" "): 
        pat = makePattern(word,combo)
        for i in range(10):
            if pat == keys[i]: num += str(i)
    count += int(num)
print(count)