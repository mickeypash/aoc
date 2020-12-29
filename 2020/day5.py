with open("input5.txt") as f:
    seat_ids = [int("".join(["0" if c == "F" or c == "L" else "1" for c in line]), 2) for line in f.read().splitlines()]
    # part 1
    print(max(seat_ids))

    sorted_seat_ids = sorted(seat_ids)
    starting = sorted_seat_ids[0]

    # part 2 
    for i, seat_id in enumerate(sorted_seat_ids, starting):
        if i < seat_id:
            print(i)
            break
