from random import randint

row0 = [" ", " ", " "]
row0[randint(0, 2)] = "X"
row1 = [" ", " ", " "]
row1[randint(0, 2)] = "X"
row2 = [" ", " ", " "]


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


while True:
    display(row0, row1, row2)
    row = int(input("row (0-2): "))
    col = int(input("col (0-2): "))
    if(row == 9 or col == 9):
        if(input("Are you sure? (y/n)") == "y"):
            break
        else:
            continue
    elif(row != range(0, 2) and col != range(0, 2)):
        if row == 0:
            print(row0[col])
            if row0[col] != 'X':
                if row0[col] != 'O':
                    row0[col] = "O"
                    shuffle(row0, row1, row2)
                    continue
            print("Already filled!")
        elif row == 1:
            print(row1[col])
            if row1[col] != 'X':
                if row1[col] != 'O':
                    row1[col] = "O"
                    shuffle(row0, row1, row2)
                    continue
            print("Already filled!")
        elif row == 2:
            print(row2[col])
            if row2[col] != 'X':
                if row2[col] != 'O':
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
