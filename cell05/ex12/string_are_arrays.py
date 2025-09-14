import sys

count = 0
text = ""

if len(sys.argv) != 2:
    print("none")
else:
    for i in sys.argv[1]:
        if i == "z":
            text += "z"
            count += 1
    if count == 0:
        print("none")
    else:
        print(text)