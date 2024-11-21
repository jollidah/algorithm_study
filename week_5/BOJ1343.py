import sys

def polyomino(s):
    result = ""
    xcnt = 0
    for char in s + ".":
        if char == "X":
            xcnt += 1
        elif char == ".":
            if xcnt%2 != 0:
                return -1
            while xcnt > 0 :
                if xcnt >= 4:
                    result += "AAAA"
                    xcnt -= 4
                elif xcnt >= 2:
                    result += "BB"
                    xcnt -= 2
            result += "."
            xcnt = 0
    return result[:-1]

def main():
    s = sys.stdin.readline().strip()
    print(polyomino(s))

if __name__=="__main__":
    main()
