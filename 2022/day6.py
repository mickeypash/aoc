
test = [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

def lookback_diff(arr, idx, buffer_size=14):

    lookback_buff = []
    for i in range(buffer_size):
        lookback_buff += arr[idx-1-i]
    
    return len(lookback_buff) == len(set(lookback_buff))


def find_marker(arr):
    for i in range(len(arr)):
        if i > 3:
            if lookback_diff(arr, i):
                return i


if __name__ == "__main__":
    datastream = open("input6.txt").read()

    start_of_paket_marker = find_marker(datastream)
    print(start_of_paket_marker)
