
def get_column(chars: int, columns=list(range(8))):
    
    if len(chars) == 1:
        return columns[0] if chars == "L" else columns[1]

    mid = len(columns) // 2
    if chars[0] == "L":
        return get_column(chars[1:], columns[:mid])
    if chars[0] == "R":
        return get_column(chars[1:], columns[mid:])

def get_row(chars: int, rows=list(range(128))):
   
    if len(chars) == 1:
        return rows[0] if chars == "F" else rows[1]

    mid = len(rows) // 2
    if chars[0] == "F":
        return get_row(chars[1:], rows[:mid])
    if chars[0] == "B":
        return get_row(chars[1:], rows[mid:])

with open("input5.txt") as f:
    lines = f.readlines()
   
    seat_ids = []

    for line in lines:
        rchars = line[:7]
        cchars = line[-3:]

        row = get_row(rchars)
        column = get_column(cchars)

        seat_id = row * 8 + column

        seat_ids.append(seat_id)

    print(max(seat_ids))
