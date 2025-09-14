count = 0
while True:
    if count == 0:
        text = input("What you gotta say? : ")
    else:
        text = input("I got that! Anything else? : ")
    if text == "STOP":
        break
    count += 1