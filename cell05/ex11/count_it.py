import sys

if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) -1 }")
    print(f"{sys.argv[1]}: {len(sys.argv[1])}")
    print(f"{sys.argv[2]}: {len(sys.argv[2])}")
    print(f"{sys.argv[3]}: {len(sys.argv[3])}")