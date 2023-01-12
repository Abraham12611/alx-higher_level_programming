#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = sum(int(args) for args in sys.argv[1:])
    print(result)
