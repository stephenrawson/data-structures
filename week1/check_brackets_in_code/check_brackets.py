# python3

#Good job! (Max time used: 0.08/5.00, max memory used: 11522048/536870912.)

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i,next))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            current = opening_brackets_stack.pop()
            result = are_matching(current[1],next)
            if not result:
                return i + 1
    
    return -1 if len(opening_brackets_stack) == 0 else opening_brackets_stack[0][0]+1

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print('Success')
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
