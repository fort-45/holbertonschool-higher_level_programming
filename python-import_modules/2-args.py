#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}"i)
    else:
        print(f"{length - 1} arguments:")
        c = 1
        for i in range(1, length):
            print(f"{c}: {sys.argv[i]}")
            c += 1
