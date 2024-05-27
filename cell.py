import sys

cells = {0: "\n", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k",
        12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w",
        24: "x", 25: "y", 26: "z", 27: " ", 28: "{", 29: "}", 30: "(", 31: ")", 32: ".", 33: ",", 34: ";", 35: "*",
        36: "+", 37: "-", 38: "[", 39: "]", 40: "!", 41: "?", 42: "&", 43: "$", 44: "@", 45: "#", 46: "\"", 47: "'",
        48: "^", 49: "~", 50: "%", 51: "=", 52: "°", 53: "/", 54: "|", 55: "\\", 56: "_",}


def interpret(code):
    lines = code.split("\n")
    cellpos = 0

    for line in lines:
        tokens = list(line)

        for token in tokens:
            if token == ">":
                cellpos += 1
            elif token == "<":
                cellpos -= 1
            elif token == "*":
                for cell in cells:
                    if cellpos == cell:
                        print(cells[cellpos], end="")
            elif token == "!":
                for cell in cells:
                    if cellpos == cell:
                        print(cells[cellpos].upper(), end="")
            elif token == "&":
                print(cellpos)
            else:
                print(f"Uknown token: '{token}'. tokens: '>', '<', '*', '!'.")

if __name__ == "__main__":
    version = "1.0"
    if len(sys.argv) == 1:
        print(f"Celllang version: {version}")
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        if sys.argv[1].endswith(".cell"):
            with open(sys.argv[1], "r") as f:
                interpret(f.read())
        else:
            print("Use '.cell' file extension")
