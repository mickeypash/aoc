
def get_row(chars, lower, rows):
   
    if len(chars) == 1:
        return rows[0] if chars == lower else rows[1]

    mid = len(rows) // 2
    if chars[0] == lower:
        return get_row(chars[1:], lower, rows[:mid])
    return get_row(chars[1:], lower, rows[mid:])

with open("input5.txt") as f:
    lines = f.readlines()
   
    seat_ids = []

    ROWS = range(128)
    COLUMNS = range(8)

    for line in lines:
        rchars = line[:7]
        cchars = line[-3:]

        row = get_row(rchars, "F", ROWS)
        column = get_row(cchars, "L", COLUMNS)

        seat_id = row * 8 + column

        seat_ids.append(seat_id)

    print(sorted(set(seat_ids)))
