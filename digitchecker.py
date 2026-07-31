# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = []
for r in range(9):
    rows.append([ch for ch in input() if ch.isdigit()])

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break


# Check if all columns are good.
if ok:
    for c in range(9):
        if not checkset([rows[r][c] for r in range(9)]):
            ok = False
            break


# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = [rows[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
            if not checkset(square):
                ok = False
                break
        if not ok:
            break


# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
    