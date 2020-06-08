# Characters in phone corresponding to numbers from 2 to 9
charsInPhone = [['a','b','c'],       # 2
['d','e','f'],                       # 3
['g','h','i'],                       # 4
['j','k','l'],                       # 5
['m','n','o'],                       # 6
['p','q','r','s'],                   # 7
['t','u','v'],                       # 8
['w','x','y','z']]                   # 9

# Make sure that the input only consists of 2-9s
def isValidInput(_str):
    for s in _str:
        if s.isdigit() and int(s) >= 2 and int(s) <= 9:
            continue
        else:
            return False
    return True

# Convert the 2-9s to charsInPhone list index
def getIndex(i_str):
    return int(i_str) - 2

# Perform DFS on the string given by the user
# res: result string to be printed
# _str: string provided by the user
# i: index of _str that is to be operated on
def dfs(res, _str, i):
    # If all chars in _str is operated on 
    #then simply print the string
    if i == len(_str):
        print (res + " ")
        return

    chars = charsInPhone[getIndex(_str[i])]
    for char in chars:
        dfs(res + char, _str, i + 1)

# Continue to take input from the user to
# test the dfs function
while True:
    _str = str(input())
    # If there is an error in user input then ignore it
    # and continue to listen for the next input
    if isValidInput(_str) == False:
        continue

    dfs("", _str, 0)
    print ("\n")
