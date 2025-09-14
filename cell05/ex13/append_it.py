import sys

if len(sys.argv) == 1:
    print("none")
else:
    sys.argv.pop(0)
    for i in sys.argv:
        if i[len(i)-3:len(i)] != "ism":
            print(f"{i}ism")