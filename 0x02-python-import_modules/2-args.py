#!/usr/bin/python3
import sys
def print_arguments():
    arguments = sys.argv[1:]  # Exclude the script name from the arguments
    num_arguments = len(arguments)

    print("Number of argument(s):", num_arguments)

    if num_arguments == 0:
        print(".")
    else:
        print("Arguments:")
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
