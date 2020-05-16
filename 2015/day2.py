"""
--- Day 2: I Was Told There Would Be No Math ---
https://adventofcode.com/2015/day/2
"""

def base(dimensions: str):
    l,w,h = map(int, dimensions.split("x"))
    area = 2*l*w + 2*w*h + 2*h*l

    shortest, shorter, _ = sorted((l,w,h))
    slack = shorter * shortest

    return area + slack

def main(dimensions: str):
    l,w,h = map(int, dimensions.split("x"))
    area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l * w, l * h, w * h)

    return area + slack

if __name__ == '__main__':
    assert main("2x3x4") == 58
    assert main("1x1x10") == 43
