


if __name__ == '__main__':
    
    input = """
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    """
    
    valid_passwords = 0

    with open("input2.txt", "r") as f:
        lines = [l.rstrip() for l in f.readlines()]

        for line in lines:

            col1, col2, col3 = line.split(" ")

            lower, upper = col1.split("-")
            character = col2[0]
            password = col3

            print(lower, upper, character, password)

            count = 0
            for char in password:
                if char == character:
                    count += 1

            if int(lower) <= count <= int(upper):
                #print("Hurrah")
                valid_passwords += 1
    
    print(f"Number of valid passwords: {valid_passwords}")
