from random import randint

row0 = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]

initial = eval(f"row{str(randint(0, 2))}")
eval("exec('initial[randint(0,2)] = \"X\"')")


def display(*rows):
    for x in rows:
        print(x)


def shuffle(*rows):
    row = rows
    limit = 1
    for x in list(row):
        if limit > 0:
            randomize = randint(0, 2)
            if x[randomize] == " ":
                x[randomize] = "X"
                limit -= 1
    return rows


def injector():
    patternO = ["O", "O", "O"]
    patternX = ["X", "X", "X"]
    return (patternO, patternX)


def win_condition(*rows):
    scores = {"O": 0, "X": 0}
    # row
    for x in list(rows):
        patternO, patternX = injector()
        for y in x:
            if y == patternO[0]:
                patternO.pop()
            if y == patternX[0]:
                patternX.pop()
            if len(patternO) == 0:
                scores["O"] += 1
            if len(patternX) == 0:
                scores["X"] += 1

    # col
    for x in range(0, len(rows)):
        patternO, patternX = injector()
        for y in range(0, len(rows)):
            if rows[x][y] == "O":
                patternO.pop()
            if rows[x][y] == "X":
                patternX.pop()
            if len(patternO) == 0:
                scores["O"] += 1
            if len(patternX) == 0:
                scores["X"] += 1

    index = {"x": 0, "y": 0}

    # Diagonal LTR
    for index["x"] in range(0, 3):
        patternO, patternX = injector()
        if rows[index["x"]][index["y"]] == "O":
            patternO.pop()
        if rows[index["x"]][index["y"]] == "X":
            patternX.pop()
        if len(patternO) == 0:
            scores["O"] += 1
        if len(patternX) == 0:
            scores["X"] += 1

        if index["y"] < len(rows):
            index["y"] += 1
        else:
            index["y"] = 0

    index = {"x": 0, "y": len(rows) - 1}

    # Diagonal RTL
    for index["x"] in range(0, 3):
        patternO, patternX = injector()
        if rows[index["x"]][index["y"]] == "O":
            patternO.pop()
        if rows[index["x"]][index["y"]] == "X":
            patternX.pop()
        if len(patternO) == 0:
            scores["O"] += 1
        if len(patternX) == 0:
            scores["X"] += 1
            
        if index["y"] == 0:
            index["y"] = 0
        else:
            index["y"] -= 1

    # Result
    if scores["O"] == scores["X"]:
        print("Draw")
    elif scores["O"] > scores["X"]:
        print("Player O Win")
    elif scores["X"] > scores["O"]:
        print("Player X Win")
    else:
        print("No one win")


while True:
    win_condition(row0, row1, row2)
    display(row0, row1, row2)
    row = int(input("row (0-2): "))
    col = int(input("col (0-2): "))
    if row == 9 or col == 9:
        if input("Are you sure? (y/n)") == "y":
            break
        else:
            continue
    elif row != range(0, 2) and col != range(0, 2):
        if row == 0:
            print(row0[col])
            if row0[col] != "X":
                if row0[col] != "O":
                    row0[col] = "O"
                    shuffle(row0, row1, row2)
                    continue
            print("Already filled!")
        elif row == 1:
            print(row1[col])
            if row1[col] != "X":
                if row1[col] != "O":
                    row1[col] = "O"
                    shuffle(row0, row1, row2)
                    continue
            print("Already filled!")
        elif row == 2:
            print(row2[col])
            if row2[col] != "X":
                if row2[col] != "O":
                    row2[col] = "O"
                    shuffle(row0, row1, row2)
                    continue
            print("Already filled!")
        else:
            print("Invalid input!")
            break
    else:
        print("please input valid row and column")
        continue
