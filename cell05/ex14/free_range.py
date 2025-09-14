import sys

my_list = []

if len(sys.argv) != 3:
    print("none")
else:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        if int(sys.argv[1]) > int(sys.argv[2]):
            for i in range(int(sys.argv[1]), int(sys.argv[2]), -1):
                my_list.append(i)
        else:
            for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
                my_list.append(i)
        print(my_list)
    else:
        print("none")