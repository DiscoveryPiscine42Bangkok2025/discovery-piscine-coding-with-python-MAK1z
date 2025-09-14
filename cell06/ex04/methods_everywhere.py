import sys

def shrink(s):
    return s[0:8]

def enlarge(s):
    if len(s) < 8:
        for i in range(8 - len(s)):
            s += "Z"
        return s

if len(sys.argv) == 1:
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) >= 8:
            print(shrink(i))
        else:
            print(enlarge(i))