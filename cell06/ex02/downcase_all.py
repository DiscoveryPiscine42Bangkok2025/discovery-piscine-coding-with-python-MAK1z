import sys

def lower_it(s):
    return s.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for i in sys.argv:
        print(lower_it(i))