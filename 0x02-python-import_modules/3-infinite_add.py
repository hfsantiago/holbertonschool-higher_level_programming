#!/usr/bin/python3
import sys
if __name__ == "__main__":
    aux = 0
    for i in range(1, len(sys.argv)):
        aux = aux + int(sys.argv[i])
    print(aux)
