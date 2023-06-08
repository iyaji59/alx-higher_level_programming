#!/usr/bin/python3
import sys

def calculate_sum():
    arguments = sys.argv[1:]
    total = sum(int(arg) for arg in arguments)
    print(total)
if __name__ == "__main__":
    calculate_sum()
